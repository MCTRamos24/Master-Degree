This project contains LaTeX lecture notes for Automatic Verification of Intelligent Systems. Keep `assets/sapienza-logo.png` with the source; it supplies the cover logo. All other diagrams use native TikZ.

The logo comes from [Sapienza's official logo download](https://www.uniroma1.it/it/pagina/impaginazione-della-tesi-e-logo).

Build with an installed MiKTeX or TeX Live distribution:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
```

The PDF is written to `out/AumaticVerificationOfIntelligentSystems.pdf`. The script runs pdfLaTeX until the contents and cross-references stabilize, and stops on compilation errors or unresolved references.

With MiKTeX, missing packages are installed into the project-local `.miktex` directory. This avoids the current installation's attempt to write packages into `C:\Program Files\MiKTeX`. The first build may need Internet access. Keep `.miktex` available for later builds.
