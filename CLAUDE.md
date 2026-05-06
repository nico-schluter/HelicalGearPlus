# Fusion 360 Add-In

Autodesk Fusion 360 extension. All production code lives under `src/`. Everything else is support, exploration, or documentation.

## Project structure

```
src/                  # Production add-in code (the ONLY code that ships)
tests/                # Test files
docs/                 # Fusion 360 API reference docs (markdown)
exploration/          # Prototypes, proof-of-concept scripts, abandoned approaches
  scratch/            # Standalone experiment scripts (.py) — no notebooks
  notes/              # Problem-solving notes (.md)
PROJECT.md            # Project overview, goals, feature targets, progress updates
```

**Critical distinction:** `exploration/` is reference material — never import from it, never promote it to `src/` without a clean rewrite. When creating exploratory code, always place it in `exploration/` with a descriptive name and a brief comment header explaining its purpose.

## Change philosophy

**No hotfixes. No local band-aids.** Every change to `src/` must be a deliberate improvement over the previous state.

Before modifying production code:
1. Understand the root cause — not just the symptom.
2. Consider whether the proposed change is actually better than what exists, including edge cases and interactions with other code.
3. Test for regression: does this break anything that was working?
4. If an approach isn't producing good results after a reasonable effort, **stop and try a different approach** rather than layering fixes on a flawed solution.

Use version control. Commit working states before attempting changes so we can compare and revert. Prefer clean, well-reasoned changes over fast ones.

## Problem solving (algorithms & geometry)

Much of this work involves non-trivial algorithms and geometric reasoning. Do NOT try to solve these intuitively or directly in `src/`.

For non-trivial algorithmic or geometric problems:
1. **Work it out mathematically first.** Write derivations, define variables, prove correctness on paper before writing code.
2. **Keep notes** in `exploration/notes/{problem-name}.md` — include the mathematical reasoning, diagrams (described textually), edge cases, and why the chosen approach works.
3. **Experiment in isolation** using standalone scripts in `exploration/scratch/{problem-name}.py`. Use plain `.py` files, not Jupyter notebooks — they are simpler to create, edit, run, and diff. Validate the algorithm on toy inputs before touching production code.
4. Only move to `src/` once the approach is validated and understood.

## Documentation maintenance

`PROJECT.md` contains: what the project is, current goals, feature targets for the next release, deferred features, and implementation summaries.

**After completing any significant change**, update `PROJECT.md` to reflect:
- What changed and why
- Current state of the relevant feature
- Any new insights about the implementation

Do not let `PROJECT.md` go stale. This is a mandatory step, not optional.

## Testing & logging

Fusion 360 API code cannot be unit-tested automatically — it requires manual testing inside Fusion.

To minimize testing cycles:
- **Add verbose logging** during development. Print what the code is doing at each significant step so failures can be pinpointed from a single test run.
- Format log output clearly: include function/step context, input values, computed results.
- Once code is validated and merged, **strip logging back** to essential messages only. No excessive debug output in production, but keep enough to diagnose issues without re-adding instrumentation.

## API reference

Fusion 360 API docs are in `docs/`. Consult them before writing API calls — don't guess at method signatures or object hierarchies.
