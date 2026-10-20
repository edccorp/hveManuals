# Collision Pulse Options Dialog Box

The user may need to select a portion of the total pulse for use in a
simulation. For example, an entire left turn may last 3 seconds, while the
resulting collision with an oncoming vehicle lasts perhaps only 125
milliseconds. The pulse options also assign the impulse center for an impulse
(force/moment) pulse.

!!! note "HVE Studio"
    There is no separate options dialog: these fields are in the
    [Collision Pulse](ColPulse.md) dialog (**Event › Collision Pulse...**),
    below **Pulse type**. Edits take effect immediately.

## Start time (s)

When the pulse is applied, in the occupant run's own time base (HVE's
*Tstart*).

## Threshold (g)

The minimum resultant acceleration for a sample to be treated as part of the
crash (HVE's *Threshold Accel*). It is an acceleration whatever the pulse type,
so it stays in g.

## Impulse centre X / Y / Z

Shown only when the pulse type is **Impulse**, because no other type reads it.
The point where the force acts, measured from the CG in the vehicle's own frame
(x forward, y right, z down), in the units set in Preferences. SIMON takes the
moment of the table's force about this point, so it decides how much yaw a purely
translational pulse produces; all zero applies the force through the CG, which
produces no yaw from a forward or lateral force.

!!! warning "Not in HVE Studio"
    HVE's **OK** / **Cancel**, and the reset of these options to zero by
    **New**. **Clear pulse** empties the table only.

<!-- NAV -->

---

← Previous: [Collision Pulse In-Use Factors Dialog Box](ColPulFact.md)  |  [Index](README.md)  |  Next: [Collision Pulse](ColPulse.md) →

<!-- /NAV -->
