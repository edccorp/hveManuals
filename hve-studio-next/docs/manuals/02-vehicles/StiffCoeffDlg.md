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
| 3-D: **Constant**, **Linear**, **Quadratic**, **Cubic**, **Saturation Crush** | SIMON (DyMESH) only |
| 3-D: **Elastic Stiffness** | SIMON (DyMESH) |
| 3-D: **Structure Restitution**, **Bumper b0**, **Bumper Restitution** (the bumper rows Front and Rear only) | SIMON (DyMESH) law 2 only: applied when the solver runs with `HVE_DYMESH_LAW=2` |


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
Not in the table: it is under it, beside **Calculate 3-D from 2-D**, one field each for **Front**, **Rear**, **Left** and **Right** (the faces with 2-D values). It is the height HVE uses for the zone when relating its 2-D (A/B) stiffness to the 3-D form: 30 in (0.762 m) unless the face states another. **Calculate 3-D from 2-D** divides A and B by it; it is not a stiffness, and no engine computes with it (SIMON prints it in its input report).

## Calculate 3-D from 2-D

Under the table, in the **3-D from 2-D** section with each face's **Conversion Height**. It sets the **Front**, **Rear**, **Left** and **Right** columns' 3-D terms from their 2-D ones over each column's Conversion Height: **Constant** = A / height, **Linear** = B / height, **Quadratic** and **Cubic** zero (A in lbf/in over inches gives lbf/in², B in lbf/in² gives lbf/in³). That is HVE's own conversion, the one it applies to a vehicle that states no 3-D values. It replaces those four columns' 3-D values; **Top** and **Bottom** keep what they hold. The button is disabled while a run's results hold this vehicle, as the other edits are.

**Top and Bottom always have values.** They have no 2-D data (the 2-D programs are planar), so a vehicle that states none left them all-zero, and anything landing on a roof or a floor met no resistance. When the editor opens on a vehicle whose Top or Bottom 3-D terms are all zero, they are filled with the mean of the Left and Right columns (from their A and B over the height, or from their 3-D terms where those are stated), and a note says so. A face that already holds a law is never changed.

### Saturation Crush
Saturation Crush caps each node's **force** in DyMESH: past it the pressure stays at its value there while the node keeps crushing (the deflection is not limited); 0 means none. The graph above the table runs a tenth past it, or 60 in where there is none.

HVE's dialog also has a **Max Crush**, which only sets how far its graph runs; no engine reads it, in HVE's source or here, and it does not limit the crush. It is not in this editor: an imported vehicle's or an older case's Max Crush is read and dropped.

### Elastic Stiffness
The structure's elastic slope, in the units of **Linear**. HVE calls it **Unloading Stiffness**.

- **Under DyMESH law 2** (the solver run with `HVE_DYMESH_LAW=2`) it is the slope a node LOADS along until its pressure reaches **Constant**, the yield pressure (at a crush of Constant / Elastic Stiffness), and the distance it springs back when it unloads: peak pressure / Elastic Stiffness. It keeps the rest as permanent crush. How much energy comes back over that spring-back is **Structure Restitution**'s. A face that states an Elastic Stiffness runs law 2; a face that states 0 runs HVE's law.
- **Under HVE's law** it is only the slope a node unloads along from its peak: it springs back peak pressure / Elastic Stiffness and keeps the rest. 0 means derive the slope from the event's **Relaxation Length**, which keeps HVE's permanent crush.

A softer slope gives a longer spring-back and less permanent crush. The DyMESH collision model's page describes the law; the run status names the faces that state a slope.

!!! note "HVE Studio"
    Named **Unloading Stiffness** here until 2026-11-22. The case stores it as `unload_stiff` as before.

### Structure Restitution
**Law 2 only.** A number from 0 to 1 for each face: of the elastic energy a node stores, the share it gives back as it springs back -- the rebound. The node returns along Structure Restitution squared times **Elastic Stiffness** (the solver smooths that into a curve carrying the same energy), over the same spring-back distance, so it does not change the permanent crush. 1 retraces the elastic loading line; a smaller value gives a softer rebound. 0 means 0.8. Read only when the solver runs with `HVE_DYMESH_LAW=2` (and by the older bumper model, `HVE_DYMESH_BUMPER=1`); otherwise the run status says it is not applied.

### Bumper b0

Shown in the table as **No-crush speed**. **Law 2 only.** The barrier speed the vehicle can hit a flat rigid wall at and keep no permanent crush, for the **Front** and **Rear** columns (the side, top and bottom columns show "--"). The default is 5 mph. 0 means no bumper.

Every node of that face gets a soft, springy bumper in front of its structure. The bumper compresses first, bottoms out at 0.9 of the node's yield pressure, and always springs back to its shape, so any permanent crush is the structure's. You don't enter the bumper's stroke: the solver works it out when the vehicle loads. It finds the stroke at which the face, meeting a flat wall in the order its surface reaches it, takes the vehicle's whole kinetic energy at b0. The run's Messages report gives the stroke for each end, and says so if the face could not hold that energy within 12 in.

The stroke depends on the vehicle's mass: the same b0 on a heavier vehicle gives a longer stroke. A face with a low yield pressure also needs a long stroke. Only DyMESH law 2 reads b0 (the solver run with `HVE_DYMESH_LAW=2`); otherwise it is not applied, and the run status says so when you have changed it from 5 mph.

### Bumper Restitution

**Law 2 only.** A number from 0 to 1 for the **Front** and **Rear** columns: how much of the bumper's energy it gives back as it springs back (the share is this number squared). The default is 0.4. A low value suits a foam or crush-can absorber that returns little; a higher one a springier bumper. The bumper always returns to its shape whatever the value: restitution sets how much energy comes back, not how much crush is kept. 0 means use the solver's default. Like b0, only law 2 reads it.

It is the restitution of a bumper that takes an impact within its stroke, a low-speed impact. Published tests of foam and
crush-can bumpers put it near 0.4: about 0.4 at 8 km/h, falling to about 0.3 at 16 km/h. In a harder impact the bumper is
crushed along with the structure behind it and does not spring back like an intact one, so the solver moves the
bumper's share of returned energy from this value to **Structure Restitution** as the structure's permanent crush grows
from nothing to one bumper stroke. **Crush Stiffness from a Barrier Test** does not fit it: it sets 0.40, because a
48-56 km/h test puts too little of its energy into the bumper to tell one value from another.

## The graph

Above the table is a graph of the **selected** column. Click a column header, or edit a cell, to select that column; the column is highlighted, and the editor opens on **Front** each time. **2-D (per unit width)** / **3-D (per unit area)** picks the graph:

- **2-D (per unit width)** — force per unit width against crush: *A + B C* (blue) and *Kv C* (red).
- **3-D (per unit area)** — the pressure *Const + Linear C + Quad C² + Cubic C³* against crush, flat beyond **Saturation Crush** (marked on the graph).
  On a face that states an **Elastic Stiffness**, which therefore runs DyMESH law 2, the graph draws the law the solver uses: its pressure while loading (red) -- elastic to yield, then the polynomial -- and its unloading from a peak at 60 percent of the graph's span back to the permanent set (orange), with **yield** and **permanent set** marked. The polynomial alone is drawn faint for comparison. A note under the graph gives the numbers the scale hides: the crush at yield, the peak, how far the face springs back from it and how much it keeps. The bumper (Front, Rear) is not drawn: its stroke is sized when a run starts, from **Bumper b0**, the mesh and the mass, and the run's Messages report gives it.

The **Top** and **Bottom** columns have only the 3-D graph.

A 3-D law with a negative term (most often a negative **Linear**) can make the
pressure go below zero at some crush: a contact there would pull the two surfaces
together. The **Linear** cell of such a face is marked, and its tooltip gives the
crush at which the pressure turns negative (checked up to a tenth past **Saturation Crush**, or 60 in
where none is stated). A negative term is acceptable in a curve fit only if the
other terms keep the pressure positive over the crush the face will see.

!!! note "HVE Studio"
    HVE applies a negative pressure as entered. HVE Studio's DyMESH holds a node's
    pressure at zero instead (a contact pushes, it never pulls), and a run in which
    that happened says so in its status, naming the faces and the crush at which
    their law goes negative.

!!! tip "New in HVE Studio"
    The graph of the selected face.

## From a barrier test (law 2)...

Beside **From crash tests...**. It opens **Crush Stiffness from a Barrier Test**, which fits DyMESH law 2's values for the
Front or the Rear from one test into a flat rigid barrier -- the vehicle's acceleration record, checked before it is
used, on this vehicle's own collision body -- and puts them on that face. See
[Crush Stiffness from a Barrier Test](../new-features/12-case-intake-and-vehicle-data.md#crush-stiffness-from-a-barrier-test).

## From crash tests...

Under the table, in the Crush Stiffness editor only. It opens **Crush Stiffness from Crash Tests**, which works out CRASH3 A and B (and G, for reference) from one or more staged tests into a full-width rigid barrier, typed in or read from an NHTSA crash test file, and puts them on one side of this vehicle (and sets that side's 3-D terms from them over the Conversion Height, as **Calculate 3-D from 2-D** does) and, optionally, on this vehicle's EDCRASH events with damage on that side. See [Crush Stiffness from Crash Tests](../new-features/12-case-intake-and-vehicle-data.md#crush-stiffness-from-crash-tests).

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
