# Chapter 11 — Vehicle Model Definition (Part A: Sprung Mass)

*Adapted for HVE Studio from the HVE User's Manual (Version 5, Seventh
Edition, Jan 2006), Chapter 11.*

The Vehicle Editor displays the current vehicle in the viewport.
The HVE Vehicle Model is a general purpose physical/mathematical model of a
vehicle developed by EDC. The HVE Vehicle Model applies to any type of
vehicle having left-side and right-side wheels, including passenger cars,
pickups, vans, sport-utility vehicles, trucks, trailers, dollies and
barriers.

The Vehicle Editor allows editing of the parameters which define the HVE
Vehicle Model. The general categories for these parameters are:

- **Sprung Mass** — *Inertias, Move CG, Color, Geometry File, Contact
  Surfaces, Inter-vehicle Connections, Belt Restraints, Airbag Restraints,
  Aerodynamic Drag, Body Torsion* (this part).
- **Unsprung Masses** — *Suspension, Tire, Brake, Wheel x,y,z Coordinates*
  (see [Part C — Suspension](11c-suspension.md) and
  [Part D — Brakes, Tires and Wheels](11d-brakes-tires-wheels.md)).
- **Exterior** — the exterior dimensions and structural stiffness (see
  [Part B — Exterior](11b-exterior.md)).
- **Brake System** — the master cylinder or compressor, and the ABS system
  (see [Part E](11e-drivetrain-steering-brake-system.md)).
- **Steering System** (see [Part E](11e-drivetrain-steering-brake-system.md)).
- **Drivetrain** — *Engine, Transmission, Differential* (see
  [Part E](11e-drivetrain-steering-brake-system.md)).

These categories and their associated parameters are described in this
chapter.

!!! note "HVE Studio"
    In HVE these groups are reached by clicking the vehicle's CG, wheels,
    exterior spheres, master cylinder, steering wheel and engine in the
    Vehicle Viewer. HVE Studio has no pickable components; each group's dialog
    is opened from the **Vehicle** menu or the **Vehicles** panel. The map
    from HVE's components to HVE Studio's dialogs is in [Chapter 10, Selecting
    and Editing Vehicles](10-creating-editing-vehicles.md#selecting-and-editing-vehicles).
    Every value is shown in the units set in Tools › Preferences; the case
    stores SI.

## Inertial Properties

The inertial properties of the vehicle are displayed and edited using the
**Inertia / Mass** dialog (Vehicles panel › Inertia › **Edit…**). It shows paired **Total** (i.e., sprung + unsprung) and **Sprung**
columns side by side for the weight, the mass, the CG location (CG to front
axle, CG to rear axle, CG height) and the roll, pitch and yaw inertias.
Either column may be edited; the other is recalculated from the vehicle's
unsprung masses and their locations. The Vehicles panel's **Inertia** section
shows one line of the totals (weight, yaw, pitch and roll inertia).

!!! note "HVE Studio"
    - There is no Basic/Complex toggle: both columns are always shown.
    - The unsprung mass used for the conversion comes from the tire weights and, on a solid axle, the axle beam mass
      entered in Suspension Data.
    - A roll, pitch or yaw inertia the vehicle does not state is
      **estimated** from the mass and the wheelbase and track, and the
      solver uses the same estimate. Type a measured value to replace it.
    - **Cancel** discards every change made since the dialog was opened.

> **NOTE:** Typically, 2-D models use total vehicle inertial properties; 3-D
> models use the sprung mass properties. Why? The unsprung masses (i.e.,
> wheels and axles) have their own independent equations of motion.

HVE's Inertial Properties dialog also includes a feature that automatically
updates the rotational inertias when the weight is changed (described
below).

!!! warning "Not in HVE Studio"
    HVE Studio has no **Auto Update When Weight Changes** option: a stated
    rotational inertia is left unchanged when the weight is edited. Scale
    the inertias yourself if the mass distribution is to be kept (an
    *estimated* inertia follows the mass automatically).

![Figure 11-2](../images/hvn-04-inertia-mass.png)
*Figure 11-2: Inertia / Mass dialog, with its Total and Sprung columns.*

See also the reference page,
[Vehicle Inertia dialog](../../02-vehicles/VehInerDlg.md).

The Inertial Properties dialog performs a number of calculations, depending
on which values the user edits.

If the sprung weight, $W_{S}$, is edited, the total weight, $W_{T}$, is updated:

$$W_T = W_S + \sum_{n=1}^{NumAxles} W_U$$

where $W_{U}$ = unsprung weight of each wheel (plus axle for solid axle
suspensions).

If the total weight, $W_{T}$, is edited, the sprung weight, $W_{S}$, is updated:

$$W_S = W_T - \sum_{n=1}^{NumAxles} W_U$$

If the sprung rotational inertia, $I_{Sx}$, $I_{Sy}$ or $I_{Sz}$ (roll, pitch or
yaw, respectively), is edited, the total rotational inertia, $I_{Tx}$, $I_{Ty}$
or $I_{Tz}$, is updated using the parallel axis theorem:

    I_T = I_S + Σ(n=1..NumAxles) (I_U + m_U * r_U²)

where

- $I_{U}$ = rotational inertia of each wheel (and axle for solid axle
  suspensions) about its own x, y or z axis
- `m_U` = mass of each wheel (plus axle for solid axle suspensions)
- `r_U` = orthogonal distance from vehicle sprung mass CG to unsprung mass
  CG.

Similarly, if the total rotational inertia, $I_{Tx}$, $I_{Ty}$ or $I_{Tz}$ (roll,
pitch or yaw, respectively), is edited, the sprung rotational inertia,
$I_{Sx}$, $I_{Sy}$ or $I_{Sz}$, is updated using the parallel axis theorem:

    I_S = I_T − Σ(n=1..NumAxles) (I_U + m_U * r_U²)

In HVE, if the *Auto Update When Weight Changes* checkbox is checked, the
rotational inertias are updated as follows (not in HVE Studio):

a) If the sprung weight is edited, the updated sprung rotational inertias
are:

    I_S = I_S0 * (W_S / W_S0)

where

- $I_{S0}$ = sprung rotational inertia before editing sprung weight
- $W_{S0}$ = sprung weight before editing

The total rotational inertias, $I_{T}$, are then calculated using the parallel
axis theorem, as shown above.

b) If the total weight is edited, the updated total rotational inertias are:

    I_T = I_T0 * (W_T / W_T0)

The sprung rotational inertias, $I_{S}$, are then calculated using the
parallel axis theorem, as shown above.

To display or edit the current vehicle's inertial properties, perform the
following steps:

1. In the Vehicles panel, open the **Inertia** section and press
   **Edit…**. The Inertia / Mass dialog will be displayed.
2. View and/or edit the desired properties. The other properties are
   updated as described above as you type.
3. Press *OK* to close the dialog, or *Cancel* to discard the changes.

The Inertial Properties are described below.

- **Weight** — Vehicle total and sprung weight.

  > **NOTE:** HVE divides your entered value by the current gravitational
  > constant (see Environment Editor) and stores the resultant mass. That
  > way, if you take the vehicle to the moon, it will behave correctly!

- **Mass** — Vehicle total and sprung mass (weight/g). In HVE Studio the mass
  row is editable too; weight and mass follow each other.
- **Roll, Pitch and Yaw Rotational Inertias** — Vehicle total and sprung
  mass rotational inertias.
- **x-z Product of Inertia** — Product of inertia about the y axis. This
  value represents the fact that the x-z plane is not a plane of symmetry
  for the vehicle sprung mass. Entered on the sprung basis only (XZ Product
  (sprung)).

  > **NOTE:** For all practical purposes, a vehicle is symmetrical in the
  > x-y plane (i.e., about the z axis) and in the y-z plane (i.e., about the
  > x axis). Therefore, these inertial products are zero.


**Table 11-1: Inertial Properties**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Weight | UtVehForce | Vehicle total and sprung weight (HVE calculates and stores the mass by dividing the entered weight by the current acceleration of gravity) |
| Rotational Inertias | UtVehInertia | Vehicle total and sprung rotational inertias about the vehicle x, y and z (roll, pitch and yaw) axes |
| x-z Product of Inertia | UtVehInertia | Inertial product about the y axis |

## Move CG

The default CG (center of gravity) location of the vehicle sprung mass is
determined from raw data (e.g., measured or table values). The user may
choose to edit the CG location using the Move CG dialog. See also the
reference page, [Move CG dialog](../../02-vehicles/MoveCGDlg.md).

!!! note "HVE Studio"
    HVE Studio has two controls where HVE has one:

    - **Event › Move CG** (in the Event editor, for EDSMAC and EDSMAC4
      events) — HVE's Move CG dialog: ΔX, ΔY and ΔZ move the CG relative to
      the body, and every distance measured from the CG follows; CG Height
      is read-only. The CG location may also be edited directly in the Vehicles
      panel's Size & Weight section (CG to axle, CG height) and in the
      Inertia / Mass dialog.
    - **Vehicle › Editors › Vehicle Mesh › Move CG** (on the Vehicle Mesh window's File &
      Placement tab) — where the CG sits in the 3-D model file's own
      coordinates. Typing a new value moves the CG the same way: the body and
      the wheels stay, and the CG distances change (see
      [Geometry File](#geometry-file)).

> **NOTE:** The default location of the CG is determined by the wheel
> locations (which are defined relative to the CG). Refer to the Wheel
> Location parameters for more information.

> **NOTE:** Changing wheel z coordinates or tire radii for any wheel
> location will change the calculated CG height.

To display or edit the current vehicle's CG location (relative to the
default location), perform the following steps:

1. In the Event editor, with an EDSMAC or EDSMAC4 event active, choose
   **Event › Move CG**. The Move CG dialog will be displayed.
2. View and/or edit the desired properties.
3. Press *Apply* to apply the change.

The Move CG parameters are described below.

- **dx** — Moves the CG in the +x or −x direction, relative to the
  vehicle-fixed coordinate system (+x is *forward* in all coordinate
  systems).
- **dy** — Moves the CG in the +y or −y direction, relative to the
  vehicle-fixed coordinate system (+y is *to the right* in the SAE
  coordinate system).
- **dz** — Moves the CG in the +z or −z direction, relative to the
  vehicle-fixed coordinate system (+z is *down* in the SAE coordinate
  system).

**Table 11-2: Move CG Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| dx, dy, dz | UtVehDispLength | Adjustment of the default CG (center of gravity) location relative to the vehicle-fixed coordinate system |
| CG Height | UtVehDispLength | Approximate CG height, calculated from vehicle wheel positions and tire radius. Tire deflection is ignored. |

## Color

The color of the vehicle is obvious from looking at it. In HVE Studio it is
edited with the **Color** field in the Identity section of the Vehicles
panel: three R, G, B
values (0–255) and a swatch. Click the swatch to open a color picker (color
wheel or square, hue, saturation and value, or hexadecimal), or drag or type
in the R, G, B fields.

> **NOTE:** Do not use a fully saturated color if you plan to produce a
> video! Saturated colors (especially red) look bad on video.

!!! tip "New in HVE Studio"
    The vehicle color is what a material-less vehicle is painted with. For
    finer control of how a vehicle looks, give it, or each of its parts,
    a display material (Vehicle › Edit Mode and View › Shader Editor; see
    [Chapter 10](10-creating-editing-vehicles.md#edit-mode-materials-per-part)).

## Geometry File

The current vehicle may be visualized using a simplified vehicle shape or an
actual 3-D geometry file created by digitizing the vehicle. If a 3-D
geometry file is available for the current vehicle, it is assigned with the
**Mesh File** field in the **3D Geometry** section of the Vehicles panel, or
in the **Vehicle Mesh** window (Vehicle › Editors › Vehicle Mesh, Event › Vehicle Mesh,
or **Vehicle Mesh...** in the 3D Geometry section), which also holds every
other setting of the model.

![Figure 11-5](../images/hvn-04-vehicle-mesh.png)
*Figure 11-5: Vehicle Mesh window.*

### Mechanical Properties

The 3-D geometry file is not only used to visualize the vehicle, it is also
used to define the mechanical/structural properties of the vehicle exterior.
Each vertex includes a complete material specification. These material
properties are:

- **x,y,z coordinates** — Vehicle-fixed coordinates for each vertex (a
  typical mesh includes approximately 2500 to 5000 vertices, not including
  the wheels).
- **Force Constant** — K₀, the force required to initiate vertex
  deformation.
- **Linear Stiffness** — F₁, the linear force-deflection constant for the
  vertex.
- **Quadratic Stiffness** — F₂, the 2nd-order force-deflection constant for
  the vertex.
- **Cubic Stiffness** — F₃, the 3rd-order force-deflection constant for the
  vertex.
- **Damping Constant** — The velocity-dependent force constant for the
  vertex.
- **Friction Constant** — The friction multiplier for the vertex.
- **Maximum Force** — Yield force for the vertex.
- **Maximum Deflection** — Yield at failure for the vertex.
- **Unloading Slope** — Linear force-deflection relationship during
  unloading.

![Figure 11-6](../images/figure-11-6.jpg)
*Figure 11-6: View of 3-D geometry file (mesh), shown in HVE's SceneViewer. The mesh provides visual properties, as well as mechanical properties that may be used by collision algorithms.*

These material properties are available for collision algorithms to
simulate collision forces and moments, as well as to visualize the resulting
deformation to the vehicle exterior.

> **NOTE:** For more information regarding these parameters and how they are
> used, refer to the User's Manual for the particular simulation model being
> used.

**Table 11-3: Vehicle 3-D Geometry Mechanical Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| x,y,z coords | UtVehDispLength | Vehicle-fixed vertex coordinates |
| Material Name | UtNone | Material name |
| Constant | UtVehForce | Force required to initiate deflection |
| Linear Stiffness | UtVehMatLinear | Linear material deformation coefficient |
| Quadratic Stiffness | UtVehMatQuad | Quadratic material deformation coefficient |
| Cubic Stiffness | UtVehMatCubic | Cubic material deformation coefficient |
| Damping Constant | UtVehMatDamp | Material velocity-dependent deformation constant |
| Friction Constant | UtNone | Friction coefficient |
| Maximum Force | UtVehForce | Force at which 3rd-order force-deflection relationship is abandoned |
| Maximum Deflection | UtVehDispLinear | Deflection at which 3rd-order force-deflection relationship is abandoned |
| Unloading Slope | UtVehMatLinear | Linear unloading slope beginning at max deflection |

### Geometry File Options

In HVE, Geometry File offers *New, Open* and *Save-As*. In HVE Studio the
Vehicles panel's **3D Geometry** section holds the **Mesh File** field (with
**…** and **Library…**), **Generic Body** and **Vehicle Mesh...**, and the
Vehicle Mesh window holds the rest, in four tabs.

**File & Placement**

- **Mesh File** — the 3-D model. **…** browses for a file; **Library…**
  searches the vehicle geometry library by name. HVE's `.h3d` files, Open
  Inventor/VRML (`.iv`, `.wrl`), `.obj`, glTF (`.gltf`, `.glb`) and
  point-cloud scans (`.las`, `.ply`, `.e57`, `.xyz`, `.pts`) are read. With a
  display mesh set (Display tab), this section is headed **Collision Mesh
  (what DyMESH collides)**, because this file is then collided but not drawn.
- **Import Options** — Scale Factor, Smooth normals (use vn), Flip normals,
  **Center on CG** and Draw wheels (tire radius), then **Load 3D File** and
  **Clear**, and a status line: whether the mesh loaded (*Mesh did NOT load*,
  with the reason, if it did not), or that the vehicle is drawn and collided
  as the generated box. Normals and Draw wheels are display only.
- **Move, Rotate and Scale the Model** — **Move CG**, and HVE's Transform
  Vehicle Geometry: **Translate**, **Rotate** (degrees) and **Scale** per
  axis, applied scale, then rotate, then translate. SAE axes: +x forward, +y
  right, +z down. **Move CG** is where the CG sits in the model file's own
  coordinates; typing a new value **moves the CG**, as HVE's Move CG does: the
  body, the wheels and everything fitted to the vehicle stay where they are,
  and the CG-to-axle distances, CG-to-side distances and CG height change to
  match. A move that would put the CG at or below the ground is refused, with
  the reason under the row. To move the picture instead, use **Translate**.
  In the Vehicle editor's 3-D view, **G**, **R** and **S** move, rotate and
  scale the mesh and edit the same Translate, Rotate and Scale rows (see
  [Chapter 21](../08-3d-editor/21-manipulators.md)).

**Collision** — what DyMESH collides; these settings change the run.

- **Collision mesh max triangles** — the most triangles DyMESH collides
  for this body. A mesh with more is reduced for the collision alone; the
  full mesh is still drawn and the crush is carried onto it. **0**
  collides the file as authored, except that an OBJ or glTF body with more
  than 50 000 vertices is reduced automatically to 10 000 triangles, and
  the run status says so. A scan body always collides as a rebuilt
  surface; 0 gives it 10 000 triangles.
- **Collide as a closed outer shell** — rebuilds what collides as one
  closed outer surface (the mesh is sampled to points and rebuilt the way
  a scan is), so interior faces, open edges and loose pieces fall away;
  reduced to the triangle budget (0 = 10 000). The mesh is still drawn.
  Off for every HVE case.
- **Collides: n of m parts** — a list of the mesh's parts (its material
  names, and any parts made from faces in Edit Mode), each with a tick.
  Untick a part, such as a mirror or an antenna, to leave it out of what
  DyMESH collides; it is still drawn.
- A note says what DyMESH collides. When the drawn file is a scan, the scan
  tools (see [Scan bodies](#scan-bodies)) follow; for a scan used as the
  display mesh they are on the Display tab.
- **DyMESH Contact Mesh Preparation** — the vehicle's defaults for
  **Tessellate**, maximum triangle leg and weld distance. An event can state
  its own, which then outrank these: **Event › DyMESH Options** (Contact Mesh
  Preparation, per vehicle). A note here says when the active event does.

**Display** — how the model is drawn. Except **Collide the display mesh
instead** (below), nothing on this tab reaches an engine.

- **Opacity** and **Round shell** (curved subdivision: Off, 1 or 2 levels;
  needs Smooth normals).
- **Display Mesh (drawn instead)** — **Display File**: a second model or scan
  to draw in place of the collision mesh, for example a detailed model or a
  scan of the actual vehicle, with **…** and **Clear**. What collides does not
  change, so an imported HVE case keeps HVE's answer, and the drawn body wears
  the crush of the run. A display mesh has its own **Scale Factor**, **Center
  on CG**, **Move CG**, **Translate**, **Rotate** and **Scale**. A newly picked
  file is fitted to the collision body; **Align to collision mesh** fits it
  again: centred on the collision body and scaled uniformly to its length,
  keeping its Rotate, with what is left over in width and height reported.
  **Collide the display mesh instead** makes DyMESH collide the display mesh
  (reduced to the triangle budget, or rebuilt as a closed shell when that is
  ticked); this changes the run, and an imported HVE case
  then no longer collides HVE's own body.
- **Shading** — **As Loaded**, **Flat**, **Smooth** or **Auto Smooth**, with
  the **Auto Smooth Angle** (default 60°) for the last. As Loaded uses the
  file's own normals; Auto Smooth smooths across edges whose faces meet
  within the angle and keeps sharper edges creased.
- **Damage Display** — Smooth crush deformation and its number of passes
  (reported crush depths and energies are the solver's).

**Wheel Images** — the picture drawn on each wheel's face (see
[Chapter 11, Part D](11d-brakes-tires-wheels.md)). Display only.

**Center on CG** is off by default. On, the body is placed by the middle of
its length and width instead of taking the file's own origin as the CG, and
that moves the body the run collides with, not only the picture. Leave it off
for a body authored about its CG, as every HVE vehicle file is: a real body's
extents are rarely centred on its CG. Use Move CG to correct a known offset.

A vehicle picked from a vehicle database names its mesh by the database it came
from (`<database>#sha256:…/<name>`). Where that database is missing or not
licensed on this computer, the 3D Geometry section says that *<name> from
<database>* is not available and that the vehicle draws and collides as the
generic box.

#### Scan bodies

A point-cloud **Mesh File** (`.las`, `.ply`, `.e57`, `.xyz`, `.pts`) is drawn
as its points, and DyMESH collides a closed surface rebuilt from them (its size
is in the run status). Two kinds of points are removed, from the drawn points
and from the collided surface alike:

- every point inside one of the case's wheels (its axle position, track, tire
  radius and width); the case's own wheel and tire are drawn there instead. A
  note gives how many points were removed, with a warning for each wheel where
  the scan does not fit the case (a tire past the radius, a face off the
  track);
- every point at, or within 2 cm of, the case's ground plane (the floor and
  the contact patches).

**Erase points** removes other points that are not the vehicle (the ground,
people, other cars). Tick it and paint over them in the viewport with the
**Brush** (its **Brush size** in pixels), or choose **Box** and drag a box that
takes everything inside it through all depth. The erased areas are stored in
the case, on the scan's own coordinates, so they stay on their points whatever
the placement does later; the scan file is never changed. **Undo last** puts
back the last stroke and **Restore all** puts back every point. Erased points
are neither drawn nor collided. The wheel note and Erase points are shown under
the section of the file they act on: under Display Mesh when the scan is the
display mesh.

> **NOTE:** If no file is assigned, or the file cannot be loaded, the vehicle
> is visualized as a simple vehicle body (defined according to its type and
> dimensions) — and DyMESH collides it as that body, not only draws it.

> **NOTE:** An OBJ or glTF body whose triangles face inward as placed (a
> mirrored placement, or the file's own winding) is turned to face out before
> DyMESH collides it, because DyMESH crushes a node along its inward side; the
> run status says so. A body that encloses too little of its box to tell which
> way it faces is reported too, with the advice to collide it as a closed
> shell. HVE's own Inventor bodies are never changed.

#### New

HVE's *New* removes the 3-D geometry file and replaces it with the simple
vehicle shape. In HVE Studio press **Clear** on the File & Placement tab of the
Vehicle Mesh window.

#### Open

To assign a 3-D geometry file to the current vehicle:

1. Choose **Vehicle › Editors › Vehicle Mesh** (or press **Vehicle Mesh...** in the
   Vehicles panel's **3D Geometry** section) and select the **File &
   Placement** tab.
2. Press **…** beside Mesh File and choose the file, or press **Library…**
   and search for it by name. (The same Mesh File row is in the panel's 3D
   Geometry section.)
3. Press **Load 3D File**.

The selected 3-D geometry file is displayed on the current vehicle.

#### Save-As

!!! warning "Not in HVE Studio"
    HVE Studio does not write vehicle geometry files. The whole scene,
    vehicles included, can be exported as glTF with **File › Export Scene
    for Blender**.

## Contact Surfaces

The current vehicle may include contact surfaces used for simulating
interaction forces between the vehicle and its occupants or pedestrians.

Contact Surfaces are planes defined by 3 corners (the fourth corner is
automatically assigned by assuming a parallelogram). Contact surfaces are
created using the Contact Surfaces dialog (**Vehicle › Editors › Contact Surfaces**).

![Figure 11-7](../images/figure-11-7.jpg)
*Figure 11-7: Vehicle contact surfaces — both interior and exterior contact surfaces are permissible (rendered in HVE).*

![Figure 11-8](../images/hvn-04-contact-surfaces.png)
*Figure 11-8: Contact Surfaces dialog (HVE Studio): the surface list, the selected surface's classification and geometry, and the Derive, template and interior-file controls below.*

The Contact Surfaces dialog lists the vehicle's surfaces on the left; the
selected surface is edited on the right. Click a name to select it;
Ctrl-click and Shift-click select several (for Delete). To create and edit a
contact surface, perform the following steps:

1. Choose **Vehicle › Editors › Contact Surfaces**. The Contact Surfaces dialog is
   displayed, and the vehicle's surfaces are drawn in the viewport, each with
   an arrow showing its normal. A surface may also be selected by clicking
   it in the viewport.
2. Press **Add** to add a surface ("Surface *n*"), and enter its **Name**.
   **Material** is the material's name.
3. Set **Class** (*Vertex*, *Face* or *Group* — HVE's Bind Material To) and
   **Side** (*Interior* or *Exterior* — HVE's Location).

   > **NOTE:** The simulation may use this information to reduce the number
   > of contacts for which it must calculate forces, based on whether the
   > human is an occupant or pedestrian. For example, it is unnecessary to
   > calculate the force between a pedestrian and seat cushion, since none
   > will occur. (See Event Editor, Contacts Dialog, for more information.)

4. Enter the geometry, in vehicle-fixed coordinates. By default the surface
   is edited as a rectangle: **Centre** (X, Y, Z), **Size** (Width, Height)
   and **Angles** (Yaw, Pitch, Roll, in degrees, applied 3-2-1). Check
   **Edit corner points instead** to enter HVE's three corners directly:
   **P2 (corner)**, **P3 (+width)** and **P1 (+height)**.

   > **NOTE:** The "right hand rule" is used to determine the positive side
   > of the contact surface. The dialog displays the surface's **Normal**;
   > **Flip** reverses it. Force on the contact surface is only calculated if
   > it is struck on the positive side!

   > **NOTE:** The fourth corner is created automatically assuming a
   > parallelogram. A skewed (non-rectangular) surface is kept only in the
   > corner-point form; editing it as a rectangle squares it up.

   ![Figure 11-9](../images/p357-figB11-9.png)
   *Figure 11-9: Convention for contact surfaces — three consecutive corners are selected; the right hand rule determines the positive side.*

5. Open **Material Properties** and edit the surface's force-deflection,
   damping and friction properties (see below). They apply only to this
   surface.

It is important to confirm the contact surfaces are correctly positioned
and facing the right direction within the vehicle. Carefully view each
surface to ensure its correct position and orientation.

> **NOTE:** The surfaces are drawn while the Contact Surfaces, Belt
> Restraint or Airbags dialog is open. **View › Scene Display › Occupant
> Equipment** draws them at any time.

Changes take effect as they are made; Edit › Undo reverses them.

!!! tip "New in HVE Studio"
    Below the list:

    - **Derive from Mesh** builds surfaces from the flat regions of a named
      group of the vehicle's 3-D model ("interior" for the cabin, "body" for
      the exterior shell a pedestrian strikes), in the chosen region;
      **Pedestrian preset** sets both for a pedestrian impact. Only the
      geometry is derived, not the material.
    - **Seed Standard Interior** replaces the list with a generic driver
      compartment (seat, floor, toe pan, instrument panel, wheel, glass,
      roof, doors) scaled from the vehicle's dimensions — generic, not
      measured.
    - A template list and **Use Template** replace the list with a set of
      surfaces authored in HVE on a real vehicle, with their materials (not
      rescaled).
    - **Save Interior…** and **Load Interior…** write and read the vehicle's
      contact surfaces as a standalone file, for reuse on another vehicle or
      case (not rescaled).

The Contact Surface parameters are described below.

- **Bind Material To** (HVE Studio: **Class**) — Assigns an attribute,
  *Vertex*, *Face* (polygon) or *Group*; the simulation uses this attribute
  to determine whether the material is associated with the vertex or
  polygonal area.
- **Location** (HVE Studio: **Side**) — Assigns an attribute, either *Interior* or *Exterior*,
  available for use by the simulation model to distinguish between surfaces
  on the vehicle's interior and exterior.
- **Material Name** — Assigns a user-editable name to the material; not
  used in calculations.
- **x,y,z** — Assigns the vehicle-fixed x,y,z coordinates for the three
  corners of the contact surface (the fourth is assigned by assuming a
  parallelogram).
- **Constant** (HVE Studio: **Force Constant**) — The force required to
  initiate deflection.
- **Linear Stiffness** — The first-order force vs deflection constant for
  the current contact surface.
- **Quadratic Stiffness** — The second-order force vs deflection constant
  for the current contact surface.
- **Cubic Stiffness** — The third-order force vs deflection constant for
  the current contact surface.
- **Damping Constant** — The velocity-dependent force contribution for the
  current contact surface.
- **Friction Constant** — Assigns friction characteristics to the surface;
  normally the friction between two surfaces is the arithmetic average of
  their individual friction coefficients.
- **Maximum Force** (HVE Studio: **Max Force (0=inf)**) — The maximum force
  resisted by the contact surface; if exceeded, force remains constant until
  the Maximum Deformation is reached.
- **Maximum Deflection** — The maximum allowable material deformation.
- **Unloading Slope** (HVE Studio: **Unloading Stiffness**) — A value used to
  assign hysteresis. The unloading slope defines the force vs deflection
  relationship during unloading.
- **Max Penetration** — The deepest penetration for which the occupant
  simulation (EDHIS) computes a contact force; HVE's Max Defl/Timestep.

> **NOTE:** The unloading slope should be steeper than the loading slope!

!!! note "HVE Studio"
    - The material properties are edited in the **Material Properties**
      section of the Contact Surfaces dialog; there is no separate material
      dialog, no force-deflection plot and no material database to choose
      from.
    - A Max Deflection of 0 is replaced by 0.25 m for occupant contact, and
      a Max Penetration of 0 by Max Deflection (else 0.25 m).

![Figure 11-11](../images/p361-figB11-11.png)
*Figure 11-11: Typical force vs deflection curve for a contact surface. The loading slope (which occurs during penetration) may be defined by a 3rd-order polynomial: F = ad + bd² + cd³, where a = Linear Stiffness, b = Quadratic Stiffness, c = Cubic Stiffness. During unloading the slope is assumed linear: F = u(d_max − d), where u = Unloading Slope.*

**Table 11-4: Vehicle Contact Surface Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Bind To | UtNone | Flag indicating whether material attributes are attached to each vertex or each face |
| Location | UtNone | Flag indicating whether the surface is an interior or exterior surface |
| x,y,z coords | UtVehDispLength | Vehicle-fixed vertex coordinates for each of 3 corners |
| Material Name | UtNone | Material name |
| Constant | UtVehForce | Force required to initiate deflection |
| Linear Stiffness | UtVehMatLinear | Linear material deformation coefficient |
| Quadratic Stiffness | UtVehMatQuad | Quadratic material deformation coefficient |
| Cubic Stiffness | UtVehMatCubic | Cubic material deformation coefficient |
| Damping Constant | UtVehMatDamp | Material velocity-dependent deformation constant |
| Friction Constant | UtNone | Friction coefficient |
| Maximum Force | UtVehForce | Force at which 3rd-order force-deflection relationship is abandoned |
| Maximum Deflection | UtVehDispLinear | Deflection at which 3rd-order force-deflection relationship is abandoned |
| Unloading Slope | UtVehMatLinear | Linear unloading slope beginning at max deflection |

## Belt Restraints

The belt restraint systems of the vehicle are displayed and edited using the
Belt Restraint System dialog (**Vehicle › Editors › Belt Restraint**, also Event ›
Restraints › Belt Restraint).

![Figure 11-12](../images/hvn-04-belt-restraint.png)
*Figure 11-12: Belt Restraint System dialog (HVE Studio), EDHIS tutorial case,
Buick Skylark driver.*

!!! note "HVE Studio"
    In HVE Studio a belt system is kept per OCCUPANT of the vehicle rather than
    per seat: the dialog's **Occupant** list chooses whose belts are edited
    (it follows the human selected in the Occupants panel). What the occupant
    actually wears is stated per event, in **Restraint In Use** (None, Lap
    Belt, 3-Point Belt, Airbag + Belt), which edits the active event.

To display or edit the current vehicle's belt properties, perform the
following steps:

1. Choose **Vehicle › Editors › Belt Restraint**. The Belt Restraint System dialog will
   be displayed, and the belt anchors are drawn in the viewport.
2. Choose the occupant in the **Occupant** list, and set **Restraint In
   Use** for the active event.
3. Check **Torso Belt Installed** and/or **Lap Belt Installed** (HVE's
   Device Installed, per section).
4. Choose the **Section** (Torso (shoulder) or Lap) to edit. Each section
   has its own anchors, slack and webbing, and **Attached To** names the
   occupant segment it is attached to (by default the chest for the torso
   section and the pelvis for the lap section).
5. View and/or edit the section's properties.
6. Repeat for the other section and each occupant.

The Belt Restraint Properties are described below.

- **Occupant** — Whose belt system is edited (HVE: Seat Location).
- **Belt Section** — The section (torso or lap) of the current belt
  restraint system.
- **Torso / Lap Belt Installed** — The vehicle has that belt section.

The following belt properties may be assigned for the left and right sides
of each section:

- **Left / Right Anchor: Slack, I, J, K** — The slack, and the point where
  the belt attaches to the occupant's segment, in the segment's coordinates.
- **Vehicle Anchor: Veh I, J, K (left and right)** — The vehicle-fixed
  coordinates (about the CG) where the belt is attached to the vehicle.
- **Stiffness** — The first-order force vs deflection constant for the belt
  section.
- **Damping** — The velocity-dependent contribution to stiffness for the
  current belt section.
- **Break Strength** — The breaking strength of the belt. If exceeded, belt
  force becomes zero.

!!! warning "Not in HVE Studio"
    The belt's Quadratic and Cubic stiffness and its Unloading Slope have no
    control in HVE Studio. A value imported from an HVE case is kept. As the
    dialog states, EDHIS reads Stiffness, Damping and Break Strength and
    GATB does not: GATB uses ATB's own fixed webbing curve, as HVE does.

**Table 11-5: Belt Restraint System Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Location | n/a | Location index (Right Front, Left Front, ..., Left Back) used to assign the location of the current belt section |
| Section | n/a | Torso or Lap belt section |
| Device Installed | BOOLEAN (True or False) | Switch that determines that a restraint is installed at the selected location and section |
| x,y,z | UtVehDispLength | Vehicle-fixed x,y,z coordinates for the anchor point of the belt |
| Linear Stiffness | UtVehMatStiffLinear | First-order force vs deflection constant |
| Quadratic Stiffness | UtVehMatStiffQuad | Second-order force vs deflection constant |
| Cubic Stiffness | UtVehMatStiffCubic | Third-order force vs deflection constant |
| Damping Constant | UtVehMatDamp | Velocity-dependent force contribution |
| Max Force | UtVehForce | Maximum allowable force |
| Unloading Slope | UtVehMatStiffLinear | Force vs deflection constant during unloading |

## Airbag Restraints

The airbags are displayed and edited using the **Airbags** dialog
(**Vehicle › Editors › Airbags**, also Event › Restraints › Airbags). As in HVE, a bag
belongs to the vehicle, one per seat location: choose the **Seat** at the top
of the dialog (each seat is listed with the occupants seated there in the
active event, and whether it has a bag). For the selected seat the dialog
holds **Device Installed**; the **Position** (vehicle-fixed, from the CG);
**Timing** (Begin Fill Time, Fill Duration); the **Contact Segments** (Head,
Chest, Arm); the **Reaction Panel** (the primary, backside panel the bag
deploys from, and up to three confining panels) and the bag's offset on it;
**Bag Geometry** (Full Inflated Volume, Initial Radius, Passenger Bag Length);
**Gas Properties** (Initial Pressure, Gas Density, Mass Flow Rate, Specific
Heat Ratio); **Vent** (Discharge Coef, Vent Area, Pressure Open Vent);
**Contact** (Column Angle, Col. Load, Max Col. Disp, Max Penetration, Force
Conv. Criterion); the **Membrane** (Bag Membrane Thickness and the Elastic,
Rebound and Bottom-out Moduli); and an **ATB Gas Dynamics (GATB)** section.

![Figure 11-14](../images/p367-figB11-14.png)
*Figure 11-14: Airbag x,y,z deployment coordinates and deployment (column) angle.*

!!! note "HVE Studio"
    The dialog states which fields reach which engine: the Position and Fill
    Duration are read by EDHIS, the Begin Fill Time by EDHIS and GATB, and
    the Contact Segments and reaction panels by GATB. An occupant uses the bag
    at their seat (the human's Location) in the event's vehicle, and only
    when the occupant's **Restraint In Use** in the event is Airbag + Belt; an
    Airbag + Belt occupant at a seat with no bag installed is refused by the
    run.

To display or edit a seat's airbag, perform the following steps:

1. Choose **Vehicle › Editors › Airbags**. The dialog opens on the seat of the occupant
   selected in the Occupants panel.
2. Choose the **Seat**, check **Device Installed** and edit the bag's
   properties. A pedestrian has no seat and no airbag.
3. Set the occupant's **Restraint In Use** to Airbag + Belt for the event
   (Vehicle › Editors › Belt Restraint, or Event Information).

The Airbag Restraint Properties are described below, under HVE's names.

- **Seat Location** — A position index used to determine the location of
  the current airbag restraint system. In HVE Studio it is the dialog's **Seat**;
  an occupant uses the bag at their seat (the human's Location).
- **Device Installed** — A checkbox to indicate the vehicle has an airbag
  system at the current location.
- **x,y,z Deployment Coordinates** — Assigns the vehicle-fixed x,y,z
  coordinates where the airbag is installed and deployed (HVE Studio:
  **Position**).
- **Initial Bag Radius** — Assigns the initial radius for the airbag.
- **Passenger Airbag Length** — Assigns the length for non-driver-side
  airbags.

  > **NOTE:** The driver's position is defined by Driver Location, in the
  > Configuration section of the Vehicles panel.

- **Initial Pressure** — Assigns the initial pressure for the airbag.
- **Bag Membrane Thickness** — Assigns the material thickness for the
  airbag.
- **Bag Full Inflation Volume** — Assigns the volume inside the airbag when
  fully inflated.
- **Vent Discharge Coefficient** — Assigns the thermodynamic discharge
  coefficient for the airbag vent hole.
- **Vent Discharge Area Coefficient** — Assigns the area of the airbag vent
  hole.
- **Pressure To Open Vent Hole** — Assigns the airbag pressure required to
  cause the vent hole to open.
- **Force Convergence** — Assigns the permissible force imbalance between
  the airbag and contact surfaces.
- **Maximum Penetration** — Assigns the penetration required before any
  force is computed.
- **Bag Elastic Modulus** — Assigns the elastic modulus for the airbag
  material during airbag filling.
- **Bag Rebound Modulus** — Assigns the elastic modulus for the airbag
  material during rebound.
- **Bag Bottom-out Modulus** — Assigns the elastic modulus for the airbag
  material after it has bottomed out.
- **Gas Density** — Assigns the gas density for the airbag filling agent.
- **Gas Mass Flow Rate** — Assigns the mass flow rate for the airbag
  filling rate.
- **Gas Specific Heat** — Assigns the specific heat (ratio) for the airbag
  filling agent.
- **Maximum Column Collapse Distance** — Assigns the maximum distance the
  steering column is allowed to collapse (applies to driver-side airbags
  only).
- **Column Collapse Load** — Assigns the axial load on the steering column
  required to begin collapsing the column (applies to driver-side airbags
  only).
- **Column Angle** — Assigns the steering column angle, about the vehicle's
  pitch axis (normally a negative angle).
- **Backside Contact Surface** — The contact surface supporting the airbag
  (HVE Studio: the reaction panel, chosen from the vehicle's contact surfaces).

> **NOTE:** An airbag must be supported on the backside. Otherwise, the bag
> would simply bounce away from the occupant.

> **NOTE:** This list of backside contact surfaces comes from the vehicle's
> interior contact surfaces.

!!! note "HVE Studio"
    No case in HVE's reference set runs an airbag, so the airbag path has
    been checked for placement and timing but its effect on an occupant has
    not been validated against HVE.

**Table 11-6: Airbag Restraint System Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Location | n/a | Location index (Right Front, Left Front, ..., Left Back) used to assign the location of the airbag |
| Device Installed | BOOLEAN (True or False) | Switch that determines that an airbag restraint is installed at the selected location |
| Deploy x,y,z | UtVehDispLength | Vehicle-fixed x,y,z coordinates for the airbag deployment location |
| Initial Bag Radius | UtVehDispLength | Radius of the (spherical) airbag at the start of filling |
| Passenger Bag Length | UtVehDispLength | Length of the (cylindrical) airbag used for passenger-side airbag systems |
| Initial Bag Pressure | UtVehDispPress | Airbag pressure at the start of filling |
| Membrane Thickness | UtVehDispLength | Thickness of the airbag material |
| Full Inflation Vol | UtVehVolume | Volume of the airbag at full inflation |
| Discharge Coef | UtNone | Thermodynamic discharge coefficient of the airbag vent |
| Discharge Area | UtVehArea | Area of the airbag vent |
| Vent Opening Pressure | UtVehPress | Pressure required to open the vent |
| Bag Penetration for Force | UtVehDispLength | Minimum deflection of an ellipsoid into the airbag required to produce a force |
| Force Convergence Criterion | UtVehForce | Allowable difference between force on the airbag and force on the human |
| Bag Elastic Modulus | UtVehMatStiffQuad | Elastic modulus of the airbag membrane material during force application |
| Bag Elastic Modulus on Rebound | UtVehMatStiffQuad | Elastic modulus of the airbag membrane material during unloading |
| Bag Elastic Modulus When Bottomed Out | UtVehMatStiffQuad | Elastic modulus of the airbag membrane material at maximum penetration |
| Gas Density | UtVehDensity | Density of the airbag filling agent |
| Max Column Collapse | UtVehDispLength | Maximum column stroke before it bottoms out |
| Column Collapse Load | UtVehForce | Force required to initiate column collapse |
| Column Angle | UtVehDispAngle | Deployment (pitch) angle |
| Backside Contact | n/a | The name of the contact surface supporting the airbag (no force can exist between the human and airbag unless the airbag is supported on a contact surface that provides a reaction force) |

*(Note: the legacy table listed the Full Inflation Vol unit as UtVehForce;
this is a typo — the quantity is a volume.)*

## Inter-vehicle Connections

The connections between tow vehicles and trailers are displayed and edited
using the Inter-vehicle Connections dialog.

The available inter-vehicle connections are:

- Ball/Hitch
- Fifth Wheel/King Pin
- Pintle Hook/Eye (drawbars may be *Fixed* or *Hinged*)

![Figure 11-15](../images/hvn-04-connections.png)
*Figure 11-15: Vehicle Connections dialog (HVE Studio).*

![Figure 11-16](../images/p372-figB11-16.png)
*Figure 11-16: Converter (hinged fifth wheel) and Fixed (hinged drawbar) dollies.*

To display or edit the current vehicle's connection properties, perform the
following steps:

1. In the Vehicles panel, open **Components** and press
   **Connections…**. The Vehicle Connections dialog will be displayed. It is
   a table with a **Front** and a **Rear** column and the rows **Type**,
   **X**, **Y**, **Z**, **Height above ground** and **Properties**.
2. To put a connection on the front of a towed vehicle (e.g., a trailer),
   choose a **Type** in the **Front** column (*None, Hitch, King Pin, Pintle
   Eye, Fixed* or *Pintle Eye, Hinged*) and enter the vehicle-fixed X, Y and
   Z coordinates under it.
3. To put a connection on the rear of a tow vehicle (e.g., a passenger car
   or truck tractor), choose a **Type** in the **Rear** column (*None, Ball,
   5th Wheel* or *Pintle Hook*) and enter its coordinates.
4. Press **Properties…** in the Rear column to edit the rear connection's
   properties in the Connection Properties dialog.
5. Press **Close** to close the dialog.

Both type lists offer all the connector types, each labelled *(trailer)* or
*(tow)*. The connection properties belong to the towing end, so they are
set on the tow vehicle's rear connection; the Front column's Properties row
says so. The **Height above ground** row shows each connection's height,
which must match the mating connector's to within about 0.1 in (0.003 m).

Edits take effect as they are made; **Edit › Undo** takes one back. The
Connection Properties dialog also has a single **Close** button.

!!! note "HVE Studio"
    The Connection Properties dialog carries HVE's full set: **Radius**,
    **Friction**; Linear: **Free Play**, **Stiffness**, **Damping**,
    **Breakaway Force**; Angular: **Max Articulation** Roll, Pitch and Yaw,
    **Stiffness**, **Damping**, **Breakaway Torque**. Yaw is the
    jackknife limit the simulations test. Each field's tooltip says which
    simulation reads it; Free Play and the roll and pitch limits are stored
    but no simulation reads them, and the stiffness and damping terms are
    read only under SIMON's Tow Vehicle Properties constraint model. A
    Breakaway Force or Torque of 0 means the connection cannot fail.

The Inter-vehicle Connection Properties are described below.

- **Front Connection Type** — The type of connection on the front of the
  current vehicle. The allowable types are *None, Hitch, King Pin* and
  *Pintle Eye* (fixed or hinged drawbar).
- **Front Connection Coords** — The vehicle-fixed x,y,z coordinates of the
  front connection.
- **Rear Connection Type** — The type of connection on the rear of the
  current vehicle. The allowable types are *None, Ball, Fifth Wheel* and
  *Pintle Hook*.

  > **NOTE:** During Event Mode, the simulation model normally checks to
  > see the user has selected vehicles with compatible connections: a Hitch
  > on the trailer must be connected to a Ball on the tow vehicle; a King
  > Pin on the trailer must be connected to a Fifth Wheel on the tow
  > vehicle; a Pintle Eye on the trailer must be connected to a Pintle Hook
  > on the tow vehicle. Otherwise, the simulation model should issue a
  > message: Incompatible Connections. (In HVE Studio the Event Information
  > dialog checks the whole rig and says what is wrong.)

- **Rear Connection Coords** — The vehicle-fixed x,y,z coordinates of the
  rear connection.

  > **NOTE:** The earth-fixed elevation of the connection above ground
  > should be approximately equal on the rear connection of the tow vehicle
  > and the front connection of the trailer. Otherwise, the trailer will be
  > pitched up or down as necessary to make the connection. This can cause
  > some physics models to compute an acceleration. For this reason, the
  > physics model may terminate with an error message.

- **Friction** — The friction coefficient at the connection between the tow
  vehicle and trailer.
- **Friction Radius** — The moment arm at which the frictional torque acts
  at the connection between the tow vehicle and trailer.
- **Maximum Articulation Angle** — The maximum articulation angle allowable
  between the tow vehicle and trailer.

**Table 11-7: Inter-vehicle Connection Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Front Connection Type | n/a | Type of front connection (None, Hitch, King Pin or Pintle Eye) |
| Front Connection Coordinates | UtVehDispLength | Vehicle-fixed coordinates of the front connection |
| Rear Connection Type | n/a | Type of rear connection (None, Ball, Fifth Wheel or Pintle Hook) |
| Rear Connection Coordinates | UtVehDispLength | Vehicle-fixed coordinates of the rear connection |
| Connection Friction | n/a | Friction coefficient at the connection |
| Connection Friction Radius | UtVehDispLength | Frictional moment arm |
| Maximum Articulation Angle | UtVehDispAngle | Maximum articulation angle between the tow vehicle and trailer |

## Aerodynamic Drag

The vehicle drag associated with aerodynamic pressure. The Aerodynamic Drag
dialog allows the user to view or edit these properties. See also the
reference page,
[Aerodynamic Drag dialog](../../02-vehicles/VehDragDlg.md).

![Figure 11-17](../images/hvn-04-aerodynamic-drag.png)
*Figure 11-17: Aerodynamic Drag dialog (HVE Studio).*

To display or edit the current vehicle's drag factors, perform the following
steps:

1. Choose **Vehicle › Editors › Aerodynamic Drag** (or Vehicles panel › Components ›
   Aerodynamic Drag…). The Aerodynamic Drag dialog will be
   displayed.
2. The four surfaces, **Front**, **Rear**, **Left** and **Right**, are the
   table's columns (by default, the front surface has already been assigned
   those properties associated with velocity-dependent air drag).
3. View and/or edit the desired properties, one row each: **Drag Device
   Installed**, **Drag Coef**, **Lift Coef**, **Side Coef**, **Surface
   Area** and **Center of Pressure X**, **Y** and **Z**.
4. Press **Close**.

!!! warning "Not in HVE Studio"
    HVE Studio offers four surfaces — Front, Rear, Left and Right. HVE's Top,
    Bottom, Front Device and Back Device surfaces have no control.

The Aerodynamic Drag parameters are described below.

- **Surface Option List** — In HVE, assigns the selected surface (*Front,
  Right, Back, Left, Top, Bottom, Front Device, Back Device*). HVE Studio has no
  surface selector: its four surfaces are the dialog's columns.
- **Device Installed** — Switch that activates the selected surface.
- **Drag Coefficient** — Assigns the properties resisting motion due to
  dynamic air pressure acting on the selected surface in the direction of
  the vehicle's total velocity vector. The force associated with this
  pressure is proportional to the velocity squared.
- **Lift Coefficient** — Assigns the properties resisting motion due to
  dynamic air pressure acting on the selected surface in the direction
  normal to the vehicle's total velocity vector.
- **Projected Surface Area** — Assigns the projected area parallel to the
  selected surface.
- **Center of Pressure** — Vehicle-fixed coordinates where the effective
  force from aerodynamic pressure is applied.

**Table 11-8: Vehicle Aerodynamic Drag Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Surface Name | n/a | Name of selected aerodynamic surface |
| Device Installed | n/a | Flag indicating device is installed and is capable of producing aerodynamic force on the vehicle |
| Drag Coefficient | UtVehDragQuad | Coefficient of aerodynamic drag acting on surface |
| Lift Coefficient | UtVehDragQuad | Coefficient of aerodynamic lift acting on surface |
| Projected Surface Area | UtVehArea | Projected surface area parallel to selected surface |
| Center of Pressure | UtVehDispLength | Vehicle-fixed coordinates where the aerodynamic force is applied |

## Body Torsion

The HVE Vehicle Model includes the capability to model torsional distortion
of the body. By default, the body is assumed to be rigid. However, the user
may wish to edit these default parameters, if the actual torsional stiffness
of the body is known, to study the effect of torsional distortion on vehicle
handling. The Body Torsion dialog is used to edit these properties. See also
the reference page,
[Body Torsion dialog](../../02-vehicles/BodyTorDlg.md).

To display or edit the vehicle's torsional data, perform the following
steps:

1. Choose **Vehicle › Editors › Body Torsion**. The Body Torsion dialog will be
   displayed.
2. Edit the **Torsional Stiffness** and the torsional roll axis location
   (**CG to Torsion Axis**).

!!! note "HVE Studio"
    As the dialog states, the body torsion is used only by an articulated
    vehicle: SIMON applies it in the tow/trailer constraint moment and EDVDS
    reports it. A single vehicle ignores it.

**Table 11-9: Vehicle Body Torsion Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| Axis Location | UtVehDispLength | Vehicle-fixed z-distance from the CG to the torsional roll axis |
| Body Stiffness | UtVehTorque | Torsional stiffness of the body |


<!-- NAV -->

---

← Previous: [Chapter 10 — Creating & Editing Vehicles](10-creating-editing-vehicles.md)  |  [Index](README.md)  |  Next: [Chapter 11 — Vehicle Model Definition (Part B: Exterior)](11b-exterior.md) →

<!-- /NAV -->
