# Chapter 7: Help Menu

*HVE User's Manual — Section Two: Menu Reference, HVE 2027 edition. Replaces
HVE's Chapter 7, Help Menu.*

HVE 2027's Help menu has two items: **License...** and **About HVE 2027...**.

| HVE item | HVE 2027 |
|---|---|
| Help Topics | Not in HVE 2027 — see [HELP TOPICS](#help-topics) |
| User Manuals | Not in HVE 2027 as a menu — see [USER MANUALS](#user-manuals) |
| Tech Support | Not in HVE 2027 — see [TECH SUPPORT](#tech-support) |
| About | Help › **About HVE 2027...** |
| Online Licensing | Help › **License...** — see [ONLINE LICENSING](#online-licensing) |

---

## ABOUT

**Menu Option:** Help › About HVE 2027...

**Purpose:** Show what program this is.

**Description:** The About HVE 2027 box shows **HVE 2027 Preview**, Human
Vehicle Environment and Engineering Dynamics Company, a short description
(HVE's own physics programs in a new cross-platform interface) and the version, with the preview build's identifier
in brackets. Quote the version when you report a problem. **OK** closes it.

![The About HVE 2027 box](../images/hvn-01-about.png)
*Help › About HVE 2027.*

---

## HELP TOPICS

!!! warning "Not in HVE 2027"
    HVE 2027 has no built-in help browser. Help in the program is given in place:
    hover over a control to see its tooltip, and turn on **View › Show Guidance
    Text** for the longer explanations in the dialogs. This manual set is the
    reference.

---

## USER MANUALS

!!! warning "Not in HVE 2027"
    There is no User Manuals submenu. The HVE 2027 edition of the HVE manuals —
    this User's Manual, the dialog reference and the program manuals for each
    calculation method — is this manual set; start at
    [What is HVE 2027?](../../getting-started/01-what-is-hve-2027.md).

---

## TECH SUPPORT

!!! warning "Not in HVE 2027"
    HVE 2027 Preview's Help menu has no Tech Support item. Questions and
    problem reports about the preview go to EDC. When reporting a problem,
    include the case file, the steps that produce the problem, the version
    shown in Help › About HVE 2027..., and on Windows the program's log
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
  bought HVE (the same one EDC's Blender add-ons use) and press **Activate this
  computer**. **Computers on this license** lists the computers already
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

!!! note "HVE 2027 Preview"
    The preview does not require a license: every engine runs, and the License
    window says so. HVE's user ID code is not used; the EDC Software secret
    takes its place.

<!-- NAV -->

---

← Previous: [Chapter 6B: Tools Menu](06b-tools-menu.md)  |  [Index](README.md)

<!-- /NAV -->
