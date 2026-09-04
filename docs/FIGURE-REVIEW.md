# HVE User's Manual — figure image review

Status of the updated figure images supplied in `Chapter_13.zip` and
`Overview.zip` against the figure references in `docs/manuals/hve-users/`.

276 references were updated automatically by exact figure-number match. The
items below were not, and need a decision.

## 1. Caption does not describe the new image

Every one of the 268 replaced figures was checked by reading the window title
out of the screenshot and comparing it with the caption. Two kinds of claim can
be checked this way:

- a caption naming a dialog, against that dialog's own title bar (57 figures);
- a caption naming a physics program, tutorial or case file, against the case
  named in the HVE title bar (4 figures).

The remaining figures are main-window screenshots whose title bar carries only
the case file name, so a caption like "HVE Human Editor" cannot be confirmed or
contradicted from the title bar alone.

**One genuine mismatch:**

| Figure | Caption says | Screenshot title bar |
|---|---|---|
| Figure 12-1 | "the Blind Intersection environment model used in the **EDSMAC4 Tutorial**" | `HVE 2016 - EDCRASH Tutorial, Visibility Study (EdcrashTutorialEDC.hve)` |

Either the caption or the screenshot needs changing.

Three further figures looked like mismatches but are not — the caption uses the
manual's wording for a dialog while the window title uses the application's:

| Figure | Caption | Window title |
|---|---|---|
| Figure 4-18 | "Vehicle Damage Profile dialog" | `Damage Data: Acura 3.2TL 4-Dr` |
| Figure 4-41 | "Vehicle Accelerometers dialog" | `Accelerometer Data: Freightliner Colum…` |
| Figure 11-13 | "Airbag Restraints dialog" | `Air Bag: Tutorial Buick Skylark` |

Worth knowing that the manual and the application disagree on these names, but
the screenshots are correct.

## 2. One figure supplied as several sub-figures

The manual has a single figure where the new set has lettered parts. Adding
them means editing the surrounding text and writing a caption for each part.

| Manual figure | Supplied as | In |
|---|---|---|
| Figure 2-15 | Figure 2-15a, Figure 2-15b | `01-overview/02-how-to-use-hve.md` |
| Figure 2-18 | Figure 2-18a, Figure 2-18b | `01-overview/02-how-to-use-hve.md` |
| Figure 2-37 | Figure 2-37a, Figure 2-37b | `01-overview/02b-how-to-use-hve.md` |
| Figure 2-5 | Figure 2-5a, Figure 2-5b, Figure 2-5c | `01-overview/02-how-to-use-hve.md` |
| Figure 4-14 | Figure 4-14a | `02-menu-reference/04a-setup-menu.md` |
| Figure 4-15 | Figure 4-15a, Figure 4-15b, Figure 4-15c | `02-menu-reference/04a-setup-menu.md` |
| Figure 4-22 | Figure 4-22a, Figure 4-22b | `02-menu-reference/04b-setup-menu.md` |
| Figure 4-27 | Figure 4-27a, Figure 4-27b | `02-menu-reference/04b-setup-menu.md` |
| Figure 6-2 | Figure 6-2a, Figure 6-2b | `02-menu-reference/06-options-menu.md` |
| Figure 11-15 | Figure 11-15a, Figure 11-15b | `04-vehicle-editor/11a-sprung-mass.md` |
| Figure 11-20 | Figure 11-20a, Figure 11-20b | `04-vehicle-editor/11b-exterior.md` |
| Figure 12-2 | Figure 12-2a, Figure 12-2b, Figure 12-2c, Figure 12-2d | `05-environment-editor/12-creating-editing-environments.md` |
| Figure 17-3 | Figure 17-3a, Figure 17-3b | `07-playback-editor/17-report-playback-windows.md` |
| Figure 19-6 | Figure 19-6a, Figure 19-6b | `08-3d-editor/19-using-3d-editor.md` |

## 3. Supplied images the manual never references

69 images whose figure number appears nowhere in the manual. Either the
manual is missing figures it should have, or these are extras. Chapter 32 (the
HVE Tutorial) accounts for more than half.

| Chapter | Count | Figures |
|---|---|---|
| 10 | 1 | 10-3 |
| 11 | 2 | 11-2a, 11-2b |
| 17 | 6 | 17-1, 17-2, 17-4, 17-5, 17-8, 17-9 |
| 18 | 2 | 18-1, 18-4 |
| 19 | 3 | 19-1, 19-2, 19-5 |
| 20 | 2 | 20-1, 20-4 |
| 23 | 11 | 23-1, 23-5, 23-9, 23-1a, 23-1b, 23-1c, 23-32, 23-3a, 23-3b, 23-10a, 23-10b |
| 27 | 2 | 27-1, 27-3 |
| 29 | 1 | 29-1 |
| 31 | 3 | 31-3, 31-8, 31-9 |
| 32 | 36 | 32-2, 32-5, 32-7, 32-8, 32-9, 32-10, 32-11, 32-12, 32-13, 32-14, 32-15, 32-21, 32-22, 32-23, 32-24, 32-25, 32-26, 32-27, 32-28, 32-30, 32-31, 32-32, 32-33, 32-34, 32-35, 32-36, 32-37, 32-38, 32-39, 32-41, 32-42, 32-43, 32-44, 32-46, 32-47, 32-48 |

## 4. Figures still using the legacy image

60 figures had no replacement supplied and still use the image extracted
from the printed manual. These will look softer than the ones around them.

| Chapter | Count | Figures |
|---|---|---|
| 2 | 3 | 2-31, 2-42, 2-78 |
| 4 | 12 | 4-1, 4-19, 4-20, 4-21, 4-28, 4-29, 4-30, 4-31, 4-36, 4-37, 4-38, 4-39 |
| 5 | 1 | 5-3 |
| 6 | 1 | 6-18 |
| 7 | 2 | 7-1, 7-2 |
| 9 | 4 | 9-3, 9-6, 9-7, 9-11 |
| 11 | 13 | 11-9, 11-11, 11-14, 11-16, 11-21, 11-24, 11-25, 11-28, 11-30, 11-37, 11-38, 11-41, 11-47 |
| 12 | 1 | 12-3 |
| 13 | 3 | 13-1, 13-6, 13-7 |
| 15 | 1 | 15-4 |
| 16 | 5 | 16-1, 16-2, 16-4, 16-5, 16-6 |
| 20 | 2 | 20-5, 20-16 |
| 29 | 6 | 29-4, 29-5, 29-6, 29-7, 29-8, 29-9 |
| 30 | 1 | 30-1 |
| 31 | 5 | 31-1, 31-4, 31-5, 31-6, 31-7 |

