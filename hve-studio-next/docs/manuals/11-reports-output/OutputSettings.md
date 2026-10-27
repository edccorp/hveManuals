# Output Settings (Tools › Output Settings...)

HVE Studio only. One window for the conventions your output is shown with, in
four tabs, with a **Preset** list at the top to switch between saved sets.

## Presets

A preset is a saved copy of all four tabs under a name. **Save as preset**
writes the current settings under the name typed beside it; choosing a name in
the list replaces the current settings with that preset's; **HVE defaults**
removes every change on all four tabs (your saved presets are kept).
**Delete preset** removes the chosen one, leaving the current settings as they
are.

Presets are folders under your settings (`presets\<name>\`, see [Where the
program keeps its settings](../getting-started/02-installing-and-running.md)),
each holding a copy of the four files the tabs edit. Zip a folder to hand a
preset to a colleague; drop one into `presets\` and it appears in the list.
Nothing here is kept in the case: a colleague who opens your case sees their
own settings.

## Variables

Every output variable the picker offers, with the group it belongs to, its own
name, HVE's name for it and its display unit. Two things can be changed per
variable:

- **Label** — your name for it. The picker, the Key Results columns, the graph
  headers and the Key Results CSV header show the label; the variable's own
  name stays the key the program matches on, so a label never breaks anything.
- **Decimals** — how many decimal places Key Results prints a value with and
  its CSV writes. The default is 4. **Export Variables** is unaffected: an
  export is data and keeps every digit.

**Changed only** lists the variables you have edited (marked `*`); **Reset**
on a row and **Reset all variables** put HVE's name and the default back.

## Limits

The soft minimum and maximum each numeric field is held to in the dialogs, by
section. **Save to File** keeps them for the next session; a preset keeps them
too. This is the same editor as **Tools › Limits Editor...**, which now opens
this tab.

## Report Text

HVE's report wording, editable per string: see [Report Text](ReportText.md).
**Tools › Report Text...** opens this tab.

## Terms

Your own wording for the labels the windows draw: a field's name, a section's
heading, a tab, a button. The tab lists every label the windows have drawn since
the program started (open a window and its labels appear in the list), with a
**Shown as** column to type the wording into. The label's own text stays the
key, so a reworded field keeps its place in every list and every test, and the
physics, the case file and the reports never see the wording. Output variables
are not here: they have the **Variables** tab.

- **Changed only** lists the terms you have reworded (marked `*`); **Reset** on
  a row and **Reset all terms** put the original labels back.
- **Export terms...** writes the reworded terms to a JSON file (**Write**), to
  hand to a colleague or keep with a project; **Import terms...** reads one
  back (**Read**), adding its wordings to yours (a term in both takes the
  file's). A preset carries the terms too.
- **Import HVE language overrides...** reads an HVE installation's
  `sys\Language.rsc` together with the `language_overrides.rsc` its toolkit
  writes, and presses **Apply**. Every row the overrides reword is applied here:
  a row whose HVE default wording is also a label in this program takes the
  override's wording, and a variable row (`VehWheelSteerDelta` and its kind)
  sets that output variable's label on the Variables tab. A row that is
  unchanged, has no wording, or is not in `Language.rsc` is counted and left
  alone; the line under the buttons says how many of each.

What a renamed label is NOT: a physics variable. "Delta" in HVE's variable list
is the wheel's steer angle and "Gamma" its camber angle (both can be typed into
the Variable Selection filter to find them); rewording a label never changes
which quantity a field or a variable holds.
