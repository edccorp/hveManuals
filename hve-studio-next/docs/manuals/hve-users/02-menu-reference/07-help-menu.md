# Chapter 7: Help Menu

*HVE User's Manual — Section Two: Menu Reference, HVE Studio edition. Replaces
HVE's Chapter 7, Help Menu.*

HVE Studio's Help menu has four items: **Manual**, **License...**, **Check for Vehicle Data
Updates** and **About HVE Studio...**.

| HVE item | HVE Studio |
|---|---|
| Help Topics | Help › **Manual** — see [HELP TOPICS](#help-topics) |
| User Manuals | Help › **Manual** — see [USER MANUALS](#user-manuals) |
| Tech Support | Not in HVE Studio — see [TECH SUPPORT](#tech-support) |
| About | Help › **About HVE Studio...** |
| Online Licensing | Help › **License...** — see [ONLINE LICENSING](#online-licensing) |
| — | Help › **Check for Vehicle Data Updates** — see [CHECK FOR VEHICLE DATA UPDATES](#check-for-vehicle-data-updates) |

---

## ABOUT

**Menu Option:** Help › About HVE Studio...

**Purpose:** Show what program this is.

**Description:** The About HVE Studio box shows **HVE Studio**, Human
Vehicle Environment and Engineering Dynamics Company, a short description
(HVE's own physics programs in a new cross-platform interface) and the version, with the preview build's identifier
in brackets. Quote the version when you report a problem. **OK** closes it.

![The About HVE Studio box](../images/hvn-01-about.png)
*Help › About HVE Studio.*

---

## HELP TOPICS

**Menu Option:** Help › Manual

**Purpose:** Open this manual set, the reference for HVE Studio, in your web browser.

**Description:** **Manual** opens the published HVE Studio manual
(manuals.edccorp.com/studio/) in your default browser. HVE Studio has no help
browser of its own; help in the program is also given in place: hover over a
control to see its tooltip, and turn on **View › Show Guidance Text** for the
longer explanations in the dialogs. If no browser can be started, the address
is copied to the clipboard and the Help menu says so, under the item.

---

## USER MANUALS

**Menu Option:** Help › Manual

**Description:** There is no User Manuals submenu: the HVE Studio edition of the
HVE manuals — this User's Manual, the dialog reference and the program manuals
for each calculation method — is the one manual set that **Help › Manual** opens.
Start at [What is HVE Studio?](../../getting-started/01-what-is-hve-studio.md).

---

## TECH SUPPORT

!!! warning "Not in HVE Studio"
    HVE Studio's Help menu has no Tech Support item. Questions and
    problem reports about the preview go to EDC. When reporting a problem,
    include the case file, the steps that produce the problem, the version
    shown in Help › About HVE Studio..., and on Windows the program's log
    `hve-next.log` (and `hve-next.crash.txt`, if there is one; see
    [Installing and Running](../../getting-started/02-installing-and-running.md#log-and-crash-files)).

---

## ONLINE LICENSING

**Menu Option:** Help › License...

**Purpose:** Show this computer's license, and activate, refresh or release it.

**Description:** The **License** window opens with **This computer**: who the
license is for, the license number and whether it is for one computer per seat
or company-wide, the engines it covers, the date updates run through, and how
long it works without reaching the license server. When no license is active it
says why.

- **Activate.** Paste the EDC Software secret you received by email when you
  bought HVE (the same one EDC's Blender add-ons use) and press
  **Activate this computer**. **Computers on this license** lists the computers already
  activated. Activation sends the secret, the computer's name and three hashed
  hardware identifiers to EDC's license server; no raw hardware identifier
  leaves the computer.
- **This computer has no internet.** **Save activation request...** writes a
  request file (it holds no secret). On any computer with internet, open the
  offline page the window names, enter your secret and upload the request; it
  gives you a license file. **Import license file...** brings it in. An offline
  license works for a year.
- **Manage** (once activated): **Refresh now** (the program also refreshes the
  license on its own when it is due and the server can be reached), **Computers
  on this license**, and **Release this computer**, which frees its seat after
  asking you to confirm.
- **Replace.** If EDC has changed the key it signs licenses with (it does so
  only after a security incident), a license signed with the old key stops
  working once the program has seen the new one, and the window says so. The
  program replaces it on its own the next time it reaches the license server;
  **Refresh now** does it immediately. No new activation or seat is needed.

!!! note "HVE Studio"
    An installed release needs a license covering the program of the event you
    run; without one, **Run** is refused and the run status gives the reason.
    A copy that does not require a license (a preview folder or development
    build) says so in this window, and runs every engine. HVE's user ID code is
    not used; the EDC Software secret takes its place.

---

## CHECK FOR VEHICLE DATA UPDATES

**Menu Option:** Help › Check for Vehicle Data Updates

**Purpose:** Install a newer edition of EDC's vehicle data.

**Description:** EDC's licensed vehicle data (`EDCVehicles.hvedb`, with its
meshes and wheel images inside it) is a separate download from the program,
installed once per computer in the EDC vehicle data folder (see
[Vehicle databases](../../getting-started/04-cases-and-files.md#vehicle-databases)).
This item asks EDC whether a newer edition that your license covers is
available. The program also checks by itself, in the background, at most once
a day.

When an update is available, a notice in the bottom-right corner of the window
names the version, the version installed and the download size. **Install**
downloads it, with a progress bar, then checks and unpacks it; **Later** hides
the notice for this session. When it is done, the notice says where it was
installed and how many vehicles the library now holds; **OK** closes it. If any
step fails, the notice says why and the vehicle data already installed is left
exactly as it was.

Vehicle data updates come with an activated license (see
[ONLINE LICENSING](#online-licensing)); without one, the check says so. A check
asked for from this menu always reports its result, including that there is no
update. This item checks for vehicle data only, not for new versions of the
program.

<!-- NAV -->

---

← Previous: [Chapter 6B: Tools Menu](06b-tools-menu.md)  |  [Index](README.md)

<!-- /NAV -->
