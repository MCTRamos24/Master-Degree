# Visual QA report

Completed 4 October 2026. Page numbers below identify physical PDF pages, including the title and contents pages.

The burgundy/white academic identity, serif typography, content, equations, labels, and plot data were preserved. The final document remains 28 pages. Baseline and revised PDFs were compiled and rendered at 200 DPI; all baseline and revised pages were inspected individually, with contact sheets for sequence-level review. Following the last float correction, all pages were rendered again: pages 2, 11, and 12 changed and were re-inspected; the other 25 pages were pixel-identical to the fully inspected preceding revision.

## Pages changed

| PDF page | Original problem / effect | Modification and reason |
|---|---|---|
| 2 | Contents split left chapter material unevenly distributed. | End the first contents page at the chapter boundary; update page references after reflow. Clearer hierarchy without compressed spacing. |
| 3 | Second contents page inherited the uneven split. | Begin with Chapter 2; retain aligned page numbers and indentation. |
| 7 | Diagram green differed from the Key Concept palette. | Use the existing muted green consistently for a restrained semantic palette. |
| 8 | The acquisition table floated into the following recognition discussion. | Keep Table 1.5 at its source location; the recognition section starts on the next page with its paragraph together. |
| 9 | Verification/identification panel frames overlapped and had uneven widths. | Increase frame separation and standardize node widths; retain the complete comparison and attached caption. |
| 10 | Recognition content reflowed after the table/diagram fixes. | Recheck continuation, headings, and table spacing; accept coherent downstream flow. |
| 11 | Reflow risked stranding a benefits bullet before the modalities table. | Keep the modalities table before the benefits section; page now ends after the face discussion. |
| 12 | A floating modalities table interrupted the benefits list. | Anchor Table 1.7 at its source position; keep the benefits paragraph, complete list, remark, and summary in reading order. |
| 13 | Chapter heading left “Systems” on a separate line. | Keep “Biometric Systems” together while retaining the plain contents title. |
| 17 | Four isolated notation displays disconnected symbols from definitions. | Replace with a native notation/meaning table; FAR and FRR definitions now remain together. |
| 18 | Score-distribution diagram was conservative in size; annotation touched the threshold. | Enlarge vector axes and reposition the overlap label; surrounding formulas retain their association with prose. |
| 19 | FAR/FRR plot was small and annotations crossed curves. | Enlarge the diagram, move the FRR label, and give the EER label a white backing. Reflow keeps ROC/DET definitions with their takeaway. |
| 20 | ROC and DET plots underused the available page area. | Increase plot dimensions and DET tick type size; move the ROC reference-line label away from the diagonal. |
| 21 | A displayed rank symbol was detached from its definition. | Make the rank definition inline; keep explanation and formula together. |
| 22 | Rank-definition and example flow needed adjustment after resizing. | Accept the corrected prose flow; reserve sufficient space for the complete example on the following page. |
| 23 | CMC plot was small; example/next heading could split awkwardly. | Enlarge CMC and protect the example and subsequent section opening with `needspace`. |
| 25 | Running header changed to “References” before the bibliography began. | Clear the preceding page before resetting bibliography marks. |
| 26 | References were densely set in smaller type. | Use normal body type, hanging indentation, ragged-right entries, and increased inter-entry spacing; all 16 entries remain readable on one page. |
| 27 | Automatic columns split boxes and produced uneven vertical gaps. | Use two deliberate, equally sized, top-aligned columns; group Foundations/Matching and Verification/Identification. |
| 28 | Review continuation looked incidental, with cramped/split material. | Place terminology and modalities in matched columns, followed by the full-width formula sheet; improve the slash break in “histograms/distributions.” |

Pages 1, 4–6, 14–16, and 24 are visually unchanged. Their title composition, typography, tables, equations, boxes, and headers were inspected and retained.

## Figures/images changed

All modified diagrams are vector TikZ/PGFPlots, with embedded fonts. Dimensions below describe coordinate scales or plotting areas, rather than the entire caption/label bounding box.

| Visual | Before | After | Reason |
|---|---|---|---|
| Architecture / enrollment-recognition diagrams | Separate green stroke choice | Existing `KeyGreen` stroke | Consistent semantic color. |
| Verification vs identification | Panel spacing 2.65 cm; nodes minimum 2.25 cm | Spacing 3.25 cm; nodes minimum 2.8 cm, text width 2.6 cm | Eliminate frame overlap and align panel widths. |
| Genuine/impostor distributions | x scale 1.05 cm; y scale 4.2 cm | x 1.16 cm; y 4.6 cm | Approximately 10% larger axes; clearer overlap annotation. |
| FAR/FRR/EER | x scale 1.05 cm; y scale 4.1 cm | x 1.16 cm; y 4.5 cm | Approximately 10% larger axes; unobstructed labels. |
| ROC | x scale 7.2 cm; y scale 5.0 cm | x 9.4 cm; y 6.4 cm | Larger reading area and clearer diagonal annotation. |
| DET | 82% text width; height 6 cm; scriptsize ticks | 90% text width; height 7 cm; small ticks | Improve tick readability while preserving probit coordinates and percentage labels. |
| CMC | x scale 0.85 cm; y scale 5.0 cm | x 1.08 cm; y 5.5 cm | Improve rank/curve visibility and page balance. |
| Ground-truth notation | Four isolated display symbols | Full-width native two-column table | Keep symbols directly beside their definitions. |

Blue curves/fills now use one muted blue. Curves remain distinguished by labels, position, and line styling. Plot coordinates and mathematical relationships were retained: FAR decreases and FRR increases with similarity threshold; EER marks their crossing; ROC uses FAR/GAR; DET uses FAR/FRR on normal-deviate axes; CMC uses rank/cumulative match score. Schematic captions remain attached to figures. These illustrative curves are not empirical measurements.

## Images deliberately retained

`sapienza_logo.png` is the only raster asset embedded in the PDF (plus its alpha mask). It is 2720 × 1130 pixels, aspect ratio 2.407:1, displayed at approximately 8.424 × 3.500 cm: about 820 DPI in both directions. It remains losslessly compressed, sharp, transparent against white, and unstretched. Its symmetric transparent padding is intentional; the visible artwork is approximately 7.027 × 2.112 cm. No blur, compression artifacts, conflicting background, or unintended border was observed. The formal title-page scale and whitespace were retained.

## Images redrawn

None. Existing vector figures were refined directly; no slide screenshot or raster illustration was introduced. The notation presentation was rebuilt as a native LaTeX table.

## Validation

- Clean build in a fresh output directory: three successful pdfLaTeX passes, 28 A4 pages.
- Final-pass log: no warnings, overfull/underfull boxes, unresolved references, float warnings, destination warnings, or missing assets.
- All 72 original labels retained; no duplicate labels or unresolved source references.
- Extracted text bounding boxes remain within page boundaries. Visual review found no clipping, object overlaps, detached captions, stretched assets, or obvious layout regressions.
- Embedded Latin Modern/AMS font subsets; no Type 3 bitmap fonts. Apart from the logo, figures are vector artwork.
- Root and `out/` delivery PDFs are identical.
- Final page renders: `out/visual-qa/delivery/`; final overview: `Final_Contact_Sheet.png`. Baseline source, PDF, renders, and contact sheet remain under `out/visual-qa/` for comparison.

## Remaining issues

1. `LEZIONE0.pdf`, `LEZIONE1_Introduzione.pdf`, and `LEZIONE2_Indici_di_prestazione.pdf` were not available in the workspace or supplied attachments. Lecture visual classification and information-completeness comparison could not be performed. No missing slide information was inferred or invented.
2. Section 2.11.2 says detect-and-identify rate and false-alarm rate vary in “opposite directions,” then says raising a similarity threshold reduces both. The latter agrees with the stated acceptance rule; this academic wording requires review. It was retained as requested.
3. There is no standalone open-set ROC plot in the supplied notes; the topic is presented in prose. Without the lecture slides, its intended visual cannot be verified or reconstructed authoritatively.
