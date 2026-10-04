$ErrorActionPreference = 'Stop'
$dependencyRoot = Join-Path $env:LOCALAPPDATA 'ComputerVision/texmf'
$searchPaths = @{
    TEXINPUTS = 'tex'
    TFMFONTS = 'fonts/tfm'
    VFFONTS = 'fonts/vf'
    T1FONTS = 'fonts/type1'
    ENCFONTS = 'fonts/enc'
}
$savedEnvironment = @{}
Push-Location $PSScriptRoot
try {
    if (Test-Path -LiteralPath $dependencyRoot) {
        foreach ($name in $searchPaths.Keys) {
            $savedEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
            $path = (Join-Path $dependencyRoot $searchPaths[$name]).Replace('\', '/')
            [Environment]::SetEnvironmentVariable($name, "$path//;$($savedEnvironment[$name])", 'Process')
        }
    }
    New-Item -ItemType Directory -Path out -Force | Out-Null
    # Multiple passes resolve the table of contents and cross-references.
    foreach ($pass in 1..3) {
        & pdflatex --disable-installer -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -output-directory=out ComputerVision.tex
        if ($LASTEXITCODE -ne 0) {
            throw "LaTeX pass $pass failed. See out/ComputerVision.log."
        }
    }
    Copy-Item -LiteralPath 'out/ComputerVision.pdf' -Destination 'ComputerVision.pdf' -Force
    Write-Host 'Built ComputerVision.pdf and out/ComputerVision.pdf'
}
finally {
    foreach ($name in $savedEnvironment.Keys) {
        [Environment]::SetEnvironmentVariable($name, $savedEnvironment[$name], 'Process')
    }
    Pop-Location
}
