# Chapter 4 — Calculation Method

In the original Fifth Edition manual this chapter was marked *(Reserved For Future Use)*.

> **NOTE:** See Reference 2 (Robbins, Bennett & Bowman, *User-Oriented Mathematical Crash Victim Simulator*, HSRI, University of Michigan) for the underlying calculation method — see [Chapter 7 — References](07-references.md).

## Summary of the method (from the current source code)

The following overview is derived from the current EDHIS physics source (`Physics/Source/Edhis/`), consistent with the model description in Chapters 1 and 2:

- **Human model** — A 3-mass (Head, Torso, Legs), 2-joint (Neck, Hip) rigid-body model with 12 degrees of freedom, derived from the HSRI-3D crash victim simulator. HVE's 15-segment human is condensed into the three EDHIS segments using the parallel axis theorem (`Hisinput.cpp`).
- **Contact forces** — Human segment ellipsoids are tested against vehicle planar contact surfaces each timestep; penetration produces a force from the linear/quadratic/cubic stiffness, damping, edge-constant and unloading-slope properties (`Contact.cpp`, `Fct.cpp`).
- **Joints** — Ball-and-socket joint torques are computed from linear elastic, damping and joint-stop elasticity properties (`Joint.cpp`).
- **Vehicle motion** — The vehicle is not dynamically simulated; its accelerations are interpolated from the user-supplied 6-DOF collision pulse and integrated for velocity and position (`Vehaccel.cpp`).
- **Numerical integration** — The equations of motion are integrated using a starter method (Euler, Runge-Kutta-Ralston "Modified Runge-Kutta" — the default — or classical Runge-Kutta) followed by a predictor-corrector method (Adams-Moulton or Milne-Hamming — the default), with timestep bisection to achieve velocity convergence (`Rk.cpp`, `Drkgs.cpp`, `Hismain.cpp`). See [Calculation Options for EDHIS](../../10-calculation-options/CalcOptionsEDHIS.md) for the user-selectable options and their internal variables.
- **Injury measures** — HIC, Chest Severity Index, chest force/acceleration, head pitch concussion, head side acceleration, femur load, joint over-rotation and belt loads are accumulated during the run and compared against the human's injury tolerances (`Output.cpp`, `Accel.cpp`).

---
*Previous: [Chapter 3 — Program Output](03-program-output.md) | Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md)*

<!-- NAV -->

---

← Previous: [Chapter 3 — EDHIS Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md) →

<!-- /NAV -->
