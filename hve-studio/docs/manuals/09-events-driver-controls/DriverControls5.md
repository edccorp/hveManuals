# Driver Controls Gear

Applies gear selections that change the current transmission ratio, and range
shifts that change the current differential ratio.

The **Gear** tab of the [Driver Controls](DriverControls.md) dialog
(**Event › Driver Controls...**). For a SINGLETRACK event the tab is labelled
*(not read)*.

## Gear table

A table of *Time (s) → Gear*, one row per gear selection. Each row's gear is
chosen from the gears of the vehicle's transmission: **Neutral**, **Reverse**,
then **1st**, **2nd**, … up to its number of forward gears. A stored gear the
transmission does not have is shown as *(not in this transmission)*. The gears
are numbered:

| Value | Selection |
|---|---|
| 0 | Neutral |
| 1 | Reverse |
| 2 | 1st gear |
| 3 | 2nd gear |
| ... | and so on |

**Add** appends a row one second after the last, in the last row's gear (first gear on an empty table); choose its gear in the row.
**X** deletes a row (the last row cannot be deleted). Up to 32 rows.

### An automatic transmission in a SIMON event

For a vehicle whose transmission is automatic (Drivetrain › Transmission), the
table's second column is **Selector**: each row puts the selector in **Drive**,
**Neutral** or **Reverse** from its time on, so an automatic can be shifted
into Neutral (or Reverse) during the run and back into Drive later.

- **Drive** — the transmission picks its own gear on the vehicle's shift
  points. At the start of the run SIMON chooses the starting gear from the
  vehicle's speed (the gear that puts the engine about halfway through its
  speed range). Coming back into Drive from Neutral or Reverse, it starts in
  first and shifts up. A row in an older case that names a forward gear above
  first reads *Drive (enters in 3rd)*, for example: that is the gear Drive
  re-enters in.
- **Neutral** — no drive torque reaches the wheels.
- **Reverse** — the reverse ratio.

A Drive row while the vehicle is already in Drive changes nothing; the shift
points decide. All of this applies only under the **At Driver** throttle
method; under % of Friction the engine is not used and the selector makes no
difference. EDVDS and EDVSM have no automatic model and run every
transmission as a manual, so in their events the column is **Gear** and each
row is the gear itself.

## Differential

A second table, *Time (s) → Ratio*, for a vehicle with a multi-speed
differential (**Gears** in the Drivetrain dialog's Differential section), such
as a truck's two-speed rear axle. Each row selects **High**, **Medium** or
**Low** (the choices follow the vehicle's number of speeds). For a vehicle with
a 1-speed differential — every car — the section is not shown; if such a case
already holds rows, they are shown with a note that they reach nothing new. **Add** appends a row one second after
the last (High); **X** deletes a row. Up to 10 rows, HVE's limit. With no rows
the engines use High for the whole run.

A schedule whose first row is after 0 s leaves the differential ratio at
**zero** before it (no drive torque), as in HVE. SIMON and EDVDS read the
schedule.

!!! note "HVE Studio"
    HVE Studio names the gears *Neutral*, *Reverse*, *1st*, … rather than HVE's
    *Shift into ...*, and offers numbered forward gears whatever the
    transmission type. Rows are not sorted or checked for duplicate times
    automatically.

!!! warning "Not in HVE Studio"
    - The **No of Shifts** field (rows are added and deleted directly).

<!-- NAV -->

---

← Previous: [Driver Controls Throttle](DriverControls4.md)  |  [Index](README.md)  |  Next: [Driver Controls Filter](DriverControls6.md) →

<!-- /NAV -->
