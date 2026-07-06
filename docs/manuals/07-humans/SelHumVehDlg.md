# Selected Humans & Vehicles Dialog Box

This is a modeless, resizable dialog box that displays the humans and vehicles selected for the current event. The dialog title bar shows the name of the current event.

## Humans & Vehicles Tree
The humans and vehicles in the current event are shown in a tree control rather than a flat list:

- Each root-level entry is a (non-trailer) vehicle or an independent human (e.g. a pedestrian).
- Trailers and other towed vehicles appear as children of their parent (tow) vehicle.
- Humans connected to a vehicle (e.g. occupants) appear as children of that vehicle; unconnected humans appear at the root level.

Clicking an entry in the tree makes that human or vehicle the currently selected object for the event: the event editor view, and any open position/velocity dialog, are updated to reflect the newly selected object.

If no humans or vehicles have been selected for the event, a "No Humans or Vehicles Selected" message is displayed instead.

---
*Source topic: SelHumVehDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Human Material Properties Dialog Box](HumMatProp.md)  |  [Index](README.md)

<!-- /NAV -->
