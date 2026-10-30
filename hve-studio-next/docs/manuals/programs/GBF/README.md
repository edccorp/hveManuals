# GBF — Air-Brake Stopping Calculator

*HVE's "Graphical Brake Forces" program, version 2.20, for heavy trucks with S-cam air brakes. HVE Studio runs it as the **GBF** calculation method. (New in HVE Studio: GBF's source was part of HVE, but no saved HVE case runs it, and this port ran it for the first time.)*

## What GBF does

GBF estimates how a truck, alone or with trailers, stops on air brakes. It is a calculation, not a trajectory simulation: the units travel in a straight line along their initial heading. For each brake, GBF works out:

1. **The push-rod force.** It reads its push-rod force table for the brake's chamber type at the stroke the push rod reaches and at the chamber pressure. The table is built in for Types 9, 12, 16, 20, 24, 30 and 36, standard and long stroke. The stroke is:
    - the push rod's **measured stroke** (at 90 psi);
    - plus the growth from a **hot drum**, above 300 °F;
    - plus a **dynamic** growth that increases through the stop.
2. **The brake force at the road.** It turns the push-rod force into a force at the tire through:
    - the slack-adjuster length;
    - a lining friction of 0.35;
    - the drum radius;
    - the cam radius;
    - the loaded tire radius;
    - an efficiency of 0.6.
3. **What the tire can take.** It limits that force to the tire's sliding friction times the wheel's load. The friction is scaled by the surface under the truck. A wheel that would exceed it **locks** and slides at that limit.

The deceleration is the sum of the wheel forces over the total weight. For the first half second, GBF applies half the deceleration it finds at 0.5 s. After that it steps the stop forward at the calculation interval until the speed reaches the termination speed.

The axle loads come from the units' weights, payloads, axle positions and connections. Each towed unit's kingpin load passes to the unit ahead. Weight transfer during braking is not modeled.

## Setting up a GBF event

1. **Vehicles.** The first unit must be a **Truck**. Each unit behind it must be a **Truck**, **Trailer** or **Dolly**, connected as in any multi-unit case. A power unit needs at least two axles, and a towed unit one.
2. **Brakes** (Vehicle > Brakes > **Brake Assembly** and the **Brake Designer**). Every brake must be an **S-Cam**. Its **Air Chamber** must be a type GBF's table has (9, 12, 16, 20, 24, 30 or 36). Type 18 is offered by the Brake Designer, but GBF has no data for it. GBF also reads each brake's:
    - slack-adjuster length;
    - cam radius;
    - drum diameter;
    - maximum stroke, which selects the long-stroke table above 2.0 in for a Type 12, 2.376 in for Types 16–24, and 2.76 in for a Type 30.
3. **The measured strokes** (Event > **Wheels...** > Brakes: **Initial stroke**, one per wheel). GBF reads the table at this stroke, so a stroke of 0 is refused. **Initial rotor/drum temp** is the drum temperature; above 300 °F it lengthens the stroke.
4. **Position and speed** (Event > **Position / Velocity...**): where the truck starts and how fast.
5. **GBF's own inputs**, on the **Event Information** panel under the method:
    - **Chamber pressure**: the air pressure at every brake chamber of every unit. A full application is about 100 psi. GBF's table covers 10–110 psi, and a value outside 0–110 psi is refused.
    - **Antilock (simple ABS)**: holds each brake **Pressure drop** below the pressure that would lock its wheel, so no wheel locks.
    - **Find the initial speed**: GBF finds the initial speed that stops the truck in the **Stopping distance** given, and the speed on **Position / Velocity** is not used. When this is off, GBF starts from the initial speed and finds the distance.
6. **Payload** (Event > **Payload...**): GBF reads each unit's payload weight and fore-aft position.

A setup GBF cannot run is refused before the run, with the reason and the dialog that fixes it in the run status. This covers a first unit that is not a Truck, a brake that is not an S-Cam, a chamber GBF has no data for, a brake with no measured stroke, and a pressure outside the table.

## What GBF reports

- **The run status** gives the answer, for example: *initial speed found 72.3 km/h (44.9 mph): 41.20 m in 3.912 s*. If the truck had not stopped when the run ended, or if the speed search did not converge, the status says so.
- **Channels:**
    - **Kinematics:** **Total Velocity**, **Long Vel (u)**, **Speedometer**, **Fwd Accel** and **Long Accel (udot)** (negative while braking), and **Distance Traveled**. The units move along their initial heading by that distance, so the 3-D view shows the stop.
    - **Wheels:** **% Avail Mu** (the share of the wheel's available friction in use, from 0 to 1), the attempted brake force, the brake stroke, the brake pressure, the push-rod force and the drum temperature.
    - **Tires:** the **Skid/Scuff** flag of a locked wheel.
- **Reports:** GBF's Accident History, Results (each brake's inputs and its state at the end of the run), Program Data, Messages and Vehicle Data pages.

## Changes from HVE's GBF

HVE's own GBF could not run as written: it opened its debug log at an unset path, and its surface query ended any run that had a road under the truck. HVE Studio's GBF has these corrections (recorded in `tests/data/port_divergences.tsv`):

- **Chamber pressure and antilock are event fields.** HVE read the chamber pressure from the first value of the brake pedal table and an antilock drop from a second row. An imported HVE GBF event keeps the 100 psi default until it is set; the import notes say so.
- **Every brake must be an S-Cam.** HVE ran any brake type through the S-cam's numbers.
- **The stop ends at the termination speed.** The last step is shortened to land on it, and each output record carries the state at its own time.
- **Finding the speed uses the whole stopping distance**, including the first half second; HVE left the first half second out. The search publishes one run. If it does not converge, it says so; HVE's search could loop forever.
- **The units move along their heading** as they stop, and **Distance Traveled** is published. HVE kept every record at the starting position.
- **Fwd Accel is negative** while braking. The skid flag is in the tire's Skid/Scuff slot. The attempted brake force is the attempted one. **% Avail Mu** is a fraction from 0 to 1, not a percentage.
- **The surface's friction applies.** HVE's query searched curbs only and dropped its result.
- **The average decelerations by time** divide by the actual elapsed times.

GBF has not been checked against a saved HVE run, because none exists. HVE Studio's checks of it (ctest `gbf`) are:

- the closed-form stop;
- distance against speed;
- the surface friction;
- the speed search reversing the forward run;
- the direction of each brake effect;
- antilock.

The frozen **HVE-reference** physics does not run GBF.
