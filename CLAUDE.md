# ttyper (Asciiverse packaging)

Max Niederman's ttyper (Rust, Ratatui, MIT), packaged for the Asciiverse
catalog (id `ttyper`, kind `game`, genre `typing`). Not our code: no code
changes so far; list any in PATCHES.md.

- `upstream` is github.com/max-niederman/ttyper (branch `master`); ours is
  branch `asciiverse`, `origin` github.com/theasciiverse/ttyper.
- Release: tag `v<upstream version>+<upstream commit date>-av.<n>` (first
  `v1.6.0+20260323-av.1`) and push it; `.github/workflows/asciiverse-release.yml`
  builds Linux musl, macOS and Windows. Upstream's workflows are removed
  because their deploy job fires on any `v*` tag.
- Preview: `asciiverse/record-preview.sh target/release/ttyper` (asciinema 3,
  tmux): drive.py reads the prompt from a tmux pane and types it, about
  37 s with the results screen.
