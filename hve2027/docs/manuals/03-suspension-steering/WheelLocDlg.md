# Wheel Location Dialog

HVE edits each wheel's location in a Wheel Location dialog. In HVE 2027 the wheel locations are a table in the Vehicle Editor (**Vehicle (F3)**): in the **Vehicles** panel, open **Dimensions / Inertias › Wheel Positions (from CG)**. The table has one column per wheel (**A1 Right**, **A1 Left**, **A2 Right**, ...) and the coordinates are relative to the vehicle-fixed (SAE) coordinate system, in the units set in Preferences.

Each wheel's position is normally **derived** from the vehicle's dimensions (the CG-to-axle distances, axle spacings, track widths, CG height and tire radius). A field left at 0 shows the derived value, and its tooltip says *Derived. Type a value to override this wheel.* Typing a value overrides that one wheel; setting it back to 0 returns it to the derived value. The left and right wheels may differ.

This table contains the following parameters:

## X
The longitudinal distance from the vehicle CG to the wheel (positive forward). When a wheel carries its own X, the wheelbase and the CG-to-axle distances shown under **Overall** are derived from the wheels instead, and an orange note there says so.

## Y
The lateral distance from the vehicle CG to the wheel (positive toward the right side).

## Z below CG
The vertical distance from the vehicle CG to the wheel (positive downward).

If the left and right wheels of an axle are at different X positions, a note says how the event's calculation method treats it: EDSMAC and EDCRASH cannot represent the difference and average the two sides into one CG-to-axle distance, so the layout is solved as if symmetric; the other methods read each wheel's own X.

!!! warning "Not in HVE 2027"
    **Copy To Other Side**: each wheel is entered on its own (leave a field at 0 to keep it derived).

!!! tip "New in HVE 2027"
    Positions are derived from the vehicle's dimensions until overridden, and the asymmetry note for methods that cannot represent it.

<!-- NAV -->

---

← Previous: [Suspension Data Dialog](SuspDlg.md)  |  [Index](README.md)

<!-- /NAV -->
