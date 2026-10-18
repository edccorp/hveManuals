# Stiffness Coefficient Dialog

**Exterior Stiffness**

The vehicle's structural properties are defined by its stiffness coefficients. HVE edits them for the front, back, sides, top or bottom of the vehicle from the Stiffness button of each Vehicle Dimensions (CG to ...) dialog: in 2-D mode a Stiffness Coefficients dialog (A, B and Kv), in 3-D mode the Vehicle Exterior Stiffness dialog, which adds the constant/linear/quadratic/cubic 3-D stiffness, saturation crush and maximum crush.

HVE 2027 edits the same coefficients in two places:

- **Vehicle › Editors › Crush Stiffness...** in the Vehicle editor (**Vehicle (F3)**) — the **Crush Stiffness** window, with every side and the 3-D stiffness in one window. They are the vehicle's own data, as in HVE.
- **Event › Crush Profile...** (EDCRASH, EDSMAC and EDSMAC4 events) — the **Crush & Geometry** window, whose **CG to Front...**, **CG to Rear...**, **CG to Left...** and **CG to Right...** buttons open one small dialog per side, titled **CG to Front Stiffness**, **CG to Rear Stiffness**, **CG to Left Stiffness** and **CG to Right Stiffness**; each holds that side's stiffness.

Both edit the same values for the selected vehicle, shown in the units set in Preferences.

!!! note "HVE 2027: Damage Profiles is not this"
    Until 2026-10-09 this window was **Event › Damage Profiles...**. In HVE that name is EDCRASH's *measured* damage — CDC, PDOF, crush depths — and **Event › Damage Profiles...** (Ctrl+M) now opens that, in Event Information's **Vehicle Impact Setup** section, for an EDCRASH event.

**Which engine reads what** — the window says this at the top of each part:

| Part | Read by |
|---|---|
| A and B (each side) | EDSMAC4 |
| Kv (each side) | EDSMAC; EDVSM, for the body against the ground |
| Distance | no engine — shown greyed |
| 3-D Node Stiffness (six zones) | SIMON (DyMESH) |

SIMON does not read A, B or Kv; EDCRASH reads none of this window (it takes A and B from the event's damage profile).

## Front, Rear, Left, Right

Each side (a collapsible section in Crush Stiffness, its own dialog from Crush & Geometry) has:

### Distance (CG to Front / Rear / Left / Right)
The distance from the CG to that face of the vehicle. It is stored with the case, but no engine reads it: they take the vehicle's exterior extents from the Vehicles panel (see [CG To Front](CGsToAll.md)). Crush Stiffness shows it greyed, *(not read by any engine)*.

### A Stiffness
Assigns the force per unit of damage width required to initiate permanent crush.

### B Stiffness
Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush.

### Kv Stiffness
Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush. This value differs from the B constant in that it assumes the force vs. deflection graph goes through zero. It is EDSMAC's crush spring, and EDVSM's for the body against the ground; EDSMAC4 uses A and B, and SIMON none of the three.

## From crash tests...

In the Crush Stiffness window only, below the four sides. It opens **Crush Stiffness from Crash Tests**, which works out CRASH3 A and B (and G, for reference) from one or more staged tests into a full-width rigid barrier, typed in or read from an NHTSA crash test file, and puts them on one side of this vehicle and, optionally, on this vehicle's EDCRASH events with damage on that side. See [Crush Stiffness from Crash Tests](../new-features/12-case-intake-and-vehicle-data.md#crush-stiffness-from-crash-tests).

!!! tip "New in HVE 2027"
    The **From crash tests...** calculation and its NHTSA test-file reader.

## 3-D Node Stiffness (SIMON / DyMESH)

In the Crush Stiffness window only, one collapsible section per zone: **Front**, **Right**, **Back**, **Left**, **Top** and **Undercarriage**. These are HVE's 3-D exterior stiffness: the contact pressure on each mesh node as a function of its crush depth, *const + linear·d + quad·d² + cubic·d³*. They are read by DyMESH only and are independent of the A/B/Kv values above. A zone whose four terms are all zero is labelled *(no resistance)*, with a warning that a DyMESH collision there passes straight through the bodywork.

### Constant, Linear, Quadratic, Cubic
The four terms of the pressure polynomial, in the units set in Preferences: HVE's own **lbf/in², lbf/in³, lbf/in^4 and lbf/in^5** in US units, **N/m², N/m³, N/m^4 and N/m^5** in metric. (They were shown in SI whatever Preferences said, until 2026-10-09.)

### Conversion Height
The conversion height HVE uses for the zone when relating its 2-D (A/B) stiffness to the 3-D form.

### Saturation Crush, Max Crush
Saturation Crush caps each node's crush depth in DyMESH; 0 means none. Max Crush is stored with the vehicle but no engine reads it, as in HVE's own source, and the dialog says so: it does not limit the crush.

!!! note "HVE 2027"
    HVE 2027 does not switch between a 2-D and a 3-D stiffness dialog: the A/B/Kv side values and the 3-D node stiffness are both shown in Crush Stiffness. The **Top** and **Bottom** faces have no A/B/Kv entry, only their 3-D node stiffness (Top and Undercarriage).

!!! warning "Not in HVE 2027"
    - HVE's **2-D/3-D Type** selection for the exterior stiffness. HVE 2027 carries both kinds at once.
    - The **Top** and **Bottom** faces' A, B and Kv. EDVSM reads a Kv for the roof and the undercarriage; this case model has none to give it.

<!-- NAV -->

---

← Previous: [Sprung Mass Dialog](SprungMassDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Drag Dialog](VehDragDlg.md) →

<!-- /NAV -->
