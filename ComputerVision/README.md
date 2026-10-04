# Computer Vision lecture notes

Build from PowerShell with `./build.ps1`, or use **Build LaTeX project** in
VS Code with LaTeX Workshop. The PDF is written to `out/ComputerVision.pdf`.
The script runs pdfLaTeX three times to resolve the contents and references.

On this computer, supplementary LaTeX packages are in
`%LOCALAPPDATA%/ComputerVision/texmf`. The build script searches that folder
directly because the existing MiKTeX package manager fails when writing its
package lock under Program Files. On another computer, install the packages
declared in `ComputerVision.tex` and their dependencies using its TeX distribution.

The lecture figures and native diagram sources are included in `cv_assets/`, extracted or reconstructed from the supplied
introduction, acquisition, and color lecture PDFs. See [figure sources](cv_assets/SOURCES.md) for
the source pages and extraction command. The Sapienza logo is included
as `sapienza_logo.png`, copied from the adjacent Biometric Systems notes.

Figures retain their aspect ratio and use individual dimensions appropriate to
their labels and content. Short chapters can share pages; lecture dividers remain
separate. The clickable two-page contents suppresses the long historical and
application section inventories while retaining their chapter links.

Run `python scripts/inspect_notes.py` after building to render every page at
110 dpi and generate a complete contact sheet plus four larger sheets under
`out/refinement/pages/`. The final PDF is also copied to `ComputerVision.pdf`.
The original source backup and refinement audit are under `out/refinement/`.
