$ErrorActionPreference = 'Stop'
$previousTexInputs = $env:TEXINPUTS
Push-Location $PSScriptRoot
try {
    # Use project-local packages compatible with the installed MiKTeX engine.
    # The trailing separator preserves MiKTeX's standard package search paths.
    $packagePath = Join-Path $PSScriptRoot 'out/texmf/texmf/tex'
    $env:TEXINPUTS = $packagePath.Replace('\', '/') + '//;' + $previousTexInputs
    New-Item -ItemType Directory -Force -Path 'out' | Out-Null
    for ($pass = 1; $pass -le 3; $pass++) {
        & pdflatex -disable-installer -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -output-directory=out SecurityInSoftwareApplications.tex
        if ($LASTEXITCODE -ne 0) {
            throw "LaTeX build failed on pass $pass. See out/SecurityInSoftwareApplications.log."
        }
    }
    Write-Host 'Built out/SecurityInSoftwareApplications.pdf'
}
finally {
    $env:TEXINPUTS = $previousTexInputs
    Pop-Location
}
