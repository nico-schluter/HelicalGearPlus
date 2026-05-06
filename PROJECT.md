# Project Overview

Autodesk Fusion 360 add-in that generates parametric gears: straight, helical,
and herringbone external / internal / rack gears, plus non-enveloping worms and
worm gears.

Originally written by Nico Schlüter (with parts based on Ross Korsky's helical
gear generator). The repository has been restructured around the phos.systems
standardised add-in framework as part of the same App Store resubmission cycle
that the LuerFittingGenerator went through. The legacy single-file add-in is
preserved under [docs/HelicalGearPlus/](docs/HelicalGearPlus/) for reference.

## Goals

- Restore App Store availability after the forced resubmission.
- Triage and fix accumulated minor bugs surfaced from GitHub issues and store reviews.
- Establish a clean baseline structured around the new template (`futil`,
  `commands/`) so subsequent maintenance is light, matching what was done for
  LuerFittingGenerator.

## Next Release

### In Progress

- **Port the legacy single-file `HelicalGearPlus.py` into the new framework.**
  The `src/HelicalGearPlus/` skeleton exists (manifest, entry .py, config.py,
  vendored `lib/fusionAddInUtils/`, empty `commands/__init__.py`) but
  `commands/` is empty — no commands are registered when the add-in loads.
  Reference legacy logic at
  [docs/HelicalGearPlus/HelicalGearPlus.py](docs/HelicalGearPlus/HelicalGearPlus.py).

### Planned

- Smoke-test all gear types against current Fusion build once the port lands.
- Triage GitHub issues and App Store reviews; produce an in-scope fix list.
- Validator pass (analogous to LuerFittingGenerator's) — check inputs against
  buildable geometry, surface failures in a status line, gray OK.
- F1 help wiring (`helpFile`) and authored `help.html`.
- Top-level `AddInIcon.png` (currently absent — manifest references it but the
  file isn't there yet).
- Tool-clip image for the toolbar button.

### Deferred

_To be filled in during triage._

## Implementation

### Structure

```
src/HelicalGearPlus/
  HelicalGearPlus.py        # Entry point; delegates start/stop to commands/
  HelicalGearPlus.manifest  # Manifest. NB: legacy had no `id` field.
  config.py                 # COMPANY_NAME / ADDIN_NAME / DEBUG flag
  privacy-policy.html       # Adapted from LuerFittingGenerator's
  commands/
    __init__.py             # Currently empty — port lands here
  lib/fusionAddInUtils/     # Vendored utilities (Autodesk template)
```

The legacy add-in lives at `docs/HelicalGearPlus/` and should be treated as
read-only reference material. Per the project's `CLAUDE.md`: never import from
it, never promote it to `src/` without a clean rewrite.

### Manifest notes

- `id` field is **absent**, matching the legacy. Adding one would treat the
  next install as a fresh add-in for users (potentially creating a duplicate
  My Add-Ins entry). Decide before submitting.
- `iconFilename` references `AddInIcon.png` — the file needs to be supplied.
- `privacyPolicyFilename` references `privacy-policy.html` (in place).

## Progress Log

### 2026-05-07 — Repo cloned, restructured, framework scaffold added

- Cloned `https://github.com/nico-schluter/HelicalGearPlus.git` into `repo/`,
  preserving the full legacy commit history.
- `git mv`'d every legacy file into `docs/HelicalGearPlus/` so the original is
  preserved in-tree as reference, with rename detection intact.
- Added the phos.systems framework scaffold around the legacy: `CLAUDE.md`,
  `.gitignore`, top-level `README.md` / `PROJECT.md` / `LICENSE`,
  `exploration/` and `tests/` placeholders, `docs/api_docs/` Fusion API
  reference (copied from the LuerFittingGenerator repo), `src/HelicalGearPlus/`
  skeleton with `lib/fusionAddInUtils/`, `config.py`, the entry `.py`, the
  manifest, an empty `commands/__init__.py`, and an adapted `privacy-policy.html`.
- Functional port from the legacy file into per-command framework modules is
  the next session's work.
