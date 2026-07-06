# Payload Dialog Box

**Payload Dialog Box**

The Payload dialog allows the user to add a payload to the selected vehicle. The payload may be any object adding inertia to a vehicle that is not accounted for in the vehicle's inertial properties. Which payload fields may be edited depends on the physics options of the calculation method assigned to the current event; fields not supported by the current calculation method are disabled.

## Payload Exists
Check this box if the vehicle has a payload. When unchecked, all remaining fields are disabled and the payload is ignored.

## x
The X distance from the vehicle's center of gravity to the payload's center of gravity.

## y
The Y distance from the vehicle's center of gravity to the payload's center of gravity.

## z
The Z distance from the vehicle's center of gravity to the payload's center of gravity.

## Weight
The weight of the payload.

## Mass
The mass of the payload. This field is read-only; it is calculated as the entered weight divided by the current acceleration of gravity.

## Roll
The roll moment of inertia of the payload.

## Pitch
The pitch moment of inertia of the payload.

## Yaw
The yaw moment of inertia of the payload.

---
*Source topic: PayLoadDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Moving CG](MoveCGDlg.md)  |  [Index](README.md)  |  Next: [Sprung Mass Dialog](SprungMassDlg.md) →

<!-- /NAV -->
