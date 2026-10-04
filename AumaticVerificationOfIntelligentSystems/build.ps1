$ErrorActionPreference = 'Stop'

$source = 'AumaticVerificationOfIntelligentSystems.tex'
$job = [System.IO.Path]::GetFileNameWithoutExtension($source)
$previousInstall = $env:MIKTEX_USERINSTALL

Push-Location $PSScriptRoot
try {
    $compiler = Get-Command pdflatex -ErrorAction Stop
    New-Item -ItemType Directory -Force -Path 'out' | Out-Null

    # Keep missing MiKTeX packages out of the protected system installation.
    $isMiKTeX = (& $compiler.Source --version | Out-String) -match 'MiKTeX'
    $compilerOptions = @()
    if ($isMiKTeX) {
        $env:MIKTEX_USERINSTALL = Join-Path $PSScriptRoot '.miktex'
        New-Item -ItemType Directory -Force -Path $env:MIKTEX_USERINSTALL | Out-Null
        $compilerOptions += '-enable-installer'
    }

    $previousState = $null
    $converged = $false
    for ($pass = 1; $pass -le 5; $pass++) {
        Write-Host "Building PDF (pass $pass)..."
        & $compiler.Source @compilerOptions '-interaction=nonstopmode' '-halt-on-error' '-file-line-error' '-output-directory=out' $source
        if ($LASTEXITCODE -ne 0) {
            throw "pdfLaTeX failed. See out/$job.log."
        }

        $state = (@('aux', 'toc', 'out') | ForEach-Object {
            $path = Join-Path 'out' "$job.$_"
            if (Test-Path -LiteralPath $path) {
                (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
            }
        }) -join ':'
        if ($pass -ge 2 -and $state -eq $previousState) {
            $converged = $true
            break
        }
        $previousState = $state
    }
    if (-not $converged) {
        throw 'Cross-references did not converge after five passes.'
    }
    $log = Get-Content -LiteralPath "out/$job.log" -Raw
    if ($log -match 'There were undefined references|Rerun to get|Label\(s\) may have changed') {
        throw "Unresolved references remain. See out/$job.log."
    }
    Write-Host "Built out/$job.pdf"
}
finally {
    $env:MIKTEX_USERINSTALL = $previousInstall
    Pop-Location
}
