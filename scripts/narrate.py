#!/usr/bin/env python3
"""
Narrate "Beyond the Prompt" into an audiobook via a local Voicebox server.

Voicebox (https://github.com/jamiepine/voicebox) is a local-first TTS studio with a
REST API. This script turns each chapter in book.yaml into speakable text, sends it to
Voicebox /generate, polls until done, fetches the audio, and combines the chapters into
mp3 / m4a (with chapter markers) / mp4 outputs under dist/audiobook/.

Stdlib only (urllib + subprocess/ffmpeg) — same no-dependency ethos as build.py.

The Voicebox contract (verified against backend/routes + backend/models.py):
  POST /generate            -> {"id", "status": "generating", ...}   (body: GenerationRequest)
  GET  /generate/{id}/status-> SSE "data: {status, duration, error}" until completed/failed
  GET  /audio/{id}          -> the audio file (wav)
  GET  /profiles            -> [{"id","name",...}]   (resolve a voice by name)
Voicebox itself does sentence-boundary chunking + crossfade, so we send a whole chapter
per call (<= 50000 chars; longer chapters are split here and concatenated).

USAGE
  # No Voicebox needed (testable now):
  python scripts/narrate.py --dry-run            # clean every chapter -> dist/audiobook/text/*.txt + manifest
  python scripts/narrate.py --combine-only       # (re)build mp3/m4a/mp4 from existing dist/audiobook/wav/*.wav

  # Needs a running Voicebox (http://127.0.0.1:17493):
  python scripts/narrate.py --probe                       # list available voices + check connectivity
  python scripts/narrate.py --voice "Michael"             # narrate the whole book in that voice
  python scripts/narrate.py --voice "Michael" --chapter 4 # just one chapter (sample pass)
  python scripts/narrate.py --voice "Michael" --engine kokoro --instruct "read slowly, warm"

See narrate.ps1 for a wrapper. Output layout is documented in build_audiobook()'s docstring.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

# Reuse build.py's book.yaml reader so the chapter order has a single source of truth.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import parse_yaml  # noqa: E402

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(PROJECT_ROOT, "dist")
AUDIO_DIR = os.path.join(DIST, "audiobook")
DEFAULT_HOST = "http://127.0.0.1:17493"
DEFAULT_CPS = 15.0  # rough chars-per-second, only for dry-run duration estimates


# ---------------------------------------------------------------------------
# 1. Markdown -> speakable narration text
# ---------------------------------------------------------------------------

def clean_chapter(md: str):
    """Reduce a chapter's Markdown to clean, speakable prose.

    Returns (text, warnings). Drops everything a narrator shouldn't read aloud:
    QR markers, link URLs (keeps the link *text* — so "Abraham 4:26" is spoken),
    footnotes, code blocks, HTML, and emphasis markup. Headings become spoken
    section titles; blockquotes (Remember boxes, scripture) are read as prose.
    """
    warnings = []
    md = md.replace("{{BUILD_VERSION}}", "")

    # HTML comments (provenance markers) and fenced code blocks — never narrated.
    md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
    n_code = len(re.findall(r"```.*?```", md, flags=re.DOTALL))
    if n_code:
        warnings.append(f"dropped {n_code} code block(s)")
    md = re.sub(r"```.*?```", "", md, flags=re.DOTALL)

    # Footnotes: drop definition lines, strip inline refs. (Audiobooks omit them.)
    n_fn = len(re.findall(r"^\[\^[^\]]+\]:", md, flags=re.MULTILINE))
    if n_fn:
        warnings.append(f"dropped {n_fn} footnote definition(s)")
    md = re.sub(r"^\[\^[^\]]+\]:.*$", "", md, flags=re.MULTILINE)
    md = re.sub(r"\[\^[^\]]+\]", "", md)

    # QR markers, then images, then links -> keep link text only.
    md = re.sub(r"\[qr\]\([^)]*\)", "", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)

    # Headings -> spoken title (ensure it ends with a period so TTS pauses).
    def _heading(m):
        t = m.group(1).strip().rstrip(".")
        return (t + ".") if t else ""
    md = re.sub(r"^#{1,6}\s*(.*)$", _heading, md, flags=re.MULTILINE)

    # Blockquotes -> prose. Horizontal rules -> paragraph break.
    md = re.sub(r"^>\s?(.*)$", r"\1", md, flags=re.MULTILINE)
    md = re.sub(r"^(?:---+|\*\*\*+)\s*$", "", md, flags=re.MULTILINE)

    # List bullets -> sentence text.
    md = re.sub(r"^\s*[-*]\s+(.*)$", r"\1", md, flags=re.MULTILINE)
    md = re.sub(r"^\s*\d+\.\s+(.*)$", r"\1", md, flags=re.MULTILINE)

    # Emphasis + inline code.
    md = re.sub(r"\*\*([^*]+)\*\*", r"\1", md)
    md = re.sub(r"\*([^*]+)\*", r"\1", md)
    md = re.sub(r"__([^_]+)__", r"\1", md)
    md = re.sub(r"`([^`]+)`", r"\1", md)

    # Any stray HTML tags (build.py restores some raw blocks in the source).
    md = re.sub(r"<[^>]+>", "", md)

    # Readability normalizations for TTS.
    md = re.sub(r"\s*·\s*", ". ", md)  # "Practice 1 · Talk" -> "Practice 1. Talk"
    md = md.replace("&amp;", "&").replace("&nbsp;", " ")
    md = re.sub(r"[ \t]+", " ", md)
    md = re.sub(r" *\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md, warnings


def chapter_title(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.*)$", md, flags=re.MULTILINE)
    title = m.group(1).strip() if m else fallback
    return title.replace("·", "-").replace("**", "").strip()


def slug_for(index: int, path: str) -> str:
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r"[^a-zA-Z0-9_-]+", "_", base)
    return f"{index:02d}_{base}"


def load_book():
    cfg = parse_yaml(os.path.join(PROJECT_ROOT, "book.yaml"))
    chapters = cfg.get("chapters", [])
    return {
        "title": cfg.get("title", "Beyond the Prompt"),
        "author": cfg.get("author", "Michael Stufflebeam"),
        "language": (cfg.get("language", "en-US") or "en")[:2],
        "chapters": chapters,
    }


# ---------------------------------------------------------------------------
# 2. Voicebox REST client (stdlib urllib)
# ---------------------------------------------------------------------------

def _get_json(url: str, timeout=30):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def list_profiles(host: str):
    return _get_json(host.rstrip("/") + "/profiles")


def resolve_voice(host: str, name: str):
    """Resolve a voice profile by name (case-insensitive) or id -> profile dict."""
    profiles = list_profiles(host)
    for p in profiles:
        if p.get("id") == name or (p.get("name", "").lower() == name.lower()):
            return p
    raise SystemExit(
        f"Voice '{name}' not found. Available: "
        + ", ".join(repr(p.get("name")) for p in profiles)
        + "  (create or clone one in the Voicebox app first)"
    )


def post_generate(host: str, text: str, profile_id: str, *, language="en", engine="qwen",
                  model_size="1.7B", instruct=None, seed=None, max_chunk_chars=800,
                  crossfade_ms=50):
    body = {
        "profile_id": profile_id,
        "text": text,
        "language": language,
        "engine": engine,
        "personality": False,  # narrate verbatim — never rewrite the manuscript
        "normalize": True,
        "max_chunk_chars": max_chunk_chars,
        "crossfade_ms": crossfade_ms,
    }
    if engine == "qwen":
        body["model_size"] = model_size
    if instruct:
        body["instruct"] = instruct
    if seed is not None:
        body["seed"] = seed
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(host.rstrip("/") + "/generate", data=data,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def wait_for_generation(host: str, gen_id: str, timeout=1800):
    """Read the SSE status stream until the generation completes or fails."""
    url = f"{host.rstrip('/')}/generate/{gen_id}/status"
    req = urllib.request.Request(url, headers={"Accept": "text/event-stream"})
    last = {}
    with urllib.request.urlopen(req, timeout=timeout) as r:
        for raw in r:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            try:
                last = json.loads(line[5:].strip())
            except json.JSONDecodeError:
                continue
            status = last.get("status")
            if status in ("completed", "failed", "not_found"):
                if status != "completed":
                    raise SystemExit(f"generation {gen_id} {status}: {last.get('error')}")
                return last
    return last


def fetch_audio(host: str, gen_id: str, dest: str):
    url = f"{host.rstrip('/')}/audio/{gen_id}"
    with urllib.request.urlopen(url, timeout=120) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return dest


# ---------------------------------------------------------------------------
# 3. ffmpeg combine/encode
# ---------------------------------------------------------------------------

def ffprobe_seconds(path: str) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        stderr=subprocess.STDOUT).decode().strip()
    try:
        return float(out)
    except ValueError:
        return 0.0


def cover_image():
    """Use the rendered cover preview if the cover build has been run."""
    for name in ("cover_preview.png", "cover.png"):
        p = os.path.join(DIST, name)
        if os.path.exists(p):
            return p
    return None


def encode_chapter_mp3(wav: str, out_mp3: str, cover=None):
    cmd = ["ffmpeg", "-y", "-i", wav]
    if cover:
        cmd += ["-i", cover, "-map", "0:a", "-map", "1:v", "-disposition:v", "attached_pic"]
    cmd += ["-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", out_mp3]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def write_ffmetadata(meta_path, title, author, chapters):
    """chapters: list of (title, start_ms, end_ms)."""
    lines = [";FFMETADATA1", f"title={title}", f"artist={author}",
             f"album={title}", "genre=Audiobook"]
    for ch_title, start_ms, end_ms in chapters:
        safe = ch_title.replace("=", "-").replace(";", ",").replace("\\", "/").replace("#", "")
        lines += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={start_ms}",
                  f"END={end_ms}", f"title={safe}"]
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def build_combined(wavs, chapters_meta, title, author, formats):
    """Concatenate chapter wavs into combined outputs with chapter markers.

    wavs: ordered list of wav paths. chapters_meta: list of (title, start_ms, end_ms).
    formats: subset of {"mp3","m4a","mp4"}.
    """
    concat_path = os.path.join(AUDIO_DIR, "_concat.txt")
    meta_path = os.path.join(AUDIO_DIR, "_chapters.ffmeta")
    with open(concat_path, "w", encoding="utf-8") as f:
        for w in wavs:
            f.write("file '%s'\n" % os.path.abspath(w).replace("'", r"'\''"))
    write_ffmetadata(meta_path, title, author, chapters_meta)
    cover = cover_image()
    stem = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "audiobook"
    outputs = []

    base_in = ["-f", "concat", "-safe", "0", "-i", concat_path, "-i", meta_path]

    if "mp3" in formats:
        out = os.path.join(AUDIO_DIR, stem + ".mp3")
        cmd = ["ffmpeg", "-y"] + base_in
        if cover:
            cmd += ["-i", cover]
        cmd += ["-map_metadata", "1", "-map", "0:a"]
        if cover:
            cmd += ["-map", "2:v", "-disposition:v", "attached_pic"]
        cmd += ["-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-id3v2_version", "3", out]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        outputs.append(out)

    if "m4a" in formats:  # AAC with embedded chapter markers (audiobook-style)
        out = os.path.join(AUDIO_DIR, stem + ".m4a")
        cmd = ["ffmpeg", "-y"] + base_in + ["-map_metadata", "1", "-map", "0:a",
                                            "-c:a", "aac", "-b:a", "128k", "-ar", "44100", out]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        outputs.append(out)

    if "mp4" in formats:  # cover image as a still video track + the audio
        out = os.path.join(AUDIO_DIR, stem + ".mp4")
        if not cover:
            print("  ! mp4 skipped — no cover image (run build.ps1 -Cover first)")
        else:
            cmd = ["ffmpeg", "-y", "-loop", "1", "-i", cover] + base_in + [
                "-map_metadata", "2", "-map", "0:v", "-map", "1:a",
                "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "128k", "-shortest", out]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            outputs.append(out)

    return outputs


# ---------------------------------------------------------------------------
# 4. Orchestration
# ---------------------------------------------------------------------------

def select_chapters(book, which):
    """which: None (all), an int index, or a substring match on the path."""
    items = list(enumerate(book["chapters"]))
    if which is None:
        return items
    if which.isdigit():
        i = int(which)
        return [items[i]] if 0 <= i < len(items) else []
    return [(i, p) for i, p in items if which.lower() in p.lower()]


def chapters_metadata(wavs_with_titles):
    """Build (title, start_ms, end_ms) markers from actual wav durations."""
    meta, cursor = [], 0
    for wav, title in wavs_with_titles:
        dur_ms = int(round(ffprobe_seconds(wav) * 1000))
        meta.append((title, cursor, cursor + dur_ms))
        cursor += dur_ms
    return meta


def run(args):
    book = load_book()
    os.makedirs(AUDIO_DIR, exist_ok=True)
    for sub in ("text", "wav", "chapters"):
        os.makedirs(os.path.join(AUDIO_DIR, sub), exist_ok=True)

    if args.probe:
        profiles = list_profiles(args.host)
        print(f"Voicebox at {args.host} — {len(profiles)} voice profile(s):")
        for p in profiles:
            kind = p.get("voice_type", "?")
            print(f"  - {p.get('name')!r}  [{kind}]  id={p.get('id')}")
        return

    selected = select_chapters(book, args.chapter)
    if not selected:
        raise SystemExit(f"no chapters matched --chapter {args.chapter!r}")

    # ---- dry-run: clean text only, no Voicebox ----
    if args.dry_run:
        manifest = {"title": book["title"], "chapters": []}
        total_chars = 0
        for i, path in selected:
            full = os.path.join(PROJECT_ROOT, path)
            md = open(full, encoding="utf-8").read() if os.path.exists(full) else ""
            if not md:
                print(f"  ! missing: {path}")
                continue
            text, warns = clean_chapter(md)
            slug = slug_for(i, path)
            with open(os.path.join(AUDIO_DIR, "text", slug + ".txt"), "w", encoding="utf-8") as f:
                f.write(text)
            total_chars += len(text)
            manifest["chapters"].append({
                "index": i, "slug": slug, "title": chapter_title(md, slug),
                "chars": len(text), "est_seconds": round(len(text) / DEFAULT_CPS, 1),
                "warnings": warns,
            })
            wtxt = ("  [" + "; ".join(warns) + "]") if warns else ""
            print(f"  {slug}: {len(text):>6} chars (~{len(text)/DEFAULT_CPS/60:.1f} min){wtxt}")
        with open(os.path.join(AUDIO_DIR, "manifest.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        est_min = total_chars / DEFAULT_CPS / 60
        print(f"\nDry run complete: {len(manifest['chapters'])} chapters, "
              f"{total_chars} chars, ~{est_min:.0f} min of audio.")
        print(f"Narration text + manifest.json written to {os.path.relpath(AUDIO_DIR, PROJECT_ROOT)}/")
        return

    # ---- combine-only: rebuild outputs from existing wavs ----
    if args.combine_only:
        wavs_with_titles = []
        for i, path in selected:
            slug = slug_for(i, path)
            wav = os.path.join(AUDIO_DIR, "wav", slug + ".wav")
            if not os.path.exists(wav):
                print(f"  ! no wav for {slug} (generate it first)")
                continue
            full = os.path.join(PROJECT_ROOT, path)
            md = open(full, encoding="utf-8").read() if os.path.exists(full) else ""
            wavs_with_titles.append((wav, chapter_title(md, slug)))
        if not wavs_with_titles:
            raise SystemExit("no chapter wavs found under dist/audiobook/wav/")
        meta = chapters_metadata(wavs_with_titles)
        outs = build_combined([w for w, _ in wavs_with_titles], meta,
                              book["title"], book["author"], args.formats)
        print("Combined:", ", ".join(os.path.relpath(o, PROJECT_ROOT) for o in outs))
        return

    # ---- full / per-chapter generation (needs Voicebox running) ----
    if not args.voice:
        raise SystemExit("--voice NAME is required for generation "
                         "(use --probe to list voices, or --dry-run to preview text)")
    profile = resolve_voice(args.host, args.voice)
    print(f"Narrating in voice {profile.get('name')!r} (engine={args.engine}) via {args.host}")
    wavs_with_titles = []
    for i, path in selected:
        full = os.path.join(PROJECT_ROOT, path)
        md = open(full, encoding="utf-8").read() if os.path.exists(full) else ""
        if not md:
            print(f"  ! missing: {path}")
            continue
        text, warns = clean_chapter(md)
        slug = slug_for(i, path)
        if not text.strip():
            print(f"  - {slug}: empty after cleaning, skipped")
            continue
        print(f"  {slug}: generating {len(text)} chars...", end="", flush=True)
        gen = post_generate(args.host, text, profile["id"], language=book["language"],
                            engine=args.engine, instruct=args.instruct, seed=args.seed,
                            max_chunk_chars=args.max_chunk_chars, crossfade_ms=args.crossfade_ms)
        wait_for_generation(args.host, gen["id"])
        wav = os.path.join(AUDIO_DIR, "wav", slug + ".wav")
        fetch_audio(args.host, gen["id"], wav)
        mp3 = os.path.join(AUDIO_DIR, "chapters", slug + ".mp3")
        encode_chapter_mp3(wav, mp3, cover=cover_image())
        dur = ffprobe_seconds(wav)
        print(f" done ({dur/60:.1f} min) -> {os.path.relpath(mp3, PROJECT_ROOT)}")
        wavs_with_titles.append((wav, chapter_title(md, slug)))

    if not wavs_with_titles:
        raise SystemExit("nothing generated")
    meta = chapters_metadata(wavs_with_titles)
    outs = build_combined([w for w, _ in wavs_with_titles], meta,
                          book["title"], book["author"], args.formats)
    print("\nAudiobook:", ", ".join(os.path.relpath(o, PROJECT_ROOT) for o in outs))
    print(f"Per-chapter mp3s in {os.path.relpath(os.path.join(AUDIO_DIR, 'chapters'), PROJECT_ROOT)}/")


def main():
    ap = argparse.ArgumentParser(description="Narrate Beyond the Prompt via Voicebox.")
    ap.add_argument("--host", default=DEFAULT_HOST, help=f"Voicebox base URL (default {DEFAULT_HOST})")
    ap.add_argument("--voice", help="voice profile name (or id) to narrate in")
    ap.add_argument("--engine", default="qwen",
                    choices=["qwen", "qwen_custom_voice", "luxtts", "chatterbox",
                             "chatterbox_turbo", "tada", "kokoro"])
    ap.add_argument("--instruct", help="delivery instruction, e.g. 'read slowly, warm, reverent'")
    ap.add_argument("--seed", type=int, help="pin a seed for reproducible takes")
    ap.add_argument("--chapter", help="one chapter: an index (0-based) or a filename substring")
    ap.add_argument("--max-chunk-chars", type=int, default=800)
    ap.add_argument("--crossfade-ms", type=int, default=50)
    ap.add_argument("--formats", default="mp3,m4a",
                    help="comma list of combined outputs: mp3,m4a,mp4 (default mp3,m4a)")
    ap.add_argument("--dry-run", action="store_true",
                    help="clean every chapter to text + manifest; no Voicebox needed")
    ap.add_argument("--combine-only", action="store_true",
                    help="rebuild combined outputs from existing dist/audiobook/wav/*.wav")
    ap.add_argument("--probe", action="store_true", help="list Voicebox voices and exit")
    args = ap.parse_args()
    args.formats = {f.strip() for f in args.formats.split(",") if f.strip()}
    run(args)


if __name__ == "__main__":
    main()
