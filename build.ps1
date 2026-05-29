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

.EXAMPLE
    .\build.ps1
    Full build: HTML + EPUB + PDF.

.EXAMPLE
    .\build.ps1 -Quick
    Fast iteration after a small edit — HTML + EPUB only.

.EXAMPLE
    .\build.ps1 -Pdf
    PDF only (skips HTML + EPUB regeneration).

.NOTES
    Requires:
        python3                 always
        docker (Docker Desktop) for PDF builds (not needed with -Quick)
#>

[CmdletBinding()]
param(
    [switch]$Quick,
    [switch]$Pdf
)

# Note: not using `$ErrorActionPreference = 'Stop'` because native commands
# (docker, python) routinely write progress to stderr, and PowerShell's
# Stop mode treats those as terminating errors. We use $LASTEXITCODE
# checks instead.

Set-Location $PSScriptRoot

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
    docker build -t scripture-book-builder . 2>&1 | Out-File -FilePath $dockerLog
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Docker build failed. Last 20 lines of ${dockerLog} :" -ForegroundColor Red
        Get-Content $dockerLog -Tail 20
        exit $LASTEXITCODE
    }
    Write-Host "    Docker image built."

    # Mount the dist/ directory as /output in the container.
    # Docker on Windows parses the Windows path (with drive-letter colon)
    # correctly because it splits on the rightmost colon.
    $hostDist = (Join-Path $PSScriptRoot "dist")
    docker run --rm -v "${hostDist}:/output" scripture-book-builder
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Docker run failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "==> Build complete. Artifacts in dist/:" -ForegroundColor Green
Get-ChildItem -Path (Join-Path $PSScriptRoot "dist\*") -Include manuscript.pdf, manuscript.html, beyond_the_prompt.epub -File -ErrorAction SilentlyContinue |
    Sort-Object Name |
    ForEach-Object {
        $size = "{0,7:N0} KB" -f ($_.Length / 1KB)
        Write-Host ("    {0,-32} {1}" -f $_.Name, $size)
    }
