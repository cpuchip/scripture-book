<#
.SYNOPSIS
    Narrate "Beyond the Prompt" into an audiobook (mp3 / m4a / mp4) via a local Voicebox server.

.DESCRIPTION
    Wraps scripts/narrate.py. Each chapter in book.yaml becomes speakable text, is sent to
    Voicebox (https://github.com/jamiepine/voicebox) /generate, and the chapters are combined
    into mp3 + m4a (with chapter markers) under dist/audiobook/. Per-chapter mp3s land in
    dist/audiobook/chapters/.

    Two modes need NO Voicebox (good for iterating on the text + the encode):
      -DryRun       cleans every chapter to dist/audiobook/text/*.txt + manifest.json
      -CombineOnly  rebuilds the combined outputs from existing dist/audiobook/wav/*.wav

    Generation needs Voicebox running locally (default http://127.0.0.1:17493). Install it,
    download a voice (or clone your own), then:
      .\narrate.ps1 -Probe                 # list available voices
      .\narrate.ps1 -Voice "Michael"       # narrate the whole book

.PARAMETER Voice
    Voice profile name (or id) to narrate in. Required for generation.

.PARAMETER Probe
    List the voices Voicebox currently has, and exit.

.PARAMETER DryRun
    Clean every chapter to narration text + a manifest; no Voicebox needed.

.PARAMETER CombineOnly
    Rebuild mp3/m4a/mp4 from the chapter wavs already in dist/audiobook/wav/.

.PARAMETER Chapter
    Narrate just one chapter: a 0-based index or a filename substring (for sample passes).

.PARAMETER Engine
    TTS engine: qwen (default), kokoro, chatterbox, chatterbox_turbo, luxtts, tada, qwen_custom_voice.

.PARAMETER Instruct
    Delivery instruction, e.g. "read slowly, warm, reverent" (qwen/custom-voice).

.PARAMETER Formats
    Comma list of combined outputs: mp3,m4a,mp4 (default mp3,m4a). mp4 needs a cover
    (run .\build.ps1 -Cover first).

.EXAMPLE
    .\narrate.ps1 -DryRun
    Preview the narration text for every chapter (no Voicebox).

.EXAMPLE
    .\narrate.ps1 -Voice "Michael" -Chapter 3 -Instruct "read slowly, warm"
    Narrate one chapter as a sample to dial in the voice and pacing.

.EXAMPLE
    .\narrate.ps1 -Voice "Michael" -Formats mp3,m4a,mp4
    Full audiobook in all three formats.
#>
[CmdletBinding()]
param(
    [string]$Voice,
    [switch]$Probe,
    [switch]$DryRun,
    [switch]$CombineOnly,
    [string]$Chapter,
    [string]$Engine = "qwen",
    [string]$Instruct,
    [string]$Seed,
    [string]$ApiHost = "http://127.0.0.1:17493",
    [string]$Formats = "mp3,m4a"
)

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

$py = (Get-Command python -ErrorAction SilentlyContinue) ?? (Get-Command python3 -ErrorAction SilentlyContinue)
if (-not $py) { throw "python not found on PATH." }

$pyArgs = @("scripts/narrate.py", "--host", $ApiHost, "--engine", $Engine, "--formats", $Formats)
if ($Probe)       { $pyArgs += "--probe" }
if ($DryRun)      { $pyArgs += "--dry-run" }
if ($CombineOnly) { $pyArgs += "--combine-only" }
if ($Voice)       { $pyArgs += @("--voice", $Voice) }
if ($Chapter)     { $pyArgs += @("--chapter", $Chapter) }
if ($Instruct)    { $pyArgs += @("--instruct", $Instruct) }
if ($Seed)        { $pyArgs += @("--seed", $Seed) }

& $py.Source @pyArgs
