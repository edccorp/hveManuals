# Tire Physical Data Dialog

The tire physical parameters for the selected wheel position are displayed and edited using the Tire Physical Data dialog (title: *Tire Physical Data: &lt;Mfr&gt; &lt;Model&gt; &lt;Size&gt;*). Each parameter may be set with a slider or typed directly into its edit field.

This dialog contains the following items (in dialog order):

## Unloaded Radius

Undeflected tire radius (no-load condition).

## Maximum Width

Maximum section width of the tire. This value is display-only; it is computed from the tire size designation string. (New since the original help.)

## Tread Width

Width of the tire tread contact patch. (New since the original help.)

## Tread Depth

Depth of the tire tread. (New since the original help.)

## Nominal Pressure

Nominal (rated) inflation pressure of the tire. (New since the original help.)

## Initial Deflection Rate

The initial tire spring rate (vertical tire load per unit of linear tire deflection).

## Secondary Deflection Rate

The spring rate under conditions of excessive tire vertical load.

## Deflection at Secondary Rate

Tire deflection at which the secondary deflection rate begins.

## Maximum Deflection

Tire maximum deflection. This value is normally used to terminate execution, indicating the probability of a damaged or broken wheel rim.

## Pneumatic Trail

Longitudinal distance from the center of the tire contact patch to the center of pressure. Pneumatic trail increases the self-aligning tendency of a steerable wheel.

## Aligning Torque Coef

Self-aligning torque coefficient due to mechanical and pneumatic trail.

## Weight

Total weight of the wheel assembly (tire plus rim). For an independent suspension, the value reflects the total unsprung mass. For a solid axle suspension system, the axle weight is added to the wheel weight to determine unsprung mass. The displayed weight is calculated from the stored tire mass.

## Spin Inertia

Tire rotational inertia about its spin axis.

## Steer Inertia

Tire rotational inertia about its steering axis.

## Rolling Resist Const

Tire rolling resistance constant force coefficient.

## Rolling Resist Linear

Tire rolling resistance linear, velocity-dependent force coefficient.

## Min Fz For Skidmark

Minimum vertical tire force required in order to cause a visible tire mark on the road.

## OK / Cancel

OK validates each entry against its allowed range and stores the physical data for the tire. Cancel discards all changes.

---
*Source topic: TirePhyDataDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Tire Information Dialog](TireInfoDlg.md)  |  [Index](README.md)  |  Next: [Tire Save As Dialog](TireSaveAsDlg.md) →

<!-- /NAV -->
