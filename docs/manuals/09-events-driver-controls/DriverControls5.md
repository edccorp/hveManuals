# Driver Controls Gear

Applies gear selections that change the current transmission or differential ratio.

The Gear Selection page is available for simulations. This page allows the user to enter a table of gear selection versus time. Separate tables may be entered for the transmission and the differential.

This page enables the user to enter data for the following items.

## Table

Selects which gear selector table is being edited:

- **Transmission** — gear shift table for the vehicle's transmission.
- **Differential** — range shift table for the vehicle's differential. This choice is available only if the vehicle's differential has more than one ratio.

## No of Shifts

Specifies the number of gear shifts in the current table (0 to 10).

## Time (sec)

Time associated with each gear shift. On leaving the page, the entries are automatically sorted into ascending time order; duplicate shift times are reported as an error.

## Gear Selection

The gear selected at each shift time. For the transmission table the available choices depend on the vehicle's transmission type:

- Automatic transmission: *Shift into Neutral*, *Shift into Reverse*, *Shift into Drive*.
- Manual transmission: *Shift into Neutral*, *Shift into Reverse*, and a numbered gear (*Shift into 1st*, *Shift into 2nd*, *Shift into 3rd*, ...) for each forward gear defined for the transmission.

For the differential table the choices are the ratios (ranges) defined for the vehicle's differential.

---
*Source topic: DriverControls5.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Throttle](DriverControls4.md)  |  [Index](README.md)  |  Next: [Driver Controls Filter](DriverControls6.md) →

<!-- /NAV -->
