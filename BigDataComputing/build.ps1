$ErrorActionPreference = 'Stop'
$previousTexInputs = $env:TEXINPUTS
$fontVariables = @('TFMFONTS', 'VFFONTS', 'T1FONTS', 'ENCFONTS')
$previousFontPaths = @{}
foreach ($name in $fontVariables) {
    $previousFontPaths[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
}
Push-Location $PSScriptRoot
try {
    if (Test-Path -LiteralPath 'out/texmf/texmf/tex') {
        $env:TEXINPUTS = ".;out/texmf/texmf/tex//;$previousTexInputs;"
    }
    New-Item -ItemType Directory -Path 'out' -Force | Out-Null
    $texSource = 'BigDataComputing.tex'
    if (Test-Path -LiteralPath 'out/texmf/newtx/map/newtx.map') {
        $env:TEXINPUTS = "out/texmf/newtx//;$env:TEXINPUTS"
        foreach ($name in $fontVariables) {
            [Environment]::SetEnvironmentVariable($name, "out/texmf//;$($previousFontPaths[$name]);", 'Process')
        }
        $texSource = '\pdfmapfile{+out/texmf/newtx/map/newtx.map}\input{BigDataComputing.tex}'
        if (Test-Path -LiteralPath 'out/texmf/texmf/fonts/map/dvips/tex-gyre/qtm.map') {
            $texSource = '\pdfmapfile{+out/texmf/texmf/fonts/map/dvips/tex-gyre/qtm.map}' + $texSource
        }
        if (Test-Path -LiteralPath 'out/texmf/texmf/fonts/map/dvips/txfonts/txfonts.map') {
            $texSource = '\pdfmapfile{+out/texmf/texmf/fonts/map/dvips/txfonts/txfonts.map}' + $texSource
        }
    }
    for ($pass = 1; $pass -le 3; $pass++) {
        & pdflatex --disable-installer -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=out $texSource
        if ($LASTEXITCODE -ne 0) {
            throw 'LaTeX compilation failed. See out/BigDataComputing.log.'
        }
    }
}
finally {
    $env:TEXINPUTS = $previousTexInputs
    foreach ($name in $fontVariables) {
        [Environment]::SetEnvironmentVariable($name, $previousFontPaths[$name], 'Process')
    }
    Pop-Location
}
