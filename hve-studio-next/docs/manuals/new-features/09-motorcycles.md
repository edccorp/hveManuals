# Motorcycles

!!! tip "New in HVE Studio"
    HVE Studio has a **Motorcycle** vehicle type, a generic motorcycle to start
    from, and a single-track engine, **SINGLETRACK**, that HVE does not have.
    The [Motorcycle Analysis](08-analysis-tools.md#motorcycle-analysis)
    calculators sit beside it.

## Adding a motorcycle

1. In the **Vehicle** editor, add a vehicle (or select one) and, in the
   **Vehicles** panel, set **Vehicle Type** to **Motorcycle**.
2. Changing the type to Motorcycle fills the vehicle with a class-typical
   mid-size machine plus rider: 200 kg + 80 kg, a 1.32 m wheelbase, a 0.60 m
   laden CG height, 25° rake, 120/70-17 front and 180/55-17 rear tires,
   telescopic forks and a swingarm, 1:1 steering (the bars are the steering).
   **Seed Generic Motorcycle** in the same panel does it again on demand.
3. Replace these figures with the real machine's data before anything that
   matters. They are published class figures, not a measured motorcycle.

The same machine is in the generic database, `Generic.hvedb`, as **Generic
Motorcycle (seeded)**: **Add...** finds it (the **Generics** button lists it with
HVE's generic vehicles), and it is also among the built-in vehicles that need no
database.

A motorcycle always has two axles. The generic machine is drawn with a real
motorcycle mesh (`MCYamaha650.h3d`), which is stored inside `Generic.hvedb` (and
in EDC's `EDCVehicles.hvedb`, where it is not licensed data), so it draws on
every computer without a separate mesh file. Where neither database nor the
file is installed it falls back to the generated body, with a warning.

**Drawn as one wheel per axle.** HVE's engines model every axle with two
wheels. For a motorcycle HVE Studio sets the two wheels of an axle side by side
across the tire's own width, so they act as one centerline contact patch, and
the viewport, the glTF export and the Blender link draw **one** wheel per axle,
on the centerline. In a lean the high-side wheel of the pair lifts off and the
low side carries the machine, so the viewport draws the wheel where the loaded
side is (the two sides weighted by their tire loads), and the tire sits on the
road. While a SIMON motorcycle rides the single-track model (before its first
contact) the wheel stays on the centerline, where that model puts it. This is
the same whether the run was solved in the app or by the separate solver
program (the default on Windows), and when a saved case is reopened with its
results. In the viewport the tire is drawn with the machine's crown
radius (a rounded tread), as the model uses it; the exports send plain
cylinders.

## Which method to use

| Method | What a motorcycle is there | Use it for |
| --- | --- | --- |
| **EDCRASH, EDSMAC, EDSMAC4** | A narrow rigid body with two contact patches. These are planar, so lean never arises. | Impacts: impulse-momentum through the collision, then the post-impact slide. This is how most motorcycle reconstructions are done. |
| **SIMON** | A motorcycle rides the **single-track model** from the start of the event until its first contact, then SIMON and DyMESH take it over from the state the model left it in. Before contact you get the balance, countersteer and lean of the SINGLETRACK method, and the steer table is read the way the Event's single-track options say. The run status says when the machine was handed over (*handed to SIMON at first contact*) or why it was not (*stayed on SIMON's own model*, with the reason, for example steering geometry that is not a motorcycle's). **After** first contact the roll is held by a *rider-control surrogate* (a spring about the roll axis that pulls toward upright), and the run says so: *lateral results are low-lean only*. A roll stiffness you enter yourself replaces the surrogate. With **Use the Lean table as the rider's lean command** (Event › Driver Controls, Lean tab), the rider holds the table's lean while the machine rides the single-track model: the rider countersteers to reach it and the machine turns, as in SINGLETRACK. **After** first contact SIMON reads no lean table (it has no forced lean angle); the surrogate holds the roll toward upright and leaning does **not** steer the machine there. The run status says which phases happened: a run with no contact says the table was the rider's lean command throughout; a run that meets something says it was the command until the hand-over and that SIMON read no lean after it. | A motorcycle that rides up to an impact with a car or a barrier. The machine follows a site's terrain and can leave a ramp and land back on its tires before it makes contact; the run status gives the number of flights and the time airborne. A machine that goes down is handed to SIMON where it fell. |
| **SINGLETRACK** | A real single-track model (below) | A machine on its wheels: balance, countersteer, braking, lean |

None of the HVE methods models lean, countersteer, gyroscopic effects, camber
thrust at large lean, the rider as a separate body, or a fall.

## The SINGLETRACK method

SINGLETRACK is the **Whipple bicycle model** in the published benchmark form
(Meijaard, Papadopoulos, Ruina and Schwab, *Linearized dynamics equations for
the balance and steer of a bicycle: a benchmark and review*, Proc. R. Soc. A
463, 2007): lean and steer coupled, with countersteer, gyroscopic precession and
the self-aligning effect of trail. Its core reproduces the benchmark's published
coefficients and self-stable speed range (4.29–6.02 m/s).

### Running it

1.  Make an event with **Calculation Method** SINGLETRACK in Event Information,
    with **one** Motorcycle-type vehicle.
2.  Press **Method Options...** in Event Information. The **SINGLETRACK Options**
    window holds:

    | Section | Field | Meaning |
    | --- | --- | --- |
    | Dynamics model | **Dynamics model** | **Whipple (linearized benchmark)** — the published model, exact for small lean. **Nonlinear (four-body, slip tires)** — the same bodies with nine rigid degrees of freedom and slip-based tires: lean exact at any angle, braking, load transfer and wheel lift solved; reads the throttle, the per-wheel and wheel force brake tables, the steering stops and each surface's friction; no hard-point ground contact yet |
    | Steer table | **Table means** | **Steer torque (N.m)** — what the rider's arms apply; the machine finds its own lean (a torque pulse is fought back upright, so use it for a disturbance, not a corner). **Commanded lean (deg)** — what the machine ended up doing; the rider countersteers to establish and hold it. Use this when the evidence is a lean angle, which is usual. |
    | Machine | **Steering damper (N.m.s/rad)** | 0 = none fitted |
    | | **Tire crown radius** | Negative = derive it from the front tire's width. At lean the contact point moves inboard round the rounded tread, so the machine leans several degrees further than the textbook angle |
    | Braking | **Front brake fraction** | Negative = the ideal split for the machine and surface; 0 = rear only; 1 = front only. The run reports whether friction or pitch-over limited the braking |
    | After a fall | **Machine drag factor**, **Rider drag factor** | The slide of each to rest if the machine goes down. Left at zero, no slide is computed |

3.  Enter the steer table in Driver Controls — as a **torque** or a **lean
    angle**, as chosen above. A steer **angle** cannot be prescribed: it would
    over-constrain the machine and remove the countersteer the model exists to
    capture. Every run says what the steer table meant.

### What it does not do

The limits below are the Whipple model's. With **Dynamics model** set to
**Nonlinear**, the first and third no longer apply: lean is exact at any angle
and braking goes through slip-based tires, with load transfer and wheel lift
solved. The nonlinear model has no hard-point ground contact yet, so a fall
still ends the run, and a motorcycle in a SIMON event still rides the Whipple
model.

- **It is linearized** about upright, straight running: exact for small lean.
  The run reports the peak lean, says so past 15°, and past 10° reports how far
  a linearized steer angle would be from the exact one. Use the
  [Motorcycle Analysis](08-analysis-tools.md#motorcycle-analysis) cornering
  calculator, which is exact at any lean, for real cornering.
- **No collision.** A motorcycle impact still goes through EDCRASH, EDSMAC or
  EDSMAC4.
- **No tire slip model.** Braking is a deceleration limited by available
  friction, with load transfer and pitch-over; a locked-wheel slide is reported
  rather than simulated.
- **No wobble.** Front-end wobble needs frame flexibility this rigid model does
  not have; a run that stays upright here is not evidence a real machine would.
- **The bridge from the case is an assumption.** The case's mass, wheelbase, CG
  height, rake and tire radii are mapped onto the benchmark's four bodies using
  published class proportions. A lean result depends on them; measured values
  should replace them.
