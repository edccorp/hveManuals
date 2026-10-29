# Select Object Dialog Box

In HVE this is not a dialog of its own: it is a panel added to the standard Windows file Open/Save dialog, showing the **Case Title**, a line describing the object being opened or saved, and a sorted list of the files of that type in the current folder.

!!! warning "Not in HVE Studio"
    HVE Studio does not use the operating system's file dialog and has no Select Object panel or **Case Title** field.

HVE Studio opens and saves files with its own file browser window (for example **File › Open Case...**, **File › Save Case As...**, or a **Browse...** / **...** button beside a file field). It shows:

- a **path** field at the top (type a folder and press Enter);
- a list of places: **Home**, **HVE Studio Cases** (Windows and macOS), **Working folder**, the root folder and, where present, mounted drives; a **favorites** list (**+ Add current** adds the current folder; right-click a favorite for **Remove from favorites**); and the **Recent folders**;
- the folder's sub-folders, with **.. (up)**, and its files, filtered to the types the command accepts;
- a **Search...** box, on its own row above the file list, that filters the list by name; click a column header to sort it;
- a **View** list beside the file list's heading: **Details** (the sortable table), **Medium icons** or **Large icons** (folders and files together as icons; double-click to open); the choice is kept;
- the selected file name, which can be typed for a save.

With no case open, **File › Open Case...** and **File › Save Case As...** start in your **HVE Studio Cases** folder: `Documents\HVE Studio\Cases` on Windows (the real Documents folder, so it follows OneDrive) and `~/Documents/HVE Studio/Cases` on macOS, created the first time it is needed. With a case open they start in the case's folder. Files you make with no case open (an animation, a rendered image, exported variables) are offered in `Documents\HVE Studio`. The program's own install folder is never offered: an uninstall removes it, and everything in it.

The case's name is shown at the right-hand end of the main menu bar (with an asterisk when it has unsaved changes; hover for the full path).

<!-- NAV -->

---

← Previous: [Render Dialog Box](RendOptDlg.md)  |  [Index](README.md)  |  Next: [Set Grid Dialog Box](SetGridDlg.md) →

<!-- /NAV -->
