# Simulation Controls Dialog Box

This dialog displays and allows editing of all simulation control data for the current event. Each value is entered with a slider or by typing directly into the associated edit field.

## Integration Timesteps

Integration timesteps define the discrete timestep used by the simulation and are dependent on the purpose and type of the simulation.

- **Human Collisions (sec)** — Integration timestep used during the collision phase for occupant and pedestrian simulations.
- **Vehicle Collisions (sec)** — Integration timestep used during the collision phase for vehicle simulations.
- **Curb Impact (sec)** — Integration timestep used during curb impact for vehicle simulations.
- **Vehicle Separation (sec)** — Integration timestep used during the initial portion of the post-impact phase for vehicle simulations.
- **Vehicle Trajectory (sec)** — Integration timestep used for vehicle trajectory simulations.
- **Output Time Interval (sec)** — Event time output interval.

## Termination Conditions

Termination conditions are used to define when the simulation terminates. Termination linear and angular velocities are natural termination conditions which define when a simulated object has stopped moving.

- **Maximum Time (sec)** — Maximum simulation time.
- **Linear Velocity (mph)** — Minimum linear velocity; event termination may result if the current linear velocity is less than this value.
- **Angular Velocity (deg/sec)** — Minimum angular velocity; event termination may result if the current angular velocity is less than this value.
- **Maximum Bisections** — Maximum number of times the integration timestep may be halved.
- **Velocity Convergence** — Allowable error between predicted and actual integration results.
- **Velocity Change Limit** — Maximum allowable change in velocity during one timestep.
- **Acceleration Change Limit** — Maximum allowable change in acceleration during one timestep.

---
*Source topic: SimuCtrlDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Position/Velocity Dialog Box](PosVelDlg.md)  |  [Index](README.md)

<!-- /NAV -->
