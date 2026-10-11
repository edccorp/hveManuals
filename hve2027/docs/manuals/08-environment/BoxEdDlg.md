# Box Editor Dialog

In HVE the Box Object Tool creates and edits 3-D boxes in the environment —
buildings, sidewalks, curbs and other box-shaped objects — with a Box Editor
dialog for the selected box's position, orientation and size.

!!! note "HVE 2027"
    In the Environment editor (F4) choose **Environment › Scene Box Editor...**.
    The **Scene Box Editor** window lists the scene's boxes on the left and
    edits the selected one on the right. Lengths follow the units set in
    Tools › Preferences.

![Scene Box Editor window](images/hvn-scene-box-editor.png)

!!! warning "Display only"
    A scene box is drawn in the 3-D view and nothing else: no physics program
    sees it, so a vehicle cannot strike, drive on or settle onto it. To model a
    curb, wall or building that the vehicles interact with, include it in the
    environment's terrain geometry (Environment › Environment..., Terrain) and
    give its surfaces the right type (see
    [Environment Material Properties](EnvrMatPropDlg.md)).

## Box list, Add, Delete

Select a box in the list to edit it. **Add** creates a box ("Box 1", "Box 2",
…); **Delete** removes the selected one.

## Name

The box's name.

## Position (x fwd, y right, z up)

**X**, **Y**, **Z** — the box's position in the scene. Note that Z is measured
**up** here.

## Size

**L**, **W**, **H** — the box's length (along its x), width (y) and height (z).

!!! note "HVE 2027"
    HVE's Box Editor forces the height equal to the length when applied;
    HVE 2027 applies all three as entered.

## Rotation (deg)

**Rx**, **Ry**, **Rz** — rotation of the box about the x, y and z axes, in
degrees. HVE's *Roll*, *Pitch* and *Yaw*.

## Appearance

**Color** — the box's colour. **Wireframe** — draw the box as edges only.

!!! warning "Not in HVE 2027"
    - The **Global / Local** reference choice: positions and rotations are
      always in the scene frame.
    - **Bind to Object / Face / Vertex** and editing individual faces or
      vertices.
    - **Apply**: edits apply as you make them.

<!-- NAV -->

---

← Previous: [Environment](README.md)  |  [Index](README.md)  |  Next: [Cone Editor Dialog](ConeEdtDlg.md) →

<!-- /NAV -->
