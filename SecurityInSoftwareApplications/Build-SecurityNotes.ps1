$ErrorActionPreference = 'Stop'
$ssaProjectRoot = $PSScriptRoot
$ssaBuildDirectory = Join-Path $ssaProjectRoot 'tmp\latex'
New-Item -ItemType Directory -Path $ssaBuildDirectory -Force | Out-Null
$ssaCompiler = (Get-Command pdflatex -ErrorAction Stop).Source
Push-Location -LiteralPath $ssaBuildDirectory
try {
    for ($ssaPass = 1; $ssaPass -le 3; $ssaPass++) {
        $ssaPassOutput = Join-Path $ssaBuildDirectory "pass-$ssaPass.txt"
        & $ssaCompiler --disable-installer -interaction=nonstopmode -halt-on-error -file-line-error "-output-directory=$ssaBuildDirectory" (Join-Path $ssaProjectRoot 'SecurityInSoftwareApplications.tex') > $ssaPassOutput 2>&1
        if ($LASTEXITCODE -ne 0) {
            Get-Content -LiteralPath $ssaPassOutput -Tail 40
            throw "LaTeX pass $ssaPass failed; see $ssaPassOutput"
        }
    }
    $ssaLog = Join-Path $ssaBuildDirectory 'SecurityInSoftwareApplications.log'
    $ssaUnresolved = Select-String -LiteralPath $ssaLog -Pattern 'There were undefined references|multiply defined|Overfull \\[hv]box'
    if ($ssaUnresolved) {
        $ssaUnresolved | ForEach-Object { Write-Warning $_.Line }
    }
    Copy-Item -LiteralPath (Join-Path $ssaBuildDirectory 'SecurityInSoftwareApplications.pdf') -Destination (Join-Path $ssaProjectRoot 'SecurityInSoftwareApplications.pdf') -Force
    Write-Output 'Built SecurityInSoftwareApplications.pdf successfully (three passes).'
}
finally {
    Pop-Location
}
