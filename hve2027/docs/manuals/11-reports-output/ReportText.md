# Report Text (Tools › Report Text...)

HVE 2027 only; classic HVE has no such window. Since 2026-10-16 it is the
Report Text tab of [Output Settings](OutputSettings.md), whose presets carry
these changes along with the variable labels and the limits.

Every physics program (EDCRASH, SIMON, EDSMAC4, ...) lays out its report pages
(**Output › HVE Reports**) from a set of strings: the headings, the column
labels, the sentences. Classic HVE kept them in a file beside each program
(`EDCRASH.rsc`, `SIMON.rsc`, ...). In HVE 2027 they are built into the program,
and this window lets you change any of them.

## What you can change

Choose the **Program**, then a string on the left (the filter box searches names
and text; **Changed only** lists the ones you have edited, marked `*`). The
right side shows HVE's own text and, under it, **Your text**. **Apply** saves
your wording; every report run from then on uses it. **Reset to HVE's** removes
your wording for that string; **Reset all programs** removes every change.

Your changes are yours alone: they are kept in `hve_report_text.json` with your
other settings (see [Where the program keeps its
settings](../getting-started/02-installing-and-running.md)), not in the case. A
colleague who opens the same case sees HVE's text, and so does an older program.

## Placeholders

Many strings carry `%s`, `%d`, `%5.2f` and the like. The program fills those in
when it writes the page: a unit, a count, a value. Your text must keep **the same
placeholders in the same order**; the window will not apply a text whose
placeholders differ, and tells you which ones. A width or precision may change
(`%5.2f` to `%.1f`); `%%` is a percent sign, not a placeholder. A `\n` in the
text is a line break, written exactly as in HVE's file.

A string that reaches the page but cannot be applied (the file was edited by
hand, say) is noted in the run status: "report text: N override(s) ... not
applied", naming the first.

## For a whole edited set

To replace a program's entire string file rather than single strings, point
the environment variable `HVE_REPORT_RSC_DIR` at a folder holding your own
`<PROGRAM>.rsc`; a program whose file is in that folder reads it instead of the
built-in text, and the others keep theirs. The Report Text window edits on top
of whichever text is in use.
