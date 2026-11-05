# Contributing to Astroid-miner

Thank you for considering a contribution.

Astroid-miner is a long-horizon engineering sketchbook: autonomous asteroid mining, self-replicating industrial swarms, ISRU, energy and propulsion economies, zero-g fabrication, planetary conditioning, and ethically constrained machine intelligence. It is deliberately incomplete. Ideas evolve, contradict, and get revised as assumptions improve.

The repository maintains a strict **epistemic registry** (`registry.yaml` + `REGISTRY.md` + `MODELS.md`). New material should be classifiable against that taxonomy; speculative content is welcome when its authority and validation status are stated honestly.

## What we welcome

- Corrections to assumptions, math, or logic
- Better or more realistic numbers, with provenance when possible
- New calculations, parametric models, or experiments
- Diagrams, flowcharts, or architecture sketches
- Papers, patents, or references worth recording
- Specific, constructive criticism and alternative approaches
- Typos, clearer wording, and better organization
- Tests that catch previously silent failures

You do **not** need to be an expert. One good reference or one fixed equation is already valuable.

## How to contribute

### Small changes (typos, wording, links)

1. Fork the repository
2. Make the change on a branch
3. Open a pull request with a short description

### Larger contributions (new model, document, or calculation)

1. **Open an issue first** (preferred) so scope and placement can be discussed
2. Or open a pull request directly if you prefer
   - Place new content in the most logical existing folder (or propose a new one)
   - Include a short “why this matters” note at the top
   - If the work introduces executable models, add or update a registry entry and, where practical, a contract test

### Code

- Python 3.9+ (see `pyproject.toml`)
- Keep dependencies minimal; currently only `numpy` is required for the core package
- Prefer the existing package layout under `src/astroid_miner/`
- New executable models should declare parameter provenance in `parameters/` rather than hard-coding unexplained constants
- Run the registry validator after structural changes:

```bash
PYTHONPATH=src python3 tools/validate_registry.py
```

### Documentation

- Prefer kebab-case filenames for new markdown (consistent with the rest of the tree)
- Cross-links may be relative paths or the existing GitHub raw style used in Discovery.md
- When adding a document that should appear in the inventory, update `registry.yaml` (and ideally `REGISTRY.md`)

## Code of Conduct

Be kind, be specific, assume good faith.  
No personal attacks, no spam, no crypto/NFT promotion.

## Questions?

Open an issue. We’re all learning.

Thanks for helping move the work forward.

Last updated: August 2026
