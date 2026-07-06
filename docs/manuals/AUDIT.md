# HVE Manual — Code-Verification Audit

This records the dedicated, independent code-verification pass performed on the
Markdown manual set (all ~290 content pages) **after** initial authoring. Every
page was re-read against the current source and its findings applied. The pass
ran in three waves; all confirmed findings have been fixed in the pages
themselves.

## Result at a glance

| Wave | Scope | Pages | CRITICAL | MAJOR | MINOR |
| --- | --- | --- | --- | --- | --- |
| 1 | Dialog reference + calculation options | 126 | 2 | ~10 | ~40 |
| 2 | Program manuals (EDCRASH … DyMESH) | 14 manuals | 11 | 8 | ~19 |
| 3 | HVE User's Manual sections | 11 sections | 1 | ~11 | ~9 |

Roughly 60% of pages were fully accurate as authored; the rest had at least one
correction. **No CRITICAL issues were found in the physics calculation-options
pages** (variable names, defaults, and rejected-option handling all verified).

## The dominant pattern

**Nearly every CRITICAL/MAJOR technical error was a calculation-method equation
in a program manual that had been faithfully transcribed from EDC's original
PDF — but the PDF itself is stale relative to the current engine.** These are
*code-vs-paper divergences*, not transcription slips: the Markdown copied the
paper correctly; the code has since changed. The pages now match the code
(authoritative for current software behavior).

Confirmed code-vs-paper divergences (PDF and old doc agreed; code differs):

- **EDVDS** — linear-tire slip limit is `0.25` (25% / 0.25 rad), fixed; PDF says
  "10% / 0.10 rad (editable)".
- **SIMON** — Eq. 95 tire parameter `a`, Eq. 98 quadratic-root sign, Eq. 114
  rolling-resistance sign + `RrMult`, Eq. 117 connection stiffness (`max`/Use
  Heavier default, not `min`). The PDF's Eq. 98 is algebraically wrong.
- **EDSVS / EDVTS** — shared Fiala tire model: μp modifier uses `|α|` not
  `|sin α|`; μx divides by `(1+IsDual)`; EDVTS cubic term `ᾱ³/27` not `3ᾱ/27`;
  saturation test on `|ᾱ|`.
- **EDVSM** — steer-axis tire moment subtracts the `F_x` term and uses raw
  camber `γ` (not `sin γ`).
- **EDCRASH** — collinear classification also covers near-head-on (≥170°) and
  fixed-barrier impacts; PDOF split-adjustment uses the user-editable PDOF Range
  (default 10°), not a hardcoded 15° (the PDF is internally inconsistent here).
- **GATB** — hard-coded ATB integration step is `0.002` s (the `0.0005` value is
  an A4-card control field).

Transcription slips (paper and code agreed; Markdown mis-typed): EDSVS/EDVTS yaw
dot notation (`ṙ` not `r̈`) and `sign(ᾱ)`.

## Two genuinely wrong pages (now rewritten)

- **`08-environment/EnvtInfoDlg.md`** — documented a dead dialog class
  (`CEnInfoDlg`); the app runs `CEnvInfoDlg`, a tabbed property sheet. Rewritten.
- **`08-environment/BoxEdDlg.md`** — did not mention that Apply forces box
  height to the Length value. Documented.

## Recurring smaller categories

- Controls present in the `.rc` but **hidden/disabled at runtime** documented as
  live: Render "Show As" / "Light Sources On" / "Texture Quality" / "Complexity",
  Camera "Rename View", GEBOD "User-defined" subject, EDSVS/EDVTS calculation-
  options dialog (`CalcOptionsDlgIsUsed = FALSE`).
- **Unit labels** resolved by type from `units.custom`/`units.us`, overriding the
  literal token in `Language.rsc` (e.g. `lb/ft-lb`, `ft-lb`).
- **Runtime labels** from `Language.rsc` overriding `.rc` design-time captions.
- **Table-size limits** drifted (slip/rolloff 6 not 10; engine power curve 15 not
  10; MAXTIRETABLE 3).

## Code issues surfaced for EDC (not doc problems)

These are defects/artifacts in the application or engine source, documented in
the manuals as actual behavior but worth fixing at the source:

1. `BoxEditorDlg.cpp:586` — box **height is forced to the Length field value**;
   the Height field is never applied.
2. `AeroDynamicDragDlg.cpp` — "Device Installed" unchecked leaves the Projected
   Surface Area edit and CoP-Z label enabled (the 7th control pair is skipped).
3. `EDVDS.rsc` Msg11 — text says "automatically calculated **by EDSMAC4**"
   (copy-paste artifact in an EDVDS message).
4. `EDVTS.rsc` — Msg2 says "EDSVS", Msg7 says "EDSMAC4" (resource-template
   leftovers).
5. `SIMON Tire.cpp:717` — in-code comment claims two quadratic-root forms are
   equal; they are algebraically different (the code expression is the correct
   one).
6. **The published EDC PDF manuals contain outdated/incorrect physics equations**
   (see the code-vs-paper list above) — the definitive fix is to update those
   source documents.

## Method

Each page was audited by an agent that located the corresponding dialog class,
resource block (`HVERSNT.rc`), runtime strings (`Language.rsc`), unit tables
(`units.custom`/`units.us`), and physics source (`Physics/Source`,
`Physics/Include`), then reported discrepancies with code citations. Fixes were
applied by separate agents that re-verified each finding against the cited
source before editing. Program-manual equation fixes additionally cross-checked
the original PDF to classify each as transcription-slip vs code-vs-paper.
