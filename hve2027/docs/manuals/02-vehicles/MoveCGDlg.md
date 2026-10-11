# Moving CG

**Move CG**

The default CG (center of gravity) location of the vehicle is determined from raw data (e.g., measured or table values). HVE's Move CG dialog moves the CG relative to the vehicle's 3-D geometry. HVE 2027 has two places that do related jobs.

## Move CG in the Vehicle Mesh dialog

Open **Vehicle › Vehicle Mesh...** in the Vehicle Editor (also on the Event menu). In the section **Move, Rotate and Scale the Model**, the row **Move CG** holds three values, X, Y and Z, in the units set in Preferences. They state where the CG sits in the geometry file's own coordinates, in the SAE vehicle frame (+x forward, +y right, +z down). The body is drawn displaced from the CG by this amount, so that the wheels and the bodywork line up. This is the value HVE's Move CG dialog stores, and it is read from an HVE case when one is opened. It moves the drawn body and the body mesh used for DyMESH contact together; it does not change the vehicle's dimensions or inertias.

The same section holds **Translate**, **Rotate (deg)** and **Scale** (per axis), which are HVE's Transform Geometry. They are applied as scale, then rotate, then translate, inside the Move CG shift, which is HVE's own order.

## Move CG dialog (EDSMAC and EDSMAC4 events)

In the Event Editor, when the active event's method is EDSMAC or EDSMAC4, **Event › Move CG...** opens a small **Move CG** dialog. The same dialog is reached from the **Move CG...** button of the **Crush & Geometry** window (**Event › Crush Profile...**, for EDCRASH, EDSMAC and EDSMAC4 events). It moves the CG relative to the body, as HVE's Move CG does: the body, the wheels, the contact surfaces, the belt and airbag anchors, the connections, the payload, the accelerometers and the occupants' seats stay where they are, and only the CG moves. Every distance measured from the CG changes to match.

### dX (+forward), dY (+right), dZ (+down)
How far to move the CG, in the units set in Preferences, in the SAE vehicle frame: +x forward, +y right, +z down. The CG-to-axle distances change by dX (the wheelbase does not), the CG-to-side distances by dY, and the CG height by dZ. A lateral move gives every wheel its own Y, since the track width alone can only describe wheels symmetric about the CG.

### CG Height
Read-only: the vehicle's CG height after the pending dZ. A move that would put the CG at or below the ground is refused with a note in the dialog.

### Apply
Makes the move and clears the three fields, so pressing Apply again does nothing until new values are entered. The dialog has no OK or Cancel; close it with the window's close button.

!!! note "HVE 2027"
    - HVE's dialog shows the CG's total offset from its original location; HVE 2027's fields are the move still to be applied.
    - The move is on the sprung-mass basis, which is how HVE 2027 stores the CG location. HVE displays the offsets on the sprung-mass or total-mass basis according to the Vehicle Dimensions Basis preference; HVE 2027 has no such preference (the Vehicles panel shows both bases side by side). The preference never changes a result: the engines overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

<!-- NAV -->

---

← Previous: [Inertia Dialog Box](InertiasDlg.md)  |  [Index](README.md)  |  Next: [Payload Dialog Box](PayLoadDlg.md) →

<!-- /NAV -->
