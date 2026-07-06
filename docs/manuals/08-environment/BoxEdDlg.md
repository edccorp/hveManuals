# Box Editor Dialog

The Box Object Tool allows the user to create and edit 3-D boxes. Boxes are useful for creating buildings, sidewalks, curbs and other box-shaped objects. The Box Editor dialog displays information about the current Box object.

The dialog is divided into a position/orientation group on the left and a shape group on the right. Position labels display the units for the current unit system (e.g. ft, deg); the labels are refreshed from the language/units resources whenever the dialog is activated, so changing the unit options updates the displayed units. Values typed into the dialog are applied to the selected box when the Apply button is pressed (pressing Enter is equivalent to Apply).

## Coordinates X

Displays and allows editing of the selected object's local or global X coordinate.

## Coordinates Y

Displays and allows editing of the selected object's local or global Y coordinate.

## Coordinates Z

Displays and allows editing of the selected object's local or global Z coordinate.

## Roll

Displays and allows editing of the selected object's local or global Roll orientation (degrees).

## Pitch

Displays and allows editing of the selected object's local or global Pitch orientation (degrees).

## Yaw

Displays and allows editing of the selected object's local or global Yaw orientation (degrees).

## Global/Local

Combo box selecting whether the coordinate and angle values are displayed and entered in the Global (world) reference frame or the box's Local reference frame. Options: *Global*, *Local*. Default: *Global*.

## Width

Allows the user to edit the box's base width in the local y' direction.

## Height

Allows the user to edit the box's height in the local z' direction.

**Note:** On Apply, the box height is not applied from this field. The height is forced equal to the **Length** value (`height = m_txtLength`, BoxEditorDlg.cpp:585–604), so the box always renders with its height equal to its length. The Height field value entered here is not independently applied.

## Length

Allows the user to edit the box's length in the local x' direction.

## Bind to

Radio buttons selecting what the coordinate fields are bound to when picking and editing:

- **Object** — the box as a whole (default).
- **Face** — an individual face of the box.
- **Vertex** — an individual vertex.

## Apply

Applies the values in the dialog to the selected box and registers the change with the undo/redo system, so the edit can be undone or redone. Pressing Enter (OK) also applies; pressing Esc (Cancel) is ignored — the dialog remains open.

---
*Source topic: BoxEdDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Environment](README.md)  |  [Index](README.md)  |  Next: [Cone Editor Dialog](ConeEdtDlg.md) →

<!-- /NAV -->
