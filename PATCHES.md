# Changes from upstream

This is the Asciiverse packaging of [ttyper](https://github.com/max-niederman/ttyper)
by Max Niederman and contributors (MIT, `LICENSE.md`), a typing test for
the terminal in Rust and Ratatui. Upstream is the `upstream` remote; this
build is upstream's `master` at `e218bad` (2026-03-23), 1.6.0 plus the
languages and fixes since (Korean, Russian, Thai, SQL, `--no-backspace`,
an error message instead of a panic for an empty test). The `asciiverse`
branch carries the changes below.

## Code

None. ttyper is built exactly as upstream has it.

## Packaging

- `.github/workflows/asciiverse-release.yml`: av archives for Linux
  (static musl, x86-64 and ARM64), macOS (Intel and Apple silicon) and
  Windows (x86-64 and ARM64), plus SHA256SUMS.
- Upstream's workflows (`deploy.yml`, `rust.yml`) are removed on this
  branch: the deploy job fires on any `v*` tag, ours included, and this
  repository only packages.
- `asciiverse/record-preview.sh` and `asciiverse/drive.py`: the catalog
  preview, a default test typed by a script at a human pace.
