# HelicalGearPlus

Add-In for Autodesk Fusion 360.
Generates straight, helical, and herringbone external, internal, and rack gears,
as well as non-enveloping worms and worm gears.

Originally created by Nico Schlüter, with parts based on Ross Korsky's helical
gear generator. The legacy single-file add-in is preserved under
[docs/HelicalGearPlus/](docs/HelicalGearPlus/) for reference while the
production code is restructured around the phos.systems framework template.

# Status

**Scaffolding in place; functional port pending.** The repository structure has
been set up around the phos.systems Fusion add-in template (`futil`, per-command
modules) but the actual gear-generation logic has not yet been ported from the
legacy file. The add-in does not currently produce any commands when loaded.

# Installation

When the port is complete, install per the standard process:

- Download the project as a ZIP and extract it somewhere convenient, or clone it with git
- Open Fusion 360 and press **Shift+S** to open Scripts & Add-Ins
- Select the **Add-Ins** tab and click the green **+** next to "My Add-Ins"
- Navigate to the `src/HelicalGearPlus/` folder inside the extracted project and hit Open
- The add-in will appear in the "My Add-Ins" list — select it, optionally check "Run on Startup", and click Run

In the meantime, the v1.0.6 release on the Autodesk App Store remains the live
version.
