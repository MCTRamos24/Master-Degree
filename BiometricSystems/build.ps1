$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
$previousTexInputs = $env:TEXINPUTS
try {
    New-Item -ItemType Directory -Force out/texmf | Out-Null
    $localTex = (Join-Path $PSScriptRoot 'out/texmf/texmf/tex').Replace('\', '/')
    $env:TEXINPUTS = "$localTex//;" + $previousTexInputs

    function Get-TexPackage([string]$package) {
        Write-Host "Downloading local LaTeX dependency: $package"
        $archive = "out/$package.tar.lzma"
        & curl.exe -fsSL --max-time 60 "https://mirrors.ctan.org/systems/win32/miktex/tm/packages/$package.tar.lzma" -o $archive
        if ($LASTEXITCODE -ne 0) { throw "Download failed: $package" }
        & tar.exe -xf $archive -C out/texmf
        if ($LASTEXITCODE -ne 0) { throw "Extraction failed: $package" }
    }

    foreach ($package in @('geometry', 'colortbl', 'fancyhdr', 'booktabs')) {
        if (-not (Test-Path "out/$package.tar.lzma")) { Get-TexPackage $package }
    }

    $downloaded = @{}
    $successfulPasses = 0
    for ($attempt = 0; $attempt -lt 40; $attempt++) {
        & pdflatex -disable-installer -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=out BiometricSystems.tex > out/build-output.txt
        if ($LASTEXITCODE -eq 0) {
            $successfulPasses++
            if ($successfulPasses -eq 3) {
                Write-Host 'Build complete: out/BiometricSystems.pdf'
                return
            }
            continue
        }
        $log = Get-Content out/BiometricSystems.log -Raw
        $missing = [regex]::Match($log, "File ``([^']+)\.sty' not found")
        if (-not $missing.Success) {
            Get-Content out/build-output.txt -Tail 30
            throw 'LaTeX compilation failed; inspect out/BiometricSystems.log.'
        }
        $package = $missing.Groups[1].Value
        if ($package.StartsWith('tikzfill.')) { $package = 'tikzfill' }
        if ($downloaded.ContainsKey($package)) { throw "Still missing package: $package" }
        Get-TexPackage $package
        $downloaded[$package] = $true
        $successfulPasses = 0
    }
    throw 'Compilation did not converge.'
} finally {
    $env:TEXINPUTS = $previousTexInputs
    Pop-Location
}
