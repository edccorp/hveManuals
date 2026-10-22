# Stiffness Coefficient Dialog

**Exterior Stiffness**

The vehicle's structural properties are defined by its stiffness coefficients. HVE edits them for the front, back, sides, top or bottom of the vehicle from the Stiffness button of each Vehicle Dimensions (CG to ...) dialog: in 2-D mode a Stiffness Coefficients dialog (A, B and Kv), in 3-D mode the Vehicle Exterior Stiffness dialog, which adds the constant/linear/quadratic/cubic 3-D stiffness, saturation crush and maximum crush.

HVE Studio edits the same coefficients in **Vehicle › Editors › Crush Stiffness...** in the Vehicle editor (**Vehicle (F3)**): the **Crush Stiffness** window, with every face and both the 2-D and the 3-D stiffness in one table, shown in the units set in Preferences. The Vehicle Designer's **Stiffness** stage (step 4) hosts the same editor as its **Crush Stiffness** tab. They are the vehicle's own data, as in HVE, so no Event menu item edits them.

!!! note "HVE Studio: Damage Profiles is not this"
    Until 2026-10-09 this window was **Event › Damage Profiles...**. In HVE that name is EDCRASH's *measured* damage — CDC, PDOF, crush depths — and **Event › Damage Profiles...** (Ctrl+M) now opens that, in Event Information's **Vehicle Impact Setup** section, for an EDCRASH event.

## The stiffness table

One table with a column per face: **Front**, **Rear**, **Top**, **Bottom**, **Left** and **Right**. Its rows, top to bottom, are a **2-D** group and then a **3-D** group. A note above the table says which engine reads each group:

| Rows | Read by |
|---|---|
| 2-D: **A** and **B** | EDSMAC4 |
| 2-D: **Kv** | EDSMAC; EDVSM, for the body against the ground |
| 3-D: **Constant**, **Linear**, **Quadratic**, **Cubic**, **Conversion Height**, **Saturation Crush** | SIMON (DyMESH) only |
| 3-D: **Max Crush (graph extent)** | no engine (the graph's span) |

SIMON does not read A, B or Kv; EDCRASH reads none of this window (it takes A and B from the event's damage profile).

### 2-D: A, B, Kv
The **Top** and **Bottom** columns show "--" in these rows: the 2-D programs are planar.

- **A** — Assigns the force per unit of damage width required to initiate permanent crush.
- **B** — Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush.
- **Kv** — Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush. This value differs from the B constant in that it assumes the force vs. deflection graph goes through zero. It is EDSMAC's crush spring, and EDVSM's for the body against the ground; EDSMAC4 uses A and B, and SIMON none of the three.

### 3-D: Constant, Linear, Quadratic, Cubic
HVE's 3-D exterior stiffness: the contact pressure on each mesh node as a function of its crush depth C, *Const + Linear·C + Quad·C² + Cubic·C³*. They are read by DyMESH only and are independent of the 2-D values above. The columns map to DyMESH's zones: **Front** is the Front zone, **Rear** the Back, **Top** the Top, **Bottom** the Undercarriage, **Left** the Left and **Right** the Right. The four terms are in the units set in Preferences: HVE's own **lbf/in², lbf/in³, lbf/in^4 and lbf/in^5** in US units, **N/m², N/m³, N/m^4 and N/m^5** in metric. (They were shown in SI whatever Preferences said, until 2026-10-09.)

A face whose four terms are all zero has its **Constant** cell tinted red, and its tooltip warns that a node there meets no resistance: a DyMESH collision on that face passes straight through the bodywork.

### Conversion Height
The conversion height HVE uses for the zone when relating its 2-D (A/B) stiffness to the 3-D form.

### Saturation Crush, Max Crush (graph extent)
Saturation Crush caps each node's **force** in DyMESH: past it the pressure stays at its value there while the node keeps crushing (the deflection is not limited); 0 means none. **Max Crush (graph extent)** is recorded with the vehicle and sets how far the graph above the table runs, as it does in HVE's own dialog; no engine reads it, as in HVE's own source, and the note under the table says so: it does not limit the crush.

## The graph

Above the table is a graph of the **selected** column. Click a column header, or edit a cell, to select that column; the column is highlighted, and the editor opens on **Front** each time. **2-D (per unit width)** / **3-D (per unit area)** picks the graph:

- **2-D (per unit width)** — force per unit width against crush: *A + B C* (blue) and *Kv C* (red).
- **3-D (per unit area)** — the pressure *Const + Linear C + Quad C² + Cubic C³* against crush, flat beyond **Saturation Crush** (marked on the graph).

The **Top** and **Bottom** columns have only the 3-D graph.

!!! tip "New in HVE Studio"
    The graph of the selected face.

## From crash tests...

Under the table, in the Crush Stiffness editor only. It opens **Crush Stiffness from Crash Tests**, which works out CRASH3 A and B (and G, for reference) from one or more staged tests into a full-width rigid barrier, typed in or read from an NHTSA crash test file, and puts them on one side of this vehicle and, optionally, on this vehicle's EDCRASH events with damage on that side. See [Crush Stiffness from Crash Tests](../new-features/12-case-intake-and-vehicle-data.md#crush-stiffness-from-crash-tests).

!!! tip "New in HVE Studio"
    The **From crash tests...** calculation and its NHTSA test-file reader.

!!! note "HVE Studio"
    HVE Studio does not switch between a 2-D and a 3-D stiffness dialog: the 2-D (A/B/Kv) values and the 3-D node stiffness are both in the one table. The **Top** and **Bottom** faces have no 2-D entry, only their 3-D node stiffness.

    The per-face distance a case stores beside A, B and Kv is not shown: no engine reads it. The engines take the vehicle's exterior extents from the **CG to Front** ... **CG to Bottom** fields of the Vehicles panel's Size & Weight section (see [CG To Front](CGsToAll.md)).

!!! warning "Not in HVE Studio"
    - HVE's **2-D/3-D Type** selection for the exterior stiffness. HVE Studio carries both kinds at once.
    - The **Top** and **Bottom** faces' A, B and Kv. EDVSM reads a Kv for the roof and the undercarriage; this case model has none to give it.

<!-- NAV -->

---

← Previous: [Sprung Mass Dialog](SprungMassDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Drag Dialog](VehDragDlg.md) →

<!-- /NAV -->
