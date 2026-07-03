<#
.SYNOPSIS
    Build "Beyond the Prompt" PDF + HTML + EPUB.

.DESCRIPTION
    Wraps the three-step pipeline behind one command:
      1. python scripts/build.py        (HTML + EPUB)
      2. docker build + docker run      (PDF via Typst, multi-stage)

    Run from anywhere — the script sets its working directory to its
    own location. Output lands in ./dist/.

.PARAMETER Quick
    Skip Docker; build HTML + EPUB only (~3 seconds, no PDF).
    Use for fast iteration during small edits.

.PARAMETER Pdf
    Build PDF only (skip HTML + EPUB).

.PARAMETER Cover
    Render the full-wrap paperback cover only (src/cover.typ -> dist/cover.pdf +
    dist/cover_preview.png). Open cover_preview.png to view it. Update the `pages`
    value in src/cover.typ after the interior page count is final.

.EXAMPLE
    .\build.ps1
    Full build: HTML + EPUB + PDF.

.EXAMPLE
    .\build.ps1 -Quick
    Fast iteration after a small edit — HTML + EPUB only.

.EXAMPLE
    .\build.ps1 -Pdf
    PDF only (skips HTML + EPUB regeneration).

.EXAMPLE
    .\build.ps1 -Cover
    Render the cover wrap + a preview PNG into dist/.

.NOTES
    Requires:
        python3                 always
        docker (Docker Desktop) for PDF builds (not needed with -Quick)
#>

[CmdletBinding()]
param(
    [switch]$Quick,
    [switch]$Pdf,
    [switch]$Cover,
    [switch]$Book2
)

# Note: not using `$ErrorActionPreference = 'Stop'` because native commands
# (docker, python) routinely write progress to stderr, and PowerShell's
# Stop mode treats those as terminating errors. We use $LASTEXITCODE
# checks instead.

Set-Location $PSScriptRoot

# Cover-only: render the full-wrap paperback cover via Typst (Docker), plus a preview PNG.
if ($Cover) {
    if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
        Write-Error "Docker not found. Install Docker Desktop to render the cover."
        exit 1
    }
    New-Item -ItemType Directory -Force (Join-Path $PSScriptRoot "dist") | Out-Null
    Write-Host "==> Rendering cover (Docker -> Typst)..." -ForegroundColor Cyan
    docker run --rm -v "${PSScriptRoot}:/work" ghcr.io/typst/typst:latest compile /work/src/cover.typ /work/dist/cover.pdf
    if ($LASTEXITCODE -ne 0) { Write-Error "Cover PDF render failed with exit code $LASTEXITCODE."; exit $LASTEXITCODE }
    docker run --rm -v "${PSScriptRoot}:/work" ghcr.io/typst/typst:latest compile --ppi 150 /work/src/cover.typ /work/dist/cover_preview.png
    Write-Host ""
    Write-Host "==> Cover rendered into dist/:" -ForegroundColor Green
    Write-Host "    cover.pdf            (print-ready full wrap, 12.527 x 9.25 in @ 123 pp)"
    Write-Host "    cover_preview.png    (open this to view)"
    exit 0
}

# Build version stamp (short git hash + -dirty + commit date) for the frontmatter
# Edition line. Passed to the host Python build via $env:BUILD_VERSION and to the Docker
# PDF build via --build-arg (git is not available inside the Typst image).
$gitHash = (git -C $PSScriptRoot rev-parse --short HEAD 2>$null)
if ($gitHash) {
    $gitDirty = (git -C $PSScriptRoot status --porcelain 2>$null)
    $gitDate  = (git -C $PSScriptRoot show -s --format=%cs HEAD 2>$null)
    $buildVer = "$gitHash$(if ($gitDirty) { '-dirty' } else { '' }) ($gitDate)"
} else {
    $buildVer = "uncommitted build"
}
$env:BUILD_VERSION = $buildVer
Write-Host "==> Build version: $buildVer" -ForegroundColor DarkGray

# Book selection: default = Book One (book.yaml -> dist/); -Book2 = book-2.yaml -> dist-book-2/
$bookConfig = if ($Book2) { "book-2.yaml" } else { "book.yaml" }
$distName   = if ($Book2) { "dist-book-2" } else { "dist" }
$imageTag   = if ($Book2) { "scripture-book2-builder" } else { "scripture-book-builder" }
$env:BOOK_CONFIG = $bookConfig
$env:DIST_DIR    = $distName
if ($Book2) { Write-Host "==> Building BOOK TWO ($bookConfig -> $distName/)" -ForegroundColor Cyan }

# HTML + EPUB via Python
if (-not $Pdf) {
    Write-Host "==> Building HTML and EPUB..." -ForegroundColor Cyan
    python scripts/build.py
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Python build failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
}

# PDF via Docker (multi-stage: Python -> Typst -> output)
if (-not $Quick) {
    if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
        Write-Error "Docker not found. Install Docker Desktop or run with -Quick to skip PDF."
        exit 1
    }

    Write-Host "==> Building PDF (Docker -> Typst)..." -ForegroundColor Cyan

    $dockerLog = Join-Path $env:TEMP "scripture-book-docker.log"
    # 2>&1 merges stderr into stdout before redirection so PowerShell
    # doesn't surface progress messages as errors.
    docker build --build-arg "BUILD_VERSION=$buildVer" --build-arg "BOOK_CONFIG=$bookConfig" -t $imageTag . 2>&1 | Out-File -FilePath $dockerLog
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Docker build failed. Last 20 lines of ${dockerLog} :" -ForegroundColor Red
        Get-Content $dockerLog -Tail 20
        exit $LASTEXITCODE
    }
    Write-Host "    Docker image built."

    # Mount the output directory as /output in the container.
    # Docker on Windows parses the Windows path (with drive-letter colon)
    # correctly because it splits on the rightmost colon.
    $hostDist = (Join-Path $PSScriptRoot $distName)
    New-Item -ItemType Directory -Force $hostDist | Out-Null
    docker run --rm -v "${hostDist}:/output" $imageTag
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Docker run failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "==> Build complete. Artifacts in ${distName}/:" -ForegroundColor Green
Get-ChildItem -Path (Join-Path $PSScriptRoot "$distName\*") -Include manuscript.pdf, manuscript.html, beyond_the_prompt.epub -File -ErrorAction SilentlyContinue |
    Sort-Object Name |
    ForEach-Object {
        $size = "{0,7:N0} KB" -f ($_.Length / 1KB)
        Write-Host ("    {0,-32} {1}" -f $_.Name, $size)
    }
