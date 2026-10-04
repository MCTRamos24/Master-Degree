$ErrorActionPreference = 'Stop'
$previousUserInstall = $env:MIKTEX_USERINSTALL
Push-Location $PSScriptRoot
try {
    # Keep MiKTeX packages in the user directory, even if its startup config
    # incorrectly points UserInstall at Program Files.
    $env:MIKTEX_USERINSTALL = Join-Path $env:APPDATA 'MiKTeX'
    for ($pass = 1; $pass -le 3; $pass++) {
        & pdflatex -enable-installer -interaction=nonstopmode -halt-on-error -file-line-error FoundationsOfDataScience.tex
        if ($LASTEXITCODE -ne 0) {
            throw "LaTeX pass $pass failed. See FoundationsOfDataScience.log."
        }
    }
} finally {
    $env:MIKTEX_USERINSTALL = $previousUserInstall
    Pop-Location
}
