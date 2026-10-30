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

**The mesh's own wheels.** A motorcycle mesh that models its wheels (the
generic machine's `MCYamaha650.h3d` names them FTIRE and RTIRE) has them found
and turned with the run: they steer, roll and lean with the solved wheel, and
no second wheel is drawn over them. Where a mesh's wheels cannot be separated
from its frame -- no part is named for a tire, or the whole machine is one
shape, as in `06.106209_Motorcycle.h3d` -- they are drawn fixed to the body and
do not turn. The Vehicle Mesh dialog says which, under **Draw wheels (tire
radius)**; tick it for drawn wheels that turn.

**Tire forces.** The tire channels (Tire Fx', Fy', Fz') and the viewport's tire force
vectors show the forces of the model that carries the machine, on its one wheel per
axle (the other half of the pair reads zero), and each vector starts at that tire's
contact on the drawn wheel. The Nonlinear model's are its tires'. The
Whipple model has rolling contacts rather than tires, so its are derived from its motion:
the load is the weight with the transfer of the machine's own braking or acceleration,
the side force is what the turn needs (split between the wheels by the yaw
acceleration), and the braking force is split by the brake balance. They are the forces
the motion needs, to first order, not a tire model's output. The rest of each wheel's
channels come from the same model: aligning moment, loaded radius, tire deflection, slip
ratio and angle, inclination, skid flag, friction factor, and drive and brake torque (for
the Whipple model, those of a rolling contact with no slip: the unloaded radius, no
deflection, the lean as the inclination). The suspension channels read zero, because the
model's machine is rigid. In a SIMON event this holds while the single-track model carries
the machine; after a hand-back the channels are SIMON's own again.

**The case's CG is the machine's.** The CG position and height entered for a motorcycle are the whole
machine's, rider included, and the model places its four bodies so their combined CG is exactly there. A
SINGLETRACK run's positions and its rest position are the CG's.

**The rider.** Both single-track models ride with the same rider: a regulator
designed from the machine's own equations at each speed, which sees the lean,
the steer, both rates and the torque already in the rider's arms, and reacts
through a 0.1 s lag. It holds the machine upright and holds a commanded lean
from walking pace (2 m/s) up, on the motorcycle and on a bicycle; a commanded
lean the machine can hold is held to within about a degree on the nonlinear
model, where the friction in the steering head leaves a small, steady
oscillation. Below 0.5 m/s no rider balances a machine on its wheels, and the
model does not try.

**Crush stiffness.** The generic motorcycle carries the passenger car's crush
coefficients, the only generic values there are; its 3-D (DyMESH) stiffness
is derived from them as HVE derives a vehicle's that states none (the 2-D
A and B over a 30 in reference height). Replace both with measured values for
a motorcycle where you have them.

## Which method to use

| Method | What a motorcycle is there | Use it for |
| --- | --- | --- |
| **EDCRASH, EDSMAC, EDSMAC4** | A narrow rigid body with two contact patches. These are planar, so lean never arises. | Impacts: impulse-momentum through the collision, then the post-impact slide. This is how most motorcycle reconstructions are done. |
| **SIMON** | By default (**Dynamics model: Nonlinear**, below) the nonlinear single-track model owns the motorcycle for the whole run. With **Dynamics model: Whipple** (and in a case saved before that setting existed) a motorcycle rides the **single-track model** from the start of the event until its first contact, then SIMON and DyMESH take it over from the state the model left it in. Before contact you get the balance, countersteer and lean of the SINGLETRACK method, and the steer table is read the way the Event's single-track options say. The run status says when the machine was handed over (*handed to SIMON at first contact*) or why it was not (*stayed on SIMON's own model*, with the reason, for example steering geometry that is not a motorcycle's). **After** first contact the roll is held by a *rider-control surrogate* (a spring about the roll axis that pulls toward upright), and the run says so: *lateral results are low-lean only*. A roll stiffness you enter yourself replaces the surrogate. The motorcycle's one rider table is its **steer table**, read as a steer torque or a **commanded lean** by **Table means** (on the Driver Controls Steer tab, or under Motorcycle in SIMON Options), exactly as in SINGLETRACK: read as a lean, the rider holds it while the machine rides the single-track model, countersteering to reach it, and the machine turns. SIMON never reads a motorcycle's steer table as a steering angle: **after** first contact it steers straight ahead, has no forced lean angle, the surrogate holds the roll toward upright, and leaning does **not** steer the machine there. (A case saved with the separate **Lean** table of earlier versions has it moved into the SIMON event's steer table, read as a commanded lean, when it is opened.) The run status says which phases happened: a run with no contact says the table was the rider's lean command throughout; a run that meets something says it was the command until the hand-over and that SIMON read no lean after it. With **Dynamics model** set to **Nonlinear** in SIMON Options (Event Information › Method Options, shown when the event has a motorcycle), nothing is handed over: the nonlinear model owns the machine for the **whole run**, and SIMON and DyMESH compute the contact force and moment on the motorcycle's mesh at every step and hand them to the model as a **load**. The rider lets go at the first contact (or once the lean passes 70°), and a machine that goes down slides on its hard points at the machine drag factor; DyMESH's contact with the site is not used for the motorcycle. The run status says it *rode the nonlinear model the whole run*, from when the contact acted on it, for how many steps and at what peak force, when the rider let go, and when it went down, how far it slid and when it came to rest. A single-track wheel is one wheel: where a case gives a motorcycle DyMESH wheel meshes on both sides of an axle, the right side's is used and the run says so. | A motorcycle that rides up to an impact with a car or a barrier. The machine follows a site's terrain and can leave a ramp and land back on its tires before it makes contact; the run status gives the number of flights and the time airborne. A machine that goes down is handed to SIMON where it fell. |
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
    | Dynamics model | **Dynamics model** | **Nonlinear** is the default; a case saved before this setting existed keeps **Whipple**. **Whipple (linearized benchmark)** — the published model, exact for small lean. **Nonlinear (four-body, slip tires)** — the same bodies with nine rigid degrees of freedom and slip-based tires: lean exact at any angle, braking, load transfer and wheel lift solved; reads the throttle, the per-wheel and wheel force brake tables, the steering stops and each surface's friction; a fall slides on the machine's hard points to rest; in a SIMON event it owns the machine through the impact |
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
solved. A fall slides on the machine's hard points to rest instead of ending
the run, and in a SIMON event the nonlinear model owns the machine through the
impact.

- **It is linearized** about upright, straight running: exact for small lean.
  The run reports the peak lean, says so past 15°, and past 10° reports how far
  a linearized steer angle would be from the exact one. Use the
  [Motorcycle Analysis](08-analysis-tools.md#motorcycle-analysis) cornering
  calculator, which is exact at any lean, for real cornering.
- **No collision** in a SINGLETRACK event. A motorcycle impact goes through
  EDCRASH, EDSMAC or EDSMAC4, or through SIMON, where the nonlinear model rides
  the machine through it (above).
- **No tire slip model.** Braking is a deceleration limited by available
  friction, with load transfer and pitch-over; a locked-wheel slide is reported
  rather than simulated.
- **No wobble.** Front-end wobble needs frame flexibility this rigid model does
  not have; a run that stays upright here is not evidence a real machine would.
- **The bridge from the case is an assumption.** The case's mass, wheelbase, CG
  height, rake and tire radii are mapped onto the benchmark's four bodies using
  published class proportions. A lean result depends on them; measured values
  should replace them.
