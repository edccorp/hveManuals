# Camera Setup Dialog Box

The Camera Setup dialog uses a camera metaphor to determine how a scene is viewed: viewing a scene is much like looking through a camera. The dialog also lets the user save and delete named views, so several views can be defined and re-used.

This dialog box contains the following options:

## View Name

A drop-down list of the available views. The list contains the current view (shown as *Current (Untitled) View*) only while it is unsaved, plus any saved cameras. Selecting a camera loads its settings into the dialog.

## View From — Object Name

The View From object list allows the user to select the object to which the camera is attached. This list contains all the objects (humans, vehicles and the environment) in the event. Attaching the camera to a human or vehicle causes the view to move with the human or vehicle.

## View From — X, Y, Z

The coordinates of the camera. These coordinates are relative to the selected View From object. For example, if the View From object is a vehicle, setting the coordinates to 0,0,0 means the scene will be viewed from the vehicle's CG, regardless of the vehicle's location in the environment.

## Use Vehicle's Vertical

When checked, the camera's up direction follows the View From vehicle's vertical (body-fixed) axis, so the view rolls and pitches with the vehicle. When unchecked, the camera up direction remains earth-fixed vertical.

## Make Glass Clear

When checked, the window glass of the View From vehicle is rendered fully transparent. This is useful for views from inside a vehicle (e.g., a driver's-eye view), where tinted glass would otherwise obscure the scene.

## Look At — Object Name

Selects the object at which the camera is aimed. The Look At coordinates below are relative to this object, so the camera can, for example, be attached to one vehicle while continuously aimed at another.

## Look At — X, Y, Z

The picture center defines the coordinates at the center of the viewer. The coordinates are relative to the Look At object. For example, if the Look At object is a vehicle, setting the picture center to 100,0,0 causes the picture center to be 100 feet ahead of the vehicle, regardless of the vehicle's position or orientation.

## Near

The depth of field is defined by near and far clipping planes. Any object closer to the camera than the near clipping plane will not be rendered in the scene. Specify the near clipping distance here.

## Far

Any object farther from the camera than the far clipping plane will not be rendered in the scene. Specify the far clipping distance here.

## Focal Length

The focal length of a virtual 35mm camera used to visualize the scene. A focal length of 50mm is the default and represents a normal view. Focal lengths less than 50mm are wide-angle lenses; greater than 50mm are telephoto lenses.

## Camera Tilt Angle

Rotates the camera about its viewing axis, tilting (banking) the picture. A tilt angle of 0 degrees keeps the horizon level.

## Save...

Saves the current settings as a named camera. The camera is added to the Camera list so it can be recalled later.

## Delete...

Deletes the currently selected saved camera.

## OK / Cancel / Apply

**Apply** applies the current settings to the viewer without closing the dialog; **OK** applies the settings and closes the dialog; **Cancel** closes the dialog without applying changes.

---
*Source topic: CameraSetDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [3-D Editor Menu](3dEditor.md)  |  [Index](README.md)  |  Next: [Key Results Dialog Box](KeyResDlg.md) →

<!-- /NAV -->
