# Repo cleanup and release note

## Summary

This cleanup keeps the repository in a verified, low-noise state without removing any key business logic or templates.

## Changes

- Normalized project metadata and author naming to the canonical Thai Hai Ly form.
- Removed generated cache folders created by Python test/lint runs.
- Refreshed the primary README status block to reflect the actual green verification state.
- Kept release information brief and factual to avoid clutter.

## Verified status

- `git diff --check`: pass
- `python -m ruff check core tests`: pass
- `pytest -q -ra`: 272 passed, 1 skipped
- `git status --short --branch`: clean on `main`

## Notes

The repository is synced to GitHub and ready for ongoing development work without noisy generated artifacts in the working tree.
