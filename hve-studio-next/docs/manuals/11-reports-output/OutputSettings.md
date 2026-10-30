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

The ranges numeric fields are held to, by section, each in the units set in
Preferences. Every row has two ranges, as HVE's own fields do:

- **Usual min / Usual max** — a value outside this range is accepted, with a
  note beside the field or under the table asking you to check it (HVE's
  "out of usual range" warning).
- **Allowed min / Allowed max** — a value outside this range is not accepted:
  the field keeps its value and says why, and a pasted block holding one is not
  pasted. **none** means nothing is refused on that side; click it to set a
  limit, and **x** beside a limit removes it.

The rows with both ranges start at HVE's own values (HVE's `Language.rsc`):
the initial speed (usual up to 200 mph, allowed up to 400 mph; a run whose
vehicle starts past the allowed limit is not run), the steering-wheel angle
(±900° / ±3600°), the steer angle at the tires (±45° / ±90°), the brake pedal
force (400 lb / 1000 lb), a wheel brake or traction force (10,000 lb /
100,000 lb) and the 0–1 throttle, brake and friction fractions. Times and
positions have no limit. The older rows (tire, suspension, brake assembly,
steering) carry a usual range their fields are held to when dragged.

A changed row is marked `*` and has a **Reset** to HVE's value; **Reset
Defaults** puts every row back. **Save to File** keeps them for the next
session; a preset keeps them too.

**Right-click a limited value** — a cell of a driver-control table, an initial
speed, or the name of a tire, suspension, brake or steering field — and choose
**Edit limits...** to open this tab with that row found and marked. The same
menu's **Rename this label...** opens the Terms tab with the label found. This
is the same editor as **Tools › Limits Editor...**, which opens this tab.

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

A wording is shown wherever that label is drawn -- every window, menu, tab and
table header that shows the same text, not only the one it was typed for. It
is kept over the language chosen in **Tools › Preferences... › Language**, so
a pack never undoes a wording you set by hand.

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
