# Case Intake and Vehicle Data

!!! tip "New in HVE 2027"
    HVE has no counterpart for the tools on this page. They put what is known
    about a crash into the case (a vehicle's identity and measured
    specifications, who and what it carried, crash-test stiffness, an event
    data recorder's pre-crash record, the facts in the case documents) and
    record where every value they set came from.

| Tool | Where | What it changes in the case |
| --- | --- | --- |
| [Vehicle Package](#vehicle-package) | **Tools › Automatic Tools › Vehicle Package...** | Adds one vehicle; seats its occupants and loads its cargo in an event, or puts them aboard the vehicle |
| [Case Intake](#case-intake) | **Tools › Automatic Tools › Case Intake...** | Adds one event with new vehicles, their starting positions and speeds |
| [Provenance](#provenance) | **Tools › Automatic Tools › Provenance...** | Nothing in the physics: it lists, and can remove, the records the other tools keep |
| [Aboard](#aboard-occupants-and-cargo-on-the-vehicle) | **Inertia / Mass** dialog, *Aboard* section | The occupants and cargo a vehicle carries into every event |
| [Crush Stiffness from Crash Tests](#crush-stiffness-from-crash-tests) | **Tools › Automatic Tools › Crush Stiffness from Crash Tests...**, or **Vehicle › Crush Stiffness...**, button **From crash tests...** | One side's A and B, and the A and B of the vehicle's EDCRASH events |
| [EDR Import](#edr-import) | **Tools › Automatic Tools › EDR Import...** | An event vehicle's initial speed and its throttle, brake and steering tables |

These tools are in the workstation product. The viewer product (which opens a
published bundle) has none of them.

## Where each value came from

Every value these tools set is labelled with one of five kinds, in the tool's
own window and afterwards in **Tools › Automatic Tools › Provenance**:

| Kind | Means |
| --- | --- |
| **Stated** | You typed it, or a document you supplied states it |
| **Looked up** | Taken from a named source: a vehicle database record, NHTSA's VIN decoder, a spec sheet, an NHTSA crash test file, an EDR report |
| **Estimated** | Worked out by a named rule from named inputs, for example GEBOD's 50th-percentile body for an occupant whose weight nobody stated |
| **Generic default** | The generic vehicle's own value, which the tool could not replace with this vehicle's |
| **Unknown** | Nothing stated it. A placeholder stands in the case until you set it |

Nothing is guessed and then presented as a fact. A value no source states is
left out, estimated by a rule the sheet names, or entered as a placeholder
recorded as **Unknown**, and the window says which.

## Case documents stay on your computer

Case Intake, the spec-sheet reader in Vehicle Package and EDR Import read
documents through **your own AI tool**, not through HVE 2027:

1. Press the window's prompt button: **Copy prompt for your AI tool** in Case
   Intake and EDR Import, **Copy spec-sheet prompt** in Vehicle Package. The
   prompt goes to the clipboard. It tells the tool exactly what to return (one JSON object), to
   give every value with its place in the document, and to leave out anything
   the document does not state.
2. Give the prompt and the documents (a police report, a spec sheet, a CDR
   report) to the AI tool you use.
3. Paste its whole answer into the window's text box. Text around the answer,
   such as a sentence before it or code-fence marks, does no harm: the window
   reads from the first `{` to the last `}`.

HVE 2027 calls no AI service and sends nothing anywhere; the documents go only
where your own tool sends them. Vehicle Package has two network actions, each
only when you press it: **Decode with NHTSA (online)**, which sends the VIN
alone, and **Look up Canadian Vehicle Specifications (online)**, which sends the
year, make and model.

!!! warning "Check the answer"
    An AI tool can misread a document. Each window shows every value beside
    the citation the tool gave for it, so that it can be checked against the
    page it names before it goes into the case.

## Vehicle Package

**Tools › Automatic Tools › Vehicle Package...** builds a case vehicle from what is known about
it: its VIN or its year, make and model, its measured specifications, who was
in it and what it carried. It also keeps what is known about a vehicle that is
already in the case. Weights, lengths and positions are shown and typed in the
units set in Preferences.

The **Vehicle** list at the top of the window chooses what the window works on:

- **New vehicle (look it up and add it)** — the window is worked from top to
  bottom, in the five numbered sections below, and adds a new vehicle to the
  case.
- **A vehicle already in the case** — choosing it also selects it everywhere
  else. The window shows that vehicle's kept identity and specifications, and
  its sections are different; see
  [A vehicle already in the case](#a-vehicle-already-in-the-case).

Opening another case sets the list back to a new vehicle.

### 1. Identify

| Control | Does |
| --- | --- |
| **VIN** | The 17-character Vehicle Identification Number. Spaces and dashes are ignored |
| **Check** | Checks the VIN offline: 17 characters, none of them I, O or Q; the check digit in position 9, reported as *Check digit OK* or *Check digit does NOT match (expected ...)*; and the model year from position 10. If **Year** is empty, Check fills it in |
| **Decode with NHTSA (online)** | Sends the VIN to NHTSA's vPIC decoder and fills **Make**, **Model**, **Series**, **Trim** and **Year** from its answer, and **Type** when vPIC's body class names one plainly (a bus or an incomplete vehicle is not guessed). It also fills any specifications vPIC states (below). Enabled once the VIN is well formed; never automatic. The line under the buttons repeats vPIC's own message. Not available in the browser version |
| **Year**, **Make**, **Model**, **Series**, **Trim** | What the vehicle is. Type them, or correct what the decoder filled in |
| **Type** | The vehicle type. It picks the generic vehicle used when no database record is chosen |

The model-year code in position 10 repeats every 30 years. For a car,
multipurpose vehicle or light truck (GVWR up to 10,000 lb), position 7 settles
it: a digit there means 1980–2009, a letter 2010–2039 (49 CFR 565.15). Heavier
vehicles do not follow that rule, so the window shows both candidate years and
the rule it applied.

Two disagreements are reported in orange rather than left for you to notice:
a **Year** that is neither of the VIN's two candidate years, and a **Make**
that is not the make NHTSA decoded the VIN as.

### 2. Vehicle data

The vehicle databases are searched for the make and model. They are the same
databases the vehicle database dialog reads (**Add...** or **Replace...** on
the Vehicles panel; the folders searched are listed under its **Database
folders**; see [Adding New Vehicles](../hve-users/04-vehicle-editor/10-creating-editing-vehicles.md#adding-new-vehicles)).
If no database is loaded, the generic vehicle is the only choice and the
window says so.

The table lists the matching records, best first, with a **Generic** row at
the bottom. Click a row to choose it.

| Match | Means |
| --- | --- |
| **Exact** | Same make and model, and the year inside the record's years |
| **Same model, other years** | Same make and model, another generation (or a record that states no years), nearest years first |
| **Generic** | No record: HVE's generic vehicle of the chosen **Type** (the middle size class where HVE has several). Every value is the generic's, not this vehicle's |

Only records of the same make and model are offered. A similar vehicle of
another model is a judgment for you, and is never offered as a match.

- **Spelling.** *F-150* and *F150* match, and so do *Silverado* and
  *Silverado 1500* (one name is the other's leading words). *Caravan* does not
  match *Grand Caravan*.
- **Family names.** NHTSA names a model family (*C-Class*, *3-Series*,
  *Silverado*) and puts the designation in its series or trim (*C300*,
  *335i*, *1500*), while the databases use either. A record whose model
  matches the series or trim is offered too, and its **Why** column says so.
- **Ranking.** Exact before other years, then the nearest years, then the
  record whose name contains more of the series and trim words (a *Ram 1500*
  before the *2500* of the same years).

**Name in the case** is the new vehicle's name. Left empty, the vehicle keeps
the record's or the generic's own name.

### Stated specifications

Expand **Stated specifications** (under the name) to enter what is known about
the real vehicle. Leave a value at 0 when it is not known.

| Row | Is |
| --- | --- |
| **Weight** | The vehicle without occupants or cargo: its curb weight. It becomes the vehicle's total weight |
| **Front axle share (0-1, total)** | The fraction of the total weight on the front axle |
| **Wheelbase** | Front axle to rear axle |
| **Front track**, **Rear track** | Each axle's track width |
| **Length**, **Width**, **Height** | The overall dimensions |
| **CG height (total)** | The CG height of the whole vehicle (total-mass basis) |

Each row has its value, a **From** column (**Stated** for a value you typed,
**Looked up** for one filled from a source) and a **Source** box for where it
came from (a spec sheet, a weigh ticket, a measurement). Typing a value makes it
Stated. A line above the table says what the last fill did and what it could
not use. Four things can fill the rows:

- **Decode with NHTSA (online)** fills the curb weight, wheelbase and track
  width when vPIC states them for this VIN (it often does not for cars), into
  rows that are still empty. vPIC gives one track width, which is used for both
  axles. A model sold in two wheelbases gives a range, which is not used.
- **Look up Canadian Vehicle Specifications (online)** sends the year, make
  and model to NHTSA's vPIC, which serves Transport Canada's Canadian Vehicle
  Specifications, and lists one row per body and trim: weight, front share,
  wheelbase, front and rear track, length, width and height. Press **Use** on
  the row that is this vehicle. It fills the rows that are empty or were looked
  up; a value you typed is kept, and an implausible value is left out and
  named. The button needs the **Year**, **Make** and **Model**. If nothing is
  found, try a shorter model name: the table names models its own way.
- **NHTSA test file** box and **Load NHTSA test**: type the path of a test
  file from NHTSA's Vehicle Crash Test Database (see
  [Reading an NHTSA crash test file](#reading-an-nhtsa-crash-test-file)). The
  tested vehicle (the first with a model year, so a side test's impactor is
  passed over) fills **Weight** (its curb weight), **Wheelbase**, **Length**
  and **Width**, and **Front axle share** from its CG position at the test
  weight. The database's API states the CG's distance behind the front axle
  but no wheelbase, so for a file fetched from it the share needs the
  **Wheelbase** row filled first (stated, or from vPIC); the note says so when
  it is missing. Load the file again once it is filled.
- **Copy spec-sheet prompt**, the box under it, and **Read spec sheet**: give
  the prompt and the spec sheet (a manufacturer's sheet, a brochure, a Canadian
  Vehicle Specifications page) to your AI tool and paste its answer. Each value
  arrives with its unit and its place in the document, and the window converts
  inches, millimeters, centimeters, meters and feet, and pounds and kilograms.
  A front share may be given as a percentage, a fraction, or front and rear
  axle weights. A value in a unit the window does not know, or one that cannot
  be right for a road vehicle (a length of 189.5 m because the unit was
  misread), is left out and named.

The NHTSA test file and the spec sheet replace any row they give a value for;
the VIN decoder only fills empty rows.

**What stated specifications do.** A **database** vehicle keeps its own values:
the specifications are recorded as *not applied*, and reconciling them is left
to you. A **generic** vehicle is scaled to them. Each stated value sets:

| Stated | Sets |
| --- | --- |
| Weight | The total weight. A weight alone keeps the generic's front axle share |
| Front axle share, Wheelbase | The CG-to-axle distances (an unstated one keeps the generic's value) |
| Front track, Rear track | That axle's track |
| Length | The overall length |
| Width | The overall width, and both CG-to-side distances (the CG is taken on the centerline) |
| Height | The overall height; and, when the CG height is not stated, the CG height by EDC's equation (below) |
| CG height | The CG height of the whole vehicle |

and these move with them, each marked **Estimated** on the sheet with its rule:

- **Overhangs**: length minus wheelbase, split front and rear as the generic
  splits it. A stated wheelbase without a length keeps the generic's overhangs.
- **Wheel positions**: fore and aft with their axle, sideways with the track,
  and in height with the CG, which keeps the wheel-center height above the
  ground. **Hitch points** move with their end of the body, and in height with
  the CG. The **CG-to-underside** distance moves with the CG height, which
  keeps the ground clearance.
- **Inertias**: when the **Weight** is stated, the roll, pitch and yaw
  inertias come from the weight by EDC's equations (below), on the total-mass
  basis; the sprung inertias are those minus the vehicle's unsprung part. When
  the weight is not stated but the size changes, the sprung roll inertia scales
  with the sprung mass and the square of the mean track, and pitch and yaw with
  the sprung mass and the square of the wheelbase. (A generic that states no
  inertia has it estimated from the new mass and size.)
- **Suspension**: each axle's spring, damper and auxiliary roll stiffness scale
  with that axle's sprung static load, which keeps its ride frequency, damping
  ratio and roll gradient.

Tires, brakes, drivetrain and aerodynamics stay the generic's, and the sheet
says so.

**EDC's equations.** Two of the rules above are EDC's equations, in inches,
pounds and lb-s²-in, with W the vehicle's weight in pounds:

| Value | Equation |
| --- | --- |
| CG height (total), when only the overall height H is stated | 0.3674 × H^1.0154 |
| Roll inertia (total) | 0.0783 × W^1.3629 |
| Pitch inertia (total) | 0.0711 × W^1.5637 |
| Yaw inertia (total) | 0.1291 × W^1.4942 |

The sheet shows each one with the numbers it used.

A generic is **not** scaled, and the specifications are recorded as not
applied with the reason, when:

- it has a body mesh file (the motorcycle generic) or a display mesh, which
  would not follow new dimensions;
- it is not a two-axle powered vehicle (a trailer or dolly, a barrier, a
  motorcycle, or a vehicle with more than two axles): a tandem's or a
  trailer's wheelbase is not one number;
- it states an explicit axle position, which would override the wheelbase;
- the specifications cannot describe one vehicle: a length not longer than
  the wheelbase, a CG at or above the overall height, a width not wider than
  the track, a front share outside 0 to 1, or a value that is zero or negative.

The vehicle is still added, as the unscaled generic.

### 3. Occupants

One row per person. **Add occupant** adds a row (the first in the driver's
seat, the next in the front right seat); **Remove** deletes one. Leave a value
at 0 when it is not known.

| Column | Is |
| --- | --- |
| **Seat** | One of the nine seats: Front Right, Front Center, Front Left (driver), Rear Right, Rear Center, Rear Left, Back Right, Back Center, Back Left |
| **Sex** | Not stated, Male or Female |
| **Age (yr)** | The occupant's age |
| **Weight**, **Height** | As stated |
| **Seat pos?** | Tick when the seat position is known |
| **x / y / z** | The seat position from the vehicle CG: x forward, y right, **z down** |

Each occupant is given a GEBOD body. A stated weight, height or age goes to
GEBOD as given. A weight or height left at 0 is GEBOD's 50th percentile for the
sex, marked **Estimated**. A sex not stated gives a male body, an age not
stated an adult, both marked Estimated. A stated age under 18 builds GEBOD's
body for that age. The occupant is named *Driver* in the driver's seat, and
after the seat otherwise.

### 4. Cargo

One row per item: **Item** (a name), **Weight**, and **x / y / z**, its
position from the vehicle CG, x forward, y right, **z up** (the payload's
frame, as in the [Payload dialog](../02-vehicles/PayLoadDlg.md)).
**Add cargo item** adds a row and **Remove** deletes one. Each item counts as a point mass.

Put in an event, several items become one payload: their total weight, the
weight-weighted CG, and their inertia about that CG by the parallel-axis
theorem. The products of inertia this creates are dropped, and the sheet says
so. SIMON reads one payload item per vehicle. In an event, an item with no
weight stops the cargo from being loaded, and the status line names it; put
aboard the vehicle, such an item is skipped.

**Put the occupants and cargo aboard the vehicle.** Unticked, the occupants
are seated in the chosen event and the cargo becomes that event's payload for
the vehicle, as HVE does it. Ticked, they go on the vehicle's
[Aboard](#aboard-occupants-and-cargo-on-the-vehicle) list instead and travel
with it into every event: each occupant as its GEBOD (or stated) weight at its
seat position, or at the CG when no seat position is given; each cargo item as
itself. Two more controls appear, **Applied** and **On the centreline (ignore
sideways offsets)**, with the meanings given under
[Aboard](#aboard-occupants-and-cargo-on-the-vehicle). Aboard occupants are
weights only: no human body is added to the case for them.

### 5. Add to the case

| Control | Does |
| --- | --- |
| **Event** | The event the vehicle joins: the active event, another event, or **Case only (no event)** |
| **Preview** | Builds the package on a copy of the case and shows the sheet. The case is not changed and nothing is recorded |
| **Add to Case** | Builds it into the case. Locked while results are on screen; reset the run first |
| **Close** | Closes the window |

**Add to Case** adds a new vehicle (the chosen record, or the generic, scaled
if specifications were stated) and adds it to the chosen event; if the event
has no room for another vehicle, the vehicle is added to the case only and the
status line says so. Then:

- unticked *aboard*: it seats the occupants in that event (an event holds at
  most four; anyone beyond that is named in the status line and not seated)
  with the seat positions given, and sets the event's payload for the vehicle
  from the cargo;
- ticked *aboard*: it puts the occupants and cargo on the vehicle's Aboard
  list;
- with **Case only (no event)**: it adds the vehicle alone. Occupants and
  cargo are added only when they are going aboard the vehicle.

**Add to Case** never changes a vehicle already in the case. The status line
under the buttons says which vehicle was added and anything that was not done.

**The sheet** below lists every value the package set: **Set** (what), the
**Value** (in the units set in Preferences), **From** (its kind, in color)
and the **Source** (the database file and record, NHTSA, the GEBOD rule, or
the scaling rule with its ratio). **Add to Case** also stores each line in
[Provenance](#provenance), tool *Vehicle Package*.

!!! note "HVE 2027"
    SIMON adds each occupant's mass at the occupant's seat position. With no
    seat position the mass counts at the vehicle CG, and the sheet says so.
    SIMON's *Event Data* report shows the effect in **Static Vehicle Loads**,
    whose **Loaded** column appears when the occupants or payload change an
    axle load. Its *Inertial Properties Including Occupants and Payload* table,
    as in HVE, adds the payload but not the occupants to **Total Weight**, and
    its **CG Location Adjustment** is the payload's alone; **Sprung Weight**
    includes both.

### A vehicle already in the case

With a case vehicle chosen in the **Vehicle** list, the window keeps what is
known about that real vehicle with the case. Its sections are:

| Section | Holds |
| --- | --- |
| **1. Identify** | The VIN, **Check**, **Decode with NHTSA (online)**, and Year, Make, Model, Series, Trim and Type, as for a new vehicle |
| **2. Specifications** | The same specification rows as [Stated specifications](#stated-specifications), with the same four ways to fill them. They change the vehicle only if you scale it to them |
| **Measured steering and suspension** | What was measured on the vehicle, and **Calculate from measurements** (below) |
| **3. Save with the case** | **Save to this vehicle**, **Scale the vehicle to these specs** and **Close** |

There is no matching table, no occupants, no cargo and no **Add to Case**.

- **Save to this vehicle** keeps the VIN, what decoding it said and the
  specifications with the case, for this vehicle, and records the
  identification in [Provenance](#provenance). None of the vehicle's own data
  changes.
- **Scale the vehicle to these specs** scales the vehicle to the
  specifications by the rules under
  [Stated specifications](#stated-specifications), with the same refusals, and
  saves them with the case. It is meant for a generic vehicle; a vehicle with
  a body mesh is refused. It is greyed while no specification is entered, and
  while the vehicle's results are on screen.
- **Close** closes the window.

**Measured steering and suspension.** Enter what was measured; leave a value
at 0 when it was not measured:

- **Steering-wheel turns, lock to lock**, **Right stop (deg, road wheel)** and
  **Left stop (deg)**;
- for **Axle 1** and **Axle 2**: **Axle rate, both wheels (the spring graph's
  slope)**, **Anti-roll bar diameter**, **Bar length L**, and **Bar lever r1**,
  **r2** and **r3**.

**Calculate from measurements** sets the vehicle's values by EDC's formulas,
from what was entered only. Each value set is listed on the sheet with its
formula and numbers, and stored in Provenance. It is greyed while nothing is
entered, and while the vehicle's results are on screen.

| Value | EDC's formula |
| --- | --- |
| Steering gear ratio | turns × 360 / (right stop + left stop), on every steerable axle |
| Ride rate, per wheel | the axle's measured rate / 2 |
| Damping, per wheel | √(k / m), with k the ride rate per wheel and m the axle's own share of the weight per wheel: (x / wheelbase) × W × 0.5 / 386.4, where x is the CG's distance to the *other* axle |
| Anti-roll bar roll stiffness | (π/32) × d⁴ × G / L × (r2/r1)² × T² / r3², with G = 11.5 × 10⁶ psi and T the axle's track |
| Roll centre (solid axle) | (sprung CG height − tire radius) − 3 in, below the CG. For an independent suspension it is listed as not applied, because the engines take a roll centre for a solid axle only |

The damping uses each axle's own share of the weight, from the CG's distance
to the other axle; EDC's sheet takes the distance to the axle's own end.

## Case Intake

**Tools › Automatic Tools › Case Intake...** builds one new event from a structured description
of the case that your own AI tool extracted from the case documents (see
[Case documents stay on your computer](#case-documents-stay-on-your-computer)).

### Case material

The **Case material** section at the top of the window holds the documents the
case is built from: police report, diagram, photographs, statements, a CDR
report, an inspection, a survey, spec sheets, crash tests, medical records.
Each has a number, **D1**, **D2** and so on, which a value cites (*"D2 p.3"*).
A number is never reused, even after its document is removed.

- **Add document...** picks a file. Its **Kind** is guessed from its name (an
  image is a photograph, *police* or *crash report* a police report, a `.cdrx`
  an EDR report) and can be changed, as can its **Title**.
- **Embed in the case**, ticked before adding, copies the file into the case.
  Untick it (the default) and the case LINKS to the file where it is: it keeps
  the path, the size and a SHA-256 fingerprint, and the case stays small. A
  file inside the case's folder is kept by a path relative to it, so a case
  folder moved or copied whole keeps its documents.
- **State** says *linked*, *embedded*, **MISSING** (not at its path, beside the
  case, or under its name in the case's folder) or **CHANGED since added**
  (its bytes are not the ones added, so it is not the document the case
  cites; add it again to cite the new version).
- **Open** opens it in your system's viewer; an embedded one is opened from a
  copy in the temporary folder. **Embed** copies a linked document in, only if
  it is still the file added; **Link** stops carrying it in the case.
  **Remove** takes it out of the case and leaves the file alone.

Documents are not a solver input: adding one does not make saved results
stale. Open is not available in the browser version.

### Pasting the description

Under **1. The case description** the window offers two routes.
**Enter it by hand** starts from an empty description that you fill in under
Review, value by value with where each is stated, and needs no AI tool. Or:

1. Press **Copy prompt for your AI tool** and give the prompt, with the police
   report, diagram, statements and inspection notes, to your AI tool.
2. Paste its answer into the box and press **Read** (enabled once the box
   holds a `{ ... }` object). If it is not the answer the prompt asks for, the
   window says why.

When the case has documents, the prompt ends with their list by number, so
the tool cites each value as the case does. The prompt asks for one JSON
object holding the case ID; the road surface,
friction, grade and conditions; each vehicle's label, type, year, make and
model, weight, CG height, length, width and wheelbase, and its starting x, y,
heading and speed; and the event sequence. It tells the tool to:

- use only what the documents state, and give **null** for anything they do
  not;
- give every value with its source (*"Police report p. 2"*), and mark a value
  **uncertain** where a document is unclear or two documents disagree;
- give meters, kilograms, meters per second and degrees, saying in the source
  when it converted mph, km/h or feet;
- place x forward along the first vehicle's direction of travel and y to its
  right, with the origin at the area of impact unless the diagram gives a
  reference point, and headings with 0 along +x and positive turning right.

### Reviewing it

The **Review** section shows how many values were stated and how many the
source marked uncertain, and the **Engine** the event will use: the first
method named anywhere in the event sequence, looked for in the order EDSMAC4,
EDSMAC, EDCRASH, EDGEN, EDHIS, GATB, SIMON; with none named, SIMON. The line
says which.

Then one table for the environment (**Road surface**, **Road friction (mu)**,
**Road grade (%)**, **Weather / light**) and one per vehicle (**Year make
model**, **Start x**, **Start y**, **Heading (deg)**, **Speed**, **Weight**,
**Length**, **Width**, **Wheelbase**, **CG height**). Each row gives the value
in the units set in Preferences or *not stated*, its kind (**Stated**,
**Stated, uncertain**, **Entered** or **Unknown**) and its **Source**, the
citation the tool gave. A row that sets nothing in the case, and is only kept
with it as what the documents say, is tagged **(record)**: Road surface, Road
grade and Weather / light always, and a vehicle's Weight, Length, Width,
Wheelbase and CG height when a database vehicle is chosen for it. Hover over a
row's name for what its value does.

For each vehicle:

- the check box before its label includes it, or leaves it out of the build;
- **Vehicle data** chooses its data: the database records that match the year,
  make and model the tool read (matched as in
  [Vehicle Package](#2-vehicle-data); hover over one for why it matched), or
  the generic of its type. After correcting the year, make and model in its
  row, press **Find in the database** beside the list to match the records
  again;
- its **type** is the one the answer states (car, pickup, SUV, van, truck,
  trailer); with none it is a passenger car. The type is never guessed from the
  make and model.

A value can be corrected in its row; a value typed there is marked
**Entered**. Emptying a row makes it *not stated*.

### Building

**Build** (locked while results are on screen) adds **one** new event, named
after the case ID (or *Case intake*), with the engine shown, and makes it the
active event. For each included vehicle it adds a **new** vehicle, as Vehicle
Package does, places it in the event and sets its initial x, y, heading and
speed. Existing vehicles and events are not changed. Every value is recorded
in [Provenance](#provenance), tool *Case Intake* (the vehicle's own lines,
tool *Vehicle Package*). Nothing is built, and the status line says why, when
no vehicle is included or the case has no room for another event or for these
vehicles.

| What the answer states | What happens |
| --- | --- |
| A starting position, heading or speed | Set in the event. One not stated is entered as **0** and recorded **Unknown**, and a red line under **Build** counts these placeholders: set them before running |
| Weight, length, width, wheelbase, CG height | Stated specifications: they **scale a generic** vehicle as in [Vehicle Package](#stated-specifications). On a database vehicle (the review tags the rows **(record)**) they are recorded and not applied |
| Friction | Applied to the tires of the vehicles this build adds: each one's tire friction is scaled so that its front tire's peak friction equals the stated value. Other vehicles and the site's surfaces are not changed |
| Grade | Recorded only. No engine reads a case-wide grade; the ground the vehicles drive on is the site geometry |
| Surface, conditions | Recorded only |

!!! note "HVE 2027"
    Case Intake builds the vehicles and their starting conditions. It does not
    seat occupants, set driver controls, or import a site; do those in the
    usual dialogs, or with Vehicle Package and EDR Import.

## Provenance

**Tools › Automatic Tools › Provenance...** lists where values in the case came from: every value
set by Vehicle Package, Case Intake, Crush Stiffness from Crash Tests or EDR
Import. With no records, the window says so and nothing else.

The line at the top counts the records by kind, and how many have been
**changed since recorded**. **Show** narrows the list: **All records**, **Not
stated (estimated, generic, unknown)**, or **Changed since recorded**.

| Column | Is |
| --- | --- |
| **Subject** | What the value belongs to: a vehicle (*V1 name*), an event (*E1 name*), a vehicle in an event (*E1 name / V1 name*), an occupant (*name in V1 name*), or *Case* |
| **Set** | What was set, in words |
| **Recorded** | The value as it was set, with its unit |
| **Now** | For a record about a single field (an occupant's weight, a payload's weight, a vehicle's name), what that field reads today: *same*, or the new value marked **(changed)** when it was edited by hand afterwards. Blank for other records |
| **From** | The kind (Stated, Looked up, Estimated, Generic default, Unknown) |
| **Source** | Where it came from, with its citation, or the rule that produced it |
| **Tool** | Which tool recorded it |
| **When** | The date and time it was recorded |
| **Remove** | Deletes the record. The value in the case is not changed |

The records are saved with the case, in both the `.hvex` and the `.json`
format. They keep naming the right vehicle, occupant or event when vehicles
are reordered or another vehicle, occupant or event is deleted, and a record
about something that is deleted goes with it. They are not a physics input:
recording or removing one never discards a run, and the window is never
locked.

## Aboard: occupants and cargo on the vehicle

A vehicle can carry a list of people and loads that travels with it into every
event and every engine. The list is in the **Aboard** section of the
[Inertia / Mass dialog](../02-vehicles/VehInerDlg.md#aboard-occupants-and-cargo)
(Vehicles panel › **Inertia** › **Edit...**), where each
item has a name, a kind (occupant or cargo), a weight and a position from the
vehicle's sprung-mass CG (x forward, y right, z up). Vehicle Package fills it
when *Put the occupants and cargo aboard the vehicle* is ticked.

The vehicle's own weight, CG and inertia stay those of the **empty** vehicle.
Each run adds the list to a copy of the case as it starts, so the stored
vehicle never becomes the loaded one and a load cannot be counted twice by
editing.

**Applied** chooses how the engine gets the load:

| Applied | What the engine gets |
| --- | --- |
| **Added to the vehicle (every engine)** | The vehicle's weight, CG and rotational inertia with the load combined in, before any engine runs: the hand method, the same in SIMON, EDSMAC4 and every other engine. The CG moves fore and aft, sideways and in height, and every position measured from it (axles and wheels, CG height, the CG-to-side and CG-to-underside distances, roll centers, steer axes, hitch points, accelerometers) moves with it, so the vehicle's geometry stays where it was. The sprung inertias gain the load by the parallel-axis theorem. The springs are the vehicle's own, so SIMON starts it at its entered ride height |
| **As payload in SIMON and EDVDS (the suspension sags)** | In SIMON and EDVDS, the load as the event's payload, combined with any payload the event already states. SIMON then lowers the body on each suspension by the extra static load and moves the wheels by the CG shift, as HVE does with a payload. Every other engine, and a dolly in any engine, gets the load added to the vehicle instead, and the run status says so |

**On the centreline (ignore sideways offsets)** counts each item's weight and
its fore-and-aft and height position, but not its sideways offset. A lone
driver then does not pull the vehicle off a straight line on a flat road, so no
steering correction is needed.

The run status (under **Run** on the playback bar, and in the **Simulation**
panel) ends with an **Aboard:** note naming each vehicle that carries
anything: its load in kilograms and how many items, and how it was applied
(with the CG shift, in meters, when added to the vehicle). It also says when:

- the engine takes no 3-D payload, so a payload-mode load was added to the
  vehicle;
- the vehicle has a body mesh file, which does not move with the CG;
- the event also seats occupants in the same vehicle: check that they are not
  the same people counted twice.

!!! note "HVE 2027"
    HVE has no such list: it adds payloads and occupants per event, which
    HVE 2027 also does (**Event › Payload...** and the event's occupants).
    Aboard items are weights at positions. They have no rotational inertia of
    their own, they are not drawn, and an aboard occupant is not a human body:
    an occupant simulation (EDHIS, GATB) needs the occupant seated in the event.
    The products of inertia a load creates are dropped, because neither the
    vehicle model nor a payload carries them.

## Crush Stiffness from Crash Tests

**Tools › Automatic Tools › Crush Stiffness from Crash Tests...**, or the
**From crash tests...** button below the four sides in the Vehicle editor's
**Vehicle › Crush Stiffness...**, opens **Crush Stiffness from Crash Tests**
for the selected vehicle (named at the top), which works out a side's
CRASH3 stiffness from one or more staged tests into a full-width rigid barrier
and puts it on the vehicle.

### The tests

**Add test** adds a row; **Remove** deletes one. Weights, speeds and lengths
are in the units set in Preferences.

| Column | Is |
| --- | --- |
| **Use** | Include the test in the calculation |
| **Test** | Its name (*NHTSA 5423*) and, in the box under it, where the numbers come from (a report and page) |
| **Weight** | The test weight, as tested |
| **Speed** | The impact speed into the barrier |
| **Points** | How many crush measurements, 2 to 10 |
| **C1 ... Cn** | The residual crush, equally spaced across the crush width |
| **Crush width** | The width of the damage |

Or read a test from a file: type its path in the **NHTSA test file** box (or
**Browse...**) and press **Load NHTSA test**.

Or find one in NHTSA's database. **Search NHTSA's crash tests (online)** has:

| Control | Does |
| --- | --- |
| **Make**, **Model** | What to search for; NHTSA's own search matches part of its names, in any case |
| **Model years** | From and to (0 is no bound) |
| **From the vehicle** | Fills make, model and years from the vehicle again (they start from it) |
| **Only vehicle-into-barrier tests** | On by default: the tests this window fits. Untick it to list every test of the vehicle (side, pole and so on), for reference |
| **Search** | Asks NHTSA's database |

The results are listed with **Test** (number), **Year**, **Vehicle**,
**Configuration**, **Speed**, **Angle** and **Type**, and a **Fetch** button on
each row that fetches that test. A line says how many tests matched and how many
are listed; **List more** lists the next page. With no match, the note suggests
the make alone, or fewer letters of the model.

Or fetch a test by its number: type it in **NHTSA test number** and press
**Fetch from NHTSA (online)**. The window asks NHTSA's
Vehicle Crash Test Database for the test, its vehicles and its barrier, and
saves the answers unchanged beside the case as `nhtsa_test_<number>.json`, so
the rows can be rebuilt offline by loading that file. A case not yet saved has
nowhere to keep them, and the note says so. Searching and fetching are not
available in the browser version.

Each vehicle in the test that has a crush profile becomes a row, with its test
weight (or its curb weight when the test weight is missing), its speed, its
crush points and its crush width. Many tests record no crush width (the
database writes 9999 for that): enter it, or press **Vehicle's** beside the
empty box to use the tested vehicle's width, which is the crush width of a
full-width frontal test. Only a vehicle driven into a barrier is ticked
**Use**. In any other test, such as a side test, the struck vehicle stands still
and its crush energy came from the impactor, which this fit does not take, so
its row comes in unticked. The note under the buttons says what was added,
skipped and left unticked, and **What was read from the file** lists which
field gave each value and the fields it did not use. See
[Reading an NHTSA crash test file](#reading-an-nhtsa-crash-test-file).

### No-damage speed b0

**b0** is the barrier speed below which nothing is permanently crushed. It is a
choice, and is recorded as one: commonly 5 mph for fronts and rears and 2 mph
for sides. Type it, or press **5 mph** or **2 mph** (the default is 5 mph).

**Fit b0 to the tests (two or more at different speeds)** fits b0 to the tests
instead. It needs at least two included tests.

### The result

Campbell's model makes each test's barrier speed a straight line in its
average crush: V = b0 + b1 · C̄. The average crush C̄ is CRASH3's own
(C1/2 + C2 + ... + Cn−1 + Cn/2) / (n − 1). Then, with m/L the test mass per
unit of crush width (the mean over the tests used):

- A = (m/L) · b0 · b1
- B = (m/L) · b1²
- G = A² / 2B

With b0 chosen, b1 is the best fit through that b0 (for one test, (V − b0) / C̄).
With b0 fitted, b0 and b1 are the best straight line through every test's
(C̄, V).

The **Result** section shows **A**, **B** and **G** in the units set in
Preferences, b0 (*chosen* or *fitted*) and b1, and for each test its average
crush and how much of the test's kinetic energy its crush profile absorbs with
this A, B and G. When b0 was fitted it also shows how far the line misses the
tests (RMS, as a speed).

There is no result, and the section says why, when a test lacks its weight,
speed, crush width or crush, a crush depth is negative, or b0 is not below a
test's speed; and, when fitting, when the tests' average crushes are all the
same, or the fitted line has no positive slope (more crush at a lower speed)
or no positive b0 (choose b0 instead).

### Apply to this vehicle

| Control | Does |
| --- | --- |
| **Side** | Front, Rear, Left or Right. A table under it shows A, B and G for that side: **this vehicle now**, **From the tests**, and the **Change** in percent, so you see how far Apply would move it |
| **Also set it in this vehicle's EDCRASH events with damage on this side (CDC)** | On by default. See below |
| **Apply** | Sets the stiffness. Locked while this vehicle's results are on screen |

**Apply** puts A and B on that side of the vehicle (the values in **Vehicle ›
Crush Stiffness**; see [Stiffness Coefficient Dialog](../02-vehicles/StiffCoeffDlg.md)).
With the check box on, it also sets the **A Stiffness** and **B Stiffness** of
every EDCRASH event of this vehicle whose CDC names the same side in its third
character (F, B, L or R; see
[Vehicle Impact Setup](../09-events-driver-controls/EventInfo.md#vehicle-impact-setup-edcrash)).
An EDCRASH event that states per-zone stiffness is left as it is and named,
because one pair cannot say what its zones do. Every value set is recorded in
[Provenance](#provenance) as **Estimated**, tool *Crush from tests*, with the
tests and the b0 it came from.

!!! note "HVE 2027"
    Kv is not set, and G is shown for reference only: the vehicle stores A and
    B, from which G follows.

## Reading an NHTSA crash test file

Vehicle Package and Crush Stiffness from Crash Tests both read a test from
NHTSA's Vehicle Crash Test Database. The file can be:

- a table with a header row, its columns separated by commas, tabs, `|` or
  `;` (the shape of the database's table downloads, or a spreadsheet saved
  from one); or
- JSON, with the fields in any object at any depth: a response from the
  database's API (nrd.api.nhtsa.dot.gov), or the file **Fetch from NHTSA**
  saves.

Fields are found by **name**, never by position, and names match in upper or
lower case. The test fields read are TSTNO, TITLE, TSTCFN, TSTTYP and CLSSPD;
the vehicle fields are VEHNO, MAKE (or MAKED), MODEL (or MODELD), YEAR, BODY
(or BODYD), VIN, VEHTWT (test weight), CURBWT (curb weight), WHLBAS
(wheelbase), VEHLEN, VEHWID, VEHCG (the CG's distance behind the front axle),
VEHSPD (impact speed; the test's CLSSPD closing speed when missing), PDOF,
DPD1 to DPD6 (the crush profile) and VDI. The API's own names are read as
the same fields (`vehicleTestWeight`, `vehicleCurbWeight`, `vehicleLength`,
`vehiclecenterofGravityDistanceBehindFrontAxle`, `vehicleSpeed`,
`damageProfileDistancesOne` to `Six`, `closingSpeed`, and so on), and so are
three it adds: `totalLengthofIndentation` (the crush width),
`distancebetweencenterofDamagedareaandCGAxis` (the damage offset) and
`maximumCrushDistance`. Values are in NHTSA's metric units: kilograms,
millimeters and km/h. A crush profile is read from DPD1 in order, and a
missing DPD ends it. A file holding several tests is read for its first test.
A vehicle listed twice (the API's vehicle list and its vehicle detail both
carry it) is read once.

- **9999 means not recorded.** The database writes 9999 for a value it did
  not record. It is read as missing, and **What was read** says so; it never
  becomes a 9.999 m crush width.
- **A stated speed of 0 is real.** The struck vehicle in a side test stands
  still. Only a vehicle driven into a barrier that states no speed of its own
  takes the test's closing speed.

!!! note "Which names are checked"
    The API names were checked against responses NHTSA's database served
    (tests 4457, a frontal test into a rigid barrier, and 5270, a side test;
    kept in `tests/data/nhtsa/`). The Test Reference Guide's codes (VEHTWT,
    DPD1, ...) for table downloads have not yet been checked against a table
    NHTSA served. Every read lists which field gave which value and the fields
    it did not use, so a file that names a value differently shows that value
    missing; it does not produce a wrong number.

## EDR Import

**Tools › Automatic Tools › EDR Import...** brings an event data recorder's
pre-crash record (a Bosch CDR report or a manufacturer's equivalent) into a
vehicle of the active event: its initial speed, and its throttle, brake and
steering tables on the simulation's own clock. For a SIMON event it can also
solve the driver so the run follows the recorded speed. After the event is run,
it compares the recorded yaw rate, accelerations and delta-V with the run's.

The window works on the **active event**. At its top is the vehicle picker every
vehicle dialog has, offering the active event's vehicles; picking one here
selects it everywhere, and everything below is that vehicle's record. A case
with no event, or an event with no vehicle, is told to add one first. A new or
opened case starts the window empty.

### Kept with the case

When the case keeps records, they are listed first, under **Kept with the
case**, each with its vehicle, event, sample counts and when it was kept.
**Open** brings one back (it selects its vehicle at the top) to compare or apply
again; a record kept for another event opens once that event is the active one.
**Remove** deletes it. A record follows its vehicle and event when either is
renumbered, and goes when either is deleted.

### 1. The record

There are three ways in:

- **Enter it by hand** — an empty record to type the report's pre-crash table
  and delta-V into, row by row, as the report prints them, with no AI tool and
  nothing to paste.
- **Open a file...** — the report as a PDF (a Bosch CDR report or a
  manufacturer's), whose text is read and its tables rebuilt; a CSV,
  tab-separated or text file holding its pre-crash and delta-V tables, each
  under its own header row (a CDR report's CSV export included; UTF-8 or
  UTF-16 text); or a saved AI answer (`.json`). The CDR tool's own `.cdr` and
  `.cdrx` files are not read: their data is encrypted. A PDF whose tables are
  pictures has no text to read; read them by eye or with your AI tool.
- **Paste** the report's tables, each with its header row, or your AI tool's
  answer, into the box and press **Read**. **Copy prompt for your AI tool**
  copies a prompt to give the tool with the report; it asks for one JSON answer
  with the numbers copied exactly as printed (no interpolating, no unit
  conversion, no sign change, no filled gaps).

When the report holds several recorded events, a **Recorded event** list
(each with its pre-crash and delta-V sample counts) chooses the one this crash
produced; changing it replaces the record below, edits included.

The window then names the vehicle, module and event, how many pre-crash and
delta-V samples were read, and anything not used. The record is editable:

- **The record's details and signs** (folded) — **Vehicle**, **Module**,
  **Event** and **Document**, and what the report says is positive for
  steering, yaw rate, longitudinal acceleration, lateral acceleration and
  lateral delta-V (*not stated* until it is set).
- The pre-crash table — **Time (s)**, **Speed** (in the units set in
  Preferences), **Accelerator (%)**, **Service brake** (–, Off or On),
  **Steering (deg)**, **Engine RPM**, **Yaw rate (deg/s)**, **Long. accel
  (g)** and **Lat. accel (g)**, as the report prints them and in its own
  signs; an empty cell is not recorded. **Add a pre-crash row** adds one and
  **x** deletes one.
- **Delta-V samples** (folded) — **Time (ms)**, **Longitudinal** and
  **Lateral**, with **Add a delta-V row**.

A table's columns are found by their labels, and a unit by its label (mph,
km/h or m/s for speed; deg/s or rad/s for yaw rate; g, m/s² or ft/s² for
acceleration); a column whose unit is not known is left out and named. Brake
samples read as on (*On*, *Applied*, *Yes*, *1*) or off (*Off*, *Not applied*,
*No*, *0*).

### 2. Into the case

The section is titled with the vehicle and the event: *2. Into the case:
<vehicle> in <event>*.

| Control | Does |
| --- | --- |
| **Simulation starts at recorder time** | The recorded sample the simulation starts at. That recorder time becomes 0 on the simulation clock |
| **Initial speed** | Set the vehicle's initial speed (**Event › Position / Velocity**) to the recorded speed at that time |
| **Throttle** | Set the throttle table from the accelerator position |
| **Brake** | Set the brake table from the service brake |
| **Steering** | Set the steering table from the steering-wheel angle |
| **Brake ON means this fraction of friction** | Shown with **Brake** ticked: the fraction of available friction (above 0, up to 1) an ON sample stands for |
| **positive = right (clockwise)** / **positive = left (counter-clockwise)** | Shown with **Steering** ticked when the record does not state its steering sign: choose it from the report. When the record states it, a line says which, and that a positive-left record is flipped |
| Yaw rate and lateral acceleration signs | When the record has yaw rate or lateral acceleration and does not state its sign, the same kind of choice is offered (**positive = clockwise (right turn)** / **counter-clockwise (left turn)**; **positive = right** / **left**). Longitudinal acceleration not stated is taken as + forward, the EDR standards' convention, and a line says so |
| **Apply** | Sets the ticked items. Locked while results are on screen |
| **Keep with the case** | Keeps the record with the case for this vehicle in this event, without setting any table |

What **Apply** sets, for the chosen vehicle in the active event:

- **Initial speed.** The recorded speed at the start time. It is an
  *indicated* speed, from wheel speed, which reads low under hard braking or in
  a slide; the provenance record says so.
- **Throttle.** The accelerator pedal position as a 0–1 fraction, under the
  **Pedal (AT_DRIVER)** input method, since that is what a pedal percentage is
  (see [Driver Controls Throttle](../09-events-driver-controls/DriverControls4.md)).
- **Brake.** An EDR records the brake switch, not the pressure. An ON sample
  becomes the fraction of friction you enter, an OFF sample 0, under the **% of
  Friction** input method (see
  [Driver Controls Brake](../09-events-driver-controls/DriverControls3.md)).
  The level is your choice and is recorded as one (Estimated). With no level
  entered, the brake table is not set.
- **Steering.** Steering-wheel degrees. Manufacturers differ on which way is
  positive, so the record must state it or you must choose; otherwise the
  steering table is not set. HVE 2027's convention is + = right (clockwise),
  and a record whose positive is left is flipped. A per-wheel (at the tires)
  steer table for the vehicle is cleared.

Each table starts at the last sample at or before the start time, so it has a
value at time 0; its times are the recorder's minus the start time. Engine RPM,
yaw rate and accelerations are not applied; yaw rate and accelerations are
compared with the run (below). The status line says what was set, and what was
not and why. Every value set is recorded in [Provenance](#provenance), tool
*EDR import*, with the clock offset. **Apply** also keeps the record with the
case, with the window's settings: start time, brake level, sign choices, time
zero and the impact position (target).

### 3. Position: the run follows the record (SIMON)

For a SIMON event, this section drives SIMON's own physics so that its speed
matches the record: the throttle and brake are solved by time, the brake only
where the record's switch is on and the throttle only where it is off, and the
steering is the recorded wheel angle. Where the tires cannot follow the record,
the run says where and by how much. For any other method the section says that
the positioning engine solves SIMON's driver.

Below it, a table holds where the vehicle starts and where it must be
later, side by side, with columns **Recorder time (s)**, **x**, **y** (in the
length units set in Preferences) and **Heading (deg)**:

- **Start position** — where the vehicle's CG is when the simulation starts,
  at the start time chosen in section 2. It is the event's own start position
  (**Event › Position / Velocity**), editable here too. With the impact
  position ticked it is labelled **Start position (first guess)**: the solve
  starts from it and moves it. It is locked while the event's results are on
  screen (Reset the run to edit it here) and while a solve is running.
- **Impact position (target)** — tick it to give the place the vehicle's CG
  must reach at a recorder time: **0** is the trigger, usually the impact.

**Target from a position in the case...**, under the table, fills the
target's x, y and heading from a position the case already holds for this
vehicle: this event's scene positions and path waypoints, then the same
vehicle's positions in the other events (for example an EDCRASH
reconstruction's impact, listed with that event's name and program). A
simulation event's own start is not offered; its **Impact** scene position —
where the vehicle is entered to be when it crashes, which an HVE case's
Position/Velocity dialog carries and the import keeps — is. Choosing one ticks the target; its recorder time stays yours. With
no position in the case the list reads *No positions in the case for this
vehicle*.

The target is kept with the record in the case, as typed, when the record is
kept; **Open** under **Kept with the case** brings it back.

- **Solve from the record** (**Solve speed and start position from the
  record** when the target is ticked) — replaces this event's throttle and
  brake tables (and its steering table, from the record, when its sign is
  known) and runs the event until its speed matches the record. With the
  target ticked, each run also moves the start position until the run is at
  the target at that recorder time (within 0.05 m and 0.2°), so the speed and
  the place are solved together. Up to 12 runs, each a quiet run in the
  background; only the answer is run on screen. It needs at least two speed
  samples, and is not offered for an event whose Physics is *HVE (imported)*.
  It also keeps the record with the case. **Stop** ends it; the case then
  holds the inputs of the run that was stopped.
- **Speed, sample by sample** (folded, after a solve) — for each recorder time,
  the record's speed, the run's, how far off it is, the brake switch, and the
  effort over the next interval (+ throttle / − brake, as a fraction of
  friction), marked *at its limit* where it could not do more.

Without a solve, two buttons place the run on screen:

- **Use the run's pose at that time** — sets the impact position to where the
  run on screen is at the target's recorder time.
- **Move the start to reach it (no speed solve)** — moves the start position so
  that the run is at the impact position at that time, and runs the event
  again. The status line says how far from the wanted pose the new run is; on
  a grade or over friction zones the path's shape changes with where it starts,
  so place again to tighten it.

Both need the event to have been run (or solved from the record).

When the record has yaw rate or accelerations and the event's results are on
screen, a line compares them with the run, sample by sample: how many samples
of yaw rate, longitudinal and lateral acceleration were compared and the worst
difference of each, with **Yaw rate and acceleration, sample by sample**
(folded) listing them. These are not solved for: a yaw-rate miss is evidence
about the steering ratio or offset, the tires, or the recorder's sign.

### 4. Delta-V: the record against the run

When the record has delta-V samples, run the event. While its results are on
screen this section shows:

| Control | Does |
| --- | --- |
| **Recorder time zero is the run's first contact** | Takes the recorder's time zero as this vehicle's first contact in the run, whose time is shown beside it (or a note that the run records no contact for this vehicle) |
| **...is this simulation time** | Takes it as the time you enter, in seconds |
| **Shift (ms)** | Moves the recorder's time zero by this much |
| **positive = right** / **positive = left** | The record's lateral sign, offered when it does not state it. Without it, the lateral comparison is left out |

The run's figure is formed the way the recorder forms its own: the vehicle's
body-axis accelerations (the run's **Fwd Accel** and **Lateral Accel**
outputs) integrated from the recorder's time zero, not the difference of two
velocities, which on a yawing vehicle is a different quantity. The window shows
the peak longitudinal and lateral delta-V of the record and of the run, and
the RMS difference between them, in the units set in Preferences; a plot with
the record as points and the run as lines (blue longitudinal, + forward;
orange lateral, + right); and under **Values**, the numbers row by row. If the
run ends before the record does, the comparison stops there and says so.

!!! note "HVE 2027"
    The recording module is not at the CG, so on a yawing vehicle the module's
    delta-V and the CG's differ by the module's offset. The comparison shows
    that difference; it does not correct for it.

!!! note "HVE 2027"
    **Apply** is locked while results are on screen, and the delta-V
    comparison needs them. To apply a different start time or brake level
    after a run, reset the run, apply, and run again.

**Export Run Report (HTML)** in the HVE Reports window adds an **EDR Delta-V**
section for each record kept for a vehicle of the event. It holds the record's
source, how its time zero and signs were set, the peaks and RMS difference, the
plot and the values, in your display units.
