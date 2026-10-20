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

## Differential

A second table, *Time (s) → Ratio*, for a vehicle with a multi-speed
differential (**Gears** in the Drivetrain dialog's Differential section). Each
row selects **High**, **Medium** or **Low** (the choices follow the vehicle's
number of speeds); with a 1-speed differential the column reads High and a note
says the schedule reaches nothing new. **Add** appends a row one second after
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
