# Output Settings (Tools › Output Settings...)

HVE Studio only. One window for the conventions your output is shown with, in
three tabs, with a **Preset** list at the top to switch between saved sets.

## Presets

A preset is a saved copy of all three tabs under a name. **Save as preset**
writes the current settings under the name typed beside it; choosing a name in
the list replaces the current settings with that preset's; **HVE defaults**
removes every change on all three tabs (your saved presets are kept).
**Delete preset** removes the chosen one, leaving the current settings as they
are.

Presets are folders under your settings (`presets\<name>\`, see [Where the
program keeps its settings](../getting-started/02-installing-and-running.md)),
each holding a copy of the three files the tabs edit. Zip a folder to hand a
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
