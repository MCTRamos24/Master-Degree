# Figure sources

The ten introduction illustrations were extracted from the user-supplied lecture PDF
**Encrypt 1 - Introduction.pdf**, Computer Vision, instructor Marco Raoul Marini.
Page numbers below are the PDF's 1-based page numbers, not the slide footers.

| Asset | PDF pages | Extraction |
| --- | --- | --- |
| `computer_vision_eye.jpg` | 15 | Original embedded eye image, without the overlaid slide title |
| `visual_data_domains_tight.jpg` | 17 | Image collage and its category labels |
| `nuisance_parameters_tight.jpg` | 54 | Six illustrated variation categories with labels |
| `visual_cues_grid_tight.jpg` | 63, 64, 66, 67 | Four panels: perspective, aerial perspective, texture gradient, shading |
| `history_grid_tight.jpg` | 31, 34, 35, 36, 37, 38 | Six representative historical panels |
| `semantic_object_labels_tight.jpg` | 47 | Street scene with the original object-label overlays |
| `early_vision_grid_tight.jpg` | 78, 81, 82 | Filtering, texture classification, and shape from texture |
| `stereo_geometry_tight.jpg` | 101 | Stereo views and reconstruction diagrams |
| `recognition_examples_tight.jpg` | 91, 92 | Positive and negative person-detection examples |
| `applications_grid_tight.jpg` | 108, 112, 117, 121 | OCR, biometrics, intelligent vehicles, and medical imaging |

The source credits Steve Seitz on page 31, Rick Szeliski on pages 34–36,
J. Koenderink on page 67, AT&T Labs on page 108, and Grimson et al., MIT,
on page 121. These are lecture illustrations, not original artwork for these notes.
Labels on the assembled grids describe the corresponding source panels.

To reproduce the assets, run from the project directory:

```powershell
python scripts/extract_figures.py "C:/Users/Matt Ramos/Downloads/Encrypt 1 - Introduction.pdf"
```

Extraction uses Pillow and the `pdfimages`/`pdftoppm` programs available with
MiKTeX. The source PDF is only read. The extracted JPGs are included here, so
normal LaTeX builds do not need Python or access to the source PDF.

## Acquisition and color lectures

The following illustrations were extracted from the user-supplied PDFs
**Encrypt 2 - Aquisition.pdf** and **Encrypt 3 - Color.pdf**, by the same instructor.
Page numbers are 1-based PDF pages. Crops preserve the original illustration
and its labels; the quantization panels combine two consecutive slides.

| Asset | Lecture | PDF pages |
| --- | --- | --- |
| `quantization_levels.jpg` | Acquisition | 35, 36 |
| `spatial_resolution_effect.jpg` | Acquisition | 51 |
| `bicubic_vs_bilinear.jpg` | Acquisition | 85 |
| `source_spectra.jpg` | Color | 8 |
| `surface_reflectance_spectra.jpg` | Color | 9 |
| `cone_sensitivity.jpg` | Color | 14 |
| `metamer_spectra.jpg` | Color | 17 |
| `cie_xyz_chromaticity.jpg` | Color | 28 |
| `mcdam_ellipses.jpg` | Color | 29 |
| `hsv_model.jpg` | Color | 31 |
| `checker_shadow.jpg` | Color | 38 |
| `white_balance_example.jpg` | Color | 46 |
| `white_balance_mixed_illuminants.jpg` | Color | 48 |

The checker-shadow figure credits Edward H. Adelson; the white-balance slides
credit Cambridge in Colour. These are original lecture illustrations.

## Final refinement

The additional figures were verified against the same supplied lectures:

| Figure / asset | Lecture | PDF pages | Treatment |
| --- | --- | --- | --- |
| Computer-vision pipeline (inline TikZ) | Introduction | 40, 42 | Native reconstruction |
| Training/testing pattern recognition (inline TikZ) | Introduction | 41, 50 | Native reconstruction; SVM, GNB, neural networks retained in prose |
| `history_timeline.tex` | Introduction | 28–38 | Vector timeline; existing historical discussion retained |
| Acquisition chain (inline TikZ) | Acquisition | 2–25 | Native reconstruction connecting the source equations |
| `connectivity_paths.tex` | Acquisition | 63, 66 | Native reconstruction; written-rule/diagram inconsistency explicitly preserved |
| `triangle_geometry.tex` | Acquisition | 76 | Native reconstruction with opposite sub-triangle areas |
| `bilinear_geometry.tex` | Acquisition | 81 | Native reconstruction preserving corner, distance, and area ordering |
| `rod_cone_regimes.png` | Color | 13 | Full sensitivity-chart crop rendered at 2200-pixel slide width |
| Color-matching experiment (inline TikZ) | Color | 19 | Native conceptual reconstruction |
| `simultaneous_contrast_source.png` / `contrast_example.tex` | Color | 40 | Cropped original perceptual artwork |

Additional source checks: finite sampling comb (Acquisition 31–32), discrete
image domain/range (38), two-stage resizing (57), RGB wavelengths (Color 26),
HSV geometry (32, 35), and clockwise LBP ordering and bit pattern (62).

To reproduce these thirteen assets:

```powershell
python scripts/extract_remaining_figures.py "C:/Users/Matt Ramos/Downloads"
```
