# Building the lecture notes

In VS Code with LaTeX Workshop, open `SecurityInSoftwareApplications.tex` and
run **Build LaTeX project**. The workspace recipe runs `build.ps1`.

From PowerShell in this folder:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
```

The PDF is written to `out/SecurityInSoftwareApplications.pdf`. The script
runs pdfLaTeX three times to resolve the table of contents and references.

Keep `out/texmf`: it contains the local packages needed by this installation.
The build adds them to `TEXINPUTS` for its process only. Packages were obtained
from CTAN's MiKTeX repository, with tcolorbox pinned to upstream v6.6.0 for
compatibility with the installed LaTeX 2025-06-01 kernel:
https://github.com/T-F-S/tcolorbox/releases/tag/v6.6.0.
Downloaded source archives are retained in `out/packages`.
The local packages include `colortbl`, required for coloured table headers.

The title page uses `sapienza_logo.png` in the project folder. LaTeX trims
the image's blank margins without changing the original PNG.
The four remaining figures are also included in the project folder:
`slammer_initial.jpg`, `slammer_spread.jpg`, `zerodium_desktop.png`, and
`zerodium_mobile.png`. These were recovered from pages 10--11 of the existing
`SecurityInSoftwareApplications_Complete_Corrected.pdf` in Downloads. Keep all
five image files alongside the `.tex` source; missing images now produce a build
error instead of being silently replaced by placeholders.

The installed MiKTeX package manager fails to acquire its package database
lock under `Program Files`; this build uses local packages and disables
automatic installation. The original global MiKTeX configuration was restored.
