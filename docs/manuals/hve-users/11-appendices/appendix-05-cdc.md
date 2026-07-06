# Appendix V — Collision Deformation Classification (CDC)

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Appendix V, pages V-1 through V-8.*

The Collision Deformation Classification (CDC) is a seven-character code
which describes the vehicle damage. The characters in the CDC identify the
Principal Direction of Force (PDOF) in clock direction, the impacted surface
(front, right, back, or left), the shape of the damage profile, and the
extent of maximum penetration. If a more accurate direction than the clock
direction is known, the PDOF may be entered in degrees after the CDC.

*Figure V-1 — Description of each column within the seven-character CDC
code.*

## Columns 1 and 2 — Principal Direction of Force

As defined in the first two columns of the CDC, the Principal Direction of
Force (PDOF) during impact is the direction of the force that caused the
crush and sheet metal displacement on the damaged vehicle. The PDOF is
determined by the vector result of forces normal and tangential to the
surface of the vehicle in the area of deformation. In columns 1 and 2 of the
CDC, the PDOF is designated by hour sectors on a conventional clock face and
referred to as the *clock direction*. 12-o'clock indicates a head-on impact,
06-o'clock refers to a rear-end impact, 03- and 09-o'clock refer to
perpendicular impacts to the right and left sides, respectively. Angles in
between are noted accordingly.

*Figure V-2 — Columns 1 and 2, Clock Direction of PDOF. Figure V-3 —
Relationship between hour angles and PDOF (degrees).*

Note the clock direction is a two-digit code; that is, six-o'clock must be
entered as 06, not 6. Note also that, by virtue of the hour increments, the
clock direction in columns 1 and 2 is rounded to the nearest 30 degrees.

## Column 3 — Deformation Location Code

The third column of the CDC, the Deformation Location Code, specifies the
general area of the vehicle which sustained damage: the Front (F), Right
(R), Back (B), or Left (L) side. The Top (T) and Undercarriage (U) of the
vehicle may also be damaged; however, due to the 2-dimensional restrictions
imposed by analysis in 3 degrees of freedom, T and U are not valid CDC
entries for HVE.

*Figure V-4 — Column 3, Deformation Location Code.*

## Column 4 — Specific Longitudinal or Lateral Location of Deformation

The specific area of damage (Distributed, Left, Center, Right, etc.) can be
considered a suffix to column three, in that the Specific Longitudinal or
Lateral Location of Deformation describes, in greater detail, the general
area of damage (front, right, back or left) entered in column 3. Letters
shown on the front and rear may be applied to either the front or rear;
letters shown on the sides may be used for either side.

*Figure V-5 — Column 4, Longitudinal or Lateral Location Code.*

## Column 5 — Specific Vertical Location of Deformation

This entry is also a suffix to column three and refers to vertical damage
characteristics. An entry (A, H, E, G, M, L, or W) is necessary for a valid
CDC. However, again due to the 2-dimensional analysis, column 5 is not used
for any calculations.

*Figure V-6 — Column 5, Vertical Location Code.*

## Column 6 — Type of Damage Distribution

The general type of impact or accident is defined in column 6. Although
several entries are available, EDCRASH only makes a distinction between
Narrow and Wide damage distributions. Further, some entries violate the
assumptions of analysis, notably Sideswipe, Rollover, and multiple impact
(K).

If Narrow impact is specified, the width of the damage profile is set to 16
inches; otherwise, Wide impact is assumed, and the width of damage is set
based on tabular data in conjunction with the Specific Longitudinal or
Lateral Location of Deformation entered in column 4 of the CDC.

*Figure V-7 — Column 6, Type of Damage Distribution.*

## Column 7 — Maximum Extent of Penetration

The extent of maximum residual deformation to the vehicle is based on a
somewhat qualitative system wherein the vehicle is divided into penetration
zones numbered from 1 to 9. Along the longitudinal axis of the vehicle, the
B-pillar is generally taken as the maximum (i.e., the beginning of zone 9).
A frontal crush penetrating rearward to the B-pillar will have a penetration
extent of 9; conversely, a rear impact penetrating forward to the B-pillar
will also have a penetration extent of 9. Laterally, a penetration extent of
9 is associated with penetrating the entire width of the vehicle. A
penetration extent of 0 would imply no permanent deformation, and therefore
no CDC.

For damage extents between 0 and 9, the extents are divided into zones
normally having equal width. The exception to this rule occurs in the areas
which include the windshield and windows.

*Figure V-8 — Column 7, Maximum Extent of Penetration.*

> **NOTE:** See "Collision Deformation Classification", SAE J224 MAR80
> [6.3] for further details.

## Examples

The following are some examples of acceptable entries:

- **11FDEW1** — Full frontal impact having a PDOF of +30 degrees and a
  maximum penetration extending approximately 1/9th of the distance from
  the front of the vehicle to the B-pillar.
- **02RDEW4** — Right side impact having a PDOF of +60 degrees and having a
  maximum penetration of approximately 4/9th of the vehicle's overall
  width.

<!-- NAV -->

---

← Previous: [Appendix IV — Units](appendix-04-units.md)  |  [Index](README.md)  |  Next: [Appendix VI — References](appendix-06-references.md) →

<!-- /NAV -->
