# Environment Information Dialog

A new environment is added to the current case using the Environment Information dialog (class `CEnvInfoDlg`). The dialog has three top-level fields — *Environment Name*, *Date of Crash* and *Time of Crash* — followed by a tabbed property sheet and the standard OK/Cancel buttons.

The property sheet may contain up to five tabs — **Terrain**, **Sky**, **Physical**, **Location** and **Traffic Signals**. Which tabs appear depends on the run mode and viewer type:

- The **Terrain** tab is always present.
- In HVE-3D (RUN_MODE_3D), all five tabs are shown.
- With a 3-D camera viewer, the **Sky**, **Location** and **Traffic Signals** tabs are added.
- In HVE-2D, only the **Terrain** tab is present. The **Physical** tab (Wind Speed, Wind Direction, Temperature, Barometric Pressure, etc.) is built only in RUN_MODE_3D, so those fields are simply not shown in HVE-2D — they are not displayed read-only.

## Top-Level Fields

### Environment Name
A user-editable field allowing the user to assign a name to the current environment.

### Date of Crash
The date of the crash or test being simulated. The entry format follows the user's date-style preference; the field label displays the expected format as either *(mm/dd/yy)* (US) or *(dd/mm/yy)* (European). The displayed year uses a 2-digit format.

### Time of Crash (24 Hr)
The standard time of day (24-hour military time) for the crash or test being simulated.

## Terrain Tab

The Terrain tab selects and configures the environment geometry or aerial photo.

### Type
Radio buttons selecting the kind of environment surface:

- **None** — no terrain or aerial image.
- **Terrain Map (Geometry)** — a 3-D geometry file.
- **Aerial Photo (Bitmap)** — an aerial photograph displayed on a ground polygon.

Selecting a type enables the corresponding *Terrain Map* or *Aerial Photo* group and disables the other.

### Terrain Map group
- **Filename** — an editable field showing the terrain geometry file in use.
- **Open...** — opens an existing geometry file. The file-type filter offers HVE Geometry Files (\*.h3d), Inventor Files (\*.iv), VRML Files (\*.wrl) and OBJ Files (\*.obj); when the DXF translator feature is licensed, DXF Files (\*.dxf) and DWG Files (\*.dwg) are also offered.
- **Save As...** — saves the current environment geometry to a new HVE Geometry file (\*.h3d). Only H3D is supported for saving; texture pathnames are cleared/stored relative to the environment textures directory. Enabled only when geometry is in use.
- **Remove** — clears the current terrain filename and resets the Type to None. Enabled only when a filename is present.
- **Use As Default** — checkbox marking the current terrain file as the default for new environments (not available when editing an existing environment).

### File Import Options
Shown for non-H3D geometry (e.g. DXF/DWG/IV/WRL/OBJ); disabled for native \*.h3d files:

- **Flip About X-Axis** — checkbox to flip the imported geometry about the X axis.
- **Scale Factor** — numeric scale applied to the imported geometry.
- **Default Type** — combo box assigning the default polygon/object type for the imported geometry. Options: *Human*, *Vehicle*, *Road*, *Friction Zone*, *Curb*, *Water*, *Other*.

### Aerial Photo group
- **Filename** — an editable field showing the aerial image file in use.
- **Open...** — opens an aerial image. Supported formats: BMP (\*.bmp), TIF (\*.tif), GIF (\*.gif), RGB (\*.rgb) and JPEG (\*.jpg/\*.jpeg). The image's ground coordinates are set from the image aspect ratio.
- **Remove** — clears the current aerial filename and resets the Type to None. Enabled only when a filename is present.
- **Use As Default** — checkbox marking the current aerial image as the default for new environments (not available when editing an existing environment).

## Sky Tab

The Sky tab configures the sky image, sky dome and fog. (Shown only in 3-D run modes or with a 3-D camera viewer.)

- **Ambient Light Intensity** — slider and edit field (0.0–1.0).
- **Use Sky Image** — checkbox enabling a sky/backdrop image. When checked, a **Filename** field, **Open...** and **Remove** buttons, and a **Use As Default** checkbox become available. Sky images use the same bitmap formats as aerial photos.
- **Use Sky Dome** — checkbox (available only when a sky image is in use) with a **Sky Dome Rotation** field.
- **Fog Type** — combo box: *None*, *Haze*, *Fog*, *Smoke*. Selecting any type other than None enables the **Visibility** field.
- **Set Sky Color...** — opens a color editor for the background/sky color.

## Physical Tab

The Physical tab holds the atmospheric and coordinate-system parameters. It is built only in RUN_MODE_3D (HVE-3D).

### Angle of X Axis (deg)
The angle of the user-defined earth-fixed coordinate system relative to true north. Valid range is -360 to +360 degrees.

### Wind Speed
The ambient wind velocity (displayed in the current user velocity unit, e.g. mph).

### Wind Dir. (from X Axis, deg)
The ambient wind direction, measured from the earth-fixed X axis. Valid range is -360 to +360 degrees.

### Barometric Pressure
The ambient barometric pressure.

### Temperature
The ambient temperature.

### Gravity
The local acceleration of gravity.

## Location Tab

### Current Location
A drop-down combo box that selects an existing location from the location database. Selecting a location fills in the Latitude, Longitude and GMT fields from that database entry.

### Latitude (dd.mm.ss)
Used to define the global latitude, entered in degrees.minutes.seconds. N and S denote north and south latitudes, respectively.

### Longitude (dd.mm.ss)
Used to define the global longitude, entered in degrees.minutes.seconds. E and W denote east and west longitudes, respectively.

### GMT (+/-24 Hr)
(Also called UTC offset.) The difference between the local standard time and the time at zero longitude. West longitudes are negative (e.g., New York City is -5 hours).

### New Location / Add New Location
To add a location to the database, type its name into the **New Location** edit field and click **Add New Location**. A duplicate name is rejected. The new location is added to the Current Location combo and selected (with empty Latitude/Longitude and GMT 0), ready for its coordinates to be entered. (Saving the page also updates an existing database entry in place if its name matches.)

## Traffic Signals Tab

The Traffic Signals tab configures the timing of traffic signals placed in the environment. (Shown in 3-D run modes or with a 3-D camera viewer.)

- **Traffic Signals List** — list of signals in the environment; select one to edit its timing.
- **Type** / **Layout** — read-only fields describing the selected signal.
- **Is Active** — checkbox enabling the selected signal.
- **Repeating** — checkbox for a repeating signal cycle.
- **Signal Timing** — a radio choice between **Start Time** (with a start-time edit field) and **Follow** (with a combo selecting the signal to follow plus an **Overlap** field).

## OK / Cancel
OK validates each tab in turn and accepts the entered environment information; Cancel discards the changes.

---
*Source topic: EnvtInfoDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Environment Material Properties Dialog](EnvrMatPropDlg.md)  |  [Index](README.md)  |  Next: [Lining Friction Properties Dialog](LinFriPropDlg.md) →

<!-- /NAV -->
