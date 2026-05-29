#!/usr/bin/env bash
# build.sh — Build "Beyond the Prompt" PDF + HTML + EPUB
#
# Usage:
#   ./build.sh           Build everything (HTML, EPUB, PDF via Docker)
#   ./build.sh --quick   HTML + EPUB only (skip Docker / PDF)
#   ./build.sh --pdf     PDF only (skip HTML / EPUB)
#   ./build.sh --help    Show this help
#
# Requires:
#   python3                 always
#   docker (Docker Desktop) for PDF builds (not needed with --quick)
#
# Run from the project root. Output lands in ./dist/

set -e
cd "$(dirname "$0")"

MODE="full"
for arg in "$@"; do
  case $arg in
    --quick) MODE="quick" ;;
    --pdf)   MODE="pdf" ;;
    -h|--help)
      sed -n '/^# Usage:/,/^# Run from/p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      echo "Run './build.sh --help' for usage." >&2
      exit 1
      ;;
  esac
done

# HTML + EPUB via Python
if [[ "$MODE" != "pdf" ]]; then
  echo "==> Building HTML and EPUB..."
  python scripts/build.py
fi

# PDF via Docker (multi-stage: Python → Typst → output)
if [[ "$MODE" != "quick" ]]; then
  if ! command -v docker > /dev/null; then
    echo "Docker not found. Install Docker Desktop or run with --quick to skip PDF." >&2
    exit 1
  fi

  echo "==> Building PDF (Docker → Typst)..."
  docker build -t scripture-book-builder . > /tmp/scripture-book-docker.log 2>&1 || {
    echo "Docker build failed. Last 20 lines of log:" >&2
    tail -20 /tmp/scripture-book-docker.log >&2
    exit 1
  }
  echo "    Docker image built."

  # Handle Windows path translation for the volume mount
  if command -v cygpath > /dev/null; then
    OUTPUT_DIR="$(cygpath -w "$PWD/dist")"
  elif pwd -W > /dev/null 2>&1; then
    OUTPUT_DIR="$(pwd -W)/dist"
  else
    OUTPUT_DIR="$PWD/dist"
  fi

  docker run --rm -v "${OUTPUT_DIR}:/output" scripture-book-builder
fi

echo ""
echo "==> Build complete. Artifacts in dist/:"
ls -lh dist/*.pdf dist/*.html dist/*.epub 2>/dev/null | awk '{printf "    %-32s %s\n", $NF, $5}'
