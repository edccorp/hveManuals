# Collision Pulse In-Use Factors Dialog Box

It may be useful to study the sensitivity of the occupant motion to changes in
the magnitude of the collision pulse. The in-use factors assign a multiplier to
each degree of freedom.

!!! note "HVE 2027"
    There is no separate factors dialog: the factors are under the
    **Scale factors** node of the [Collision Pulse](ColPulse.md) dialog
    (**Event › Collision Pulse...**). Edits take effect immediately.

Each column of the pulse table is multiplied by its factor before the engine
sees it. 1 leaves it alone (the default). Values from −100 to 100 can be entered
(HVE's dialog allowed 0.0 to 2.0).

- **Forward** — multiplier on the forward component of the vehicle's linear
  motion.
- **Lateral** — multiplier on the lateral component.
- **Vertical** — multiplier on the vertical component.
- **Roll** — multiplier on the roll component.
- **Pitch** — multiplier on the pitch component.
- **Yaw** — multiplier on the yaw component.

!!! warning "Not in HVE 2027"
    HVE's **OK** / **Cancel**, and the reset of the factors to 1.0 by **New**.
    **Clear pulse** leaves the factors as they are.

<!-- NAV -->

---

← Previous: [Accident History](AcciHistDlg.md)  |  [Index](README.md)  |  Next: [Collision Pulse Options Dialog Box](ColPulOptDlg.md) →

<!-- /NAV -->
