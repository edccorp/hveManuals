# Variable Output Edit Dialog

In HVE the developer of a simulation model could make certain non-calculated
results editable by the user — for example, a 2-D simulation could let the user
edit the sprung mass Z position and roll and pitch orientations, to create a 3-D
sequence from a 2-D program. HVE's **Edit...** button in the Variable Output
window opened a grid of those variables.

!!! warning "Not in HVE 2027"
    Output variables cannot be edited in HVE 2027; there is no **Edit...**
    button and no edit grid. A solved event's results are exactly what the
    engine computed.

    What HVE 2027 does instead for the 2-D programs: EDSMAC, EDSMAC4 and EDSVS
    settle the vehicle onto the terrain at every step and publish its real
    elevation, roll and pitch, so the vehicles are drawn following the ground
    without editing the output.

<!-- NAV -->

---

← Previous: [Trajectory Report](TrajRepDlg.md)  |  [Index](README.md)  |  Next: [Variable Output: Graph Dialog](VarOutGraphDlg.md) →

<!-- /NAV -->
