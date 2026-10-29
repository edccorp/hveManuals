# Chapter 8a — Human Designer

The Human Designer is the Vehicle Designer's frame turned on a human: a stage
bar (along the bottom; **Bar position** moves it to the top, left or right), a
**Key figures** strip on the left that remembers what each number was, the
Human editor's own dialogs hosted on the stage that asks their question, and a
**Guidance** panel under Key figures whose rows name the fix and the stage that
owns it. It is the Human editor's panel: switching to the Human editor (F2)
opens it, and **Human › Human Designer...** opens it too.

Like the other designers it is an ordinary docked window, on the left with the
3-D view beside it, where the body is drawn. A dialog on a stage is the same
dialog drawn in the stage instead of its own window, so a field has one editor.
Body Segments, Joint Properties, Body Pose and Injury Tolerances used to open as
four separate windows over the view; they are stages now.

The human the designer edits is the one selected in the Humans panel (the Human
stage). A click on a body in the 3-D view also selects it.

## The stages

1. **Human**: the **Humans** panel: **Add Human**, **Remove**, the list of the
   case's humans, and the selected one's Identity, Anthropometry (the GEBOD
   inputs) and Anthropometric weight and mass.
2. **Body Segments**: the 15 segments' mass, inertia, color, contact ellipsoids
   and joint locations. A click on a body part in the 3-D view selects that
   segment here.
3. **Joint Properties**: the 14 joints' stops, stiffness and damping.
4. **Body Pose**: the body's posture and initial velocity in the **active**
   event. HVE states a pose per event, so the same human can sit differently
   in each; the Events stage makes another of its events active.
5. **Injury Tolerances**: the limits EDHIS tests the run's head, chest, knee
   and belt loads against.
6. **Events**: every event that lists the human, its calculation method, what
   the human is there (a pedestrian, or seated in a vehicle) and whether the
   event poses it. **Make active** makes that event the active one, whose pose
   the Body Pose stage edits. Which vehicle a human rides in, where it sits and
   its restraint are the event's, edited in the Event editor (F5).
7. **Summary**: the spec sheet (every key figure, what it was and the change),
   **Set as baseline**, **Copy spec sheet**, and the guidance.

## Key figures

Stated mass, Segment mass sum, Segments with mass, Contact ellipsoids, Events
listing it and Events posing it. A mass is shown in kg, or as its weight in lb
in US units. In parentheses, what each was when the stage was opened, or at
**Set as baseline**; a changed value is yellow.

## Guidance

| Grade | Stage | Rule |
|-------|-------|------|
| Fix | Human | The case has no human. |
| Fix | Human | The human has no body (no segment data). |
| Consider | Body Segments | The stated mass differs from the 15 segment masses' sum by more than 1%. The engines take the segments' masses. |
| Fix | Body Segments | A segment carries mass and a rotational inertia of zero or less about some axis. |
| Note | Events | The case has events and none lists the human. |
| Note | Events | The human is in some event but not the active one, whose pose the Body Pose stage edits. |

Each row's **Go to** button opens the stage that owns the input.

<!-- NAV -->

---

← Previous: [Chapter 8 — Creating and Editing Humans](08-creating-editing-humans.md)  |  [Index](README.md)  |  Next: [Chapter 9 — Human Model Definition](09-human-model-definition.md) →

<!-- /NAV -->
