# Overlays Dialog Box

HVE's Overlays dialog, opened from the View menu, displays or removes from the scene all the objects belonging to a named overlay (for example *Accident Debris* or *Measured Skids*).

In HVE 2027 the same job is done by **layers** in the **Outliner**: **View › Outliner** (the Environment panel's **Selected Surface** section has an **Open Outliner** button). Each layer of the site is listed with its surfaces under it, and the case's saved cameras are listed in their own group.

## Draw and Drive switches

Each layer and each surface has an **eye** switch (**Draw**: show it in the picture) and a **road** switch (**Drive**: include it in the surfaces the engines drive on). Turning both off removes a surface from the picture and from the solver; this is reversible, because the geometry is rebuilt from its file on every load. A greyed eye means the surface's own switch is on and its layer is what hides it.

- Ctrl-click an eye to show only that layer or surface; Shift-click a layer's eye to switch its surfaces too.
- Drag down a column of switches to set several at once.
- Right-click a layer or surface for a menu; the commands offered include **Show Only This**, **Show All**, **Hide**, **Hide All**, **Make All Drivable** / **Make None Drivable**, **Move to Layer**, **New Layer**, **Rename**, **Duplicate**, **Delete** and **Delete Layer**.
- Drag surfaces onto a layer to move them to it. The **Search** box filters the list.

As in HVE, layers serve several purposes: showing the scene before and after the accident, comparing simulated and measured skidmarks, and so on.

## Scanned Image Overlay

An aerial photograph or scanned image of the site is set up with **Environment › Aerial Image...** in the Environment Editor.

!!! note "HVE 2027"
    The **Drive** switch is new: an overlay in HVE only affects what is displayed, while a layer in HVE 2027 can also remove surfaces from the physics. Removing a drivable surface changes the result of the next run.

<!-- NAV -->

---

← Previous: [Options Menu](OptionsMenu.md)  |  [Index](README.md)  |  Next: [Playback Controls (Toolbar)](PlayBackControls.md) →

<!-- /NAV -->
