# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

ECE 474 (Embedded Microcomputer Systems) course materials for UW Spring 2026. Source files produce three output formats: handout PDFs (`.h`), notes PDFs (`.n`), slides (`.s`), and a combined course notes pack.

## Build System

### The `.shn` preprocessor

Source files use a custom Perl preprocessor (`coursetex`, installed system-wide). `.shn` files are multi-stream LaTeX: lines beginning with `<tag>` are selectively included in output streams:

| Tag | Streams included |
|-----|-----------------|
| `<s>` | slides only |
| `<h>` | handouts only |
| `<n>` | notes only |
| `<c>` | combined notes pack only |
| `<shn>` | slides, handouts, notes (NOT combined) |
| `<hnc>` | handouts, notes, combined |
| `<chn>` | combined, handouts, notes |
| `<*tag>` | starts a block for those streams (until next `<*>`) |
| `<!tag>` | excludes those streams |

Lines without a `<>` prefix go to **all** streams.

`<stream, c>` at the top of a `.shn` file marks it as content to be combined into the notes pack (not a standalone document for the `c` stream).

### Building outputs

**Combined notes pack** (primary student document):
```bash
./gen_tex_files          # runs: coursetex --out c <file>.shn for each chapter
pdflatex 474ECE_NotesPack_Sp26.tex
```

**Individual chapter handout/notes/slides:**
```bash
coursetex --out h Cprog.shn    # generates Cprog.h.tex
coursetex --out n Cprog.shn    # generates Cprog.n.tex
coursetex --out s Cprog.shn    # generates Cprog.s.tex
pdflatex Cprog.h.tex
```

**Scheduler worksheets** (standalone `.tex`, no preprocessing needed):
```bash
pdflatex SchedChartV2.tex
pdflatex SchedulerExamples_IOPS/Ex01_SchedChart.tex
```

### Generated files (not version controlled)
`*.c.tex`, `*.n.tex`, `*.s.tex`, `*.h.tex` are all generated — edit only the `.shn` source.

## Key Architecture

### Notes pack structure (`474ECE_NotesPack_Sp26.tex`)
A `book`-class LaTeX document that `\input`s the `.c.tex` generated files in chapter order. The package preamble here applies to all combined content — packages needed by any `.c.tex` content (e.g., `pdfcomment`) must be loaded here, not just in the `.shn` preambles.

### Package loading caveat
`<shn>` in a preamble covers slides/handouts/notes but **not** the `c` (combined) stream. If a package is needed in the notes pack, add it to **both** the `<shn>` lines in `.shn` files AND to `474ECE_NotesPack_Sp26.tex` directly.

### Accessibility work (in progress)
PDF accessibility changes applied so far:
- `[T1]{fontenc}` + `lmodern` — proper font encoding, Latin Modern appearance
- `[utf8]{inputenc}`, `[english]{babel}` — encoding and language
- `hyperref` with full metadata (title, author, language, subject, keywords per file)
- `colorlinks=true, linkcolor=blue` — clickable colored links
- `pdfcomment` + `\pdftooltip{}{}` wrapping all `\includegraphics` calls — image alt text

Alt text guesses are marked `*\#*\#Guess by Claude.ai:` in the source. Search for `Guess by Claude` to find items needing human review.

### Chapter → `.shn` file mapping
| Chapter | File |
|---------|------|
| Introduction | `474_IntroW22.shn` |
| C Program Structure | `Cprog.shn` |
| Pointers | `Pointers.shn` |
| Constants/Defines | `ConstDef.shn` |
| Schedulers | `Schedulers.shn` |
| Scheduler Implementation | `SchedImplementation.shn` |
| Hardware and I/O | `Hardware_IO.shn` |
| Interrupts | `Interrupts.shn` |
| Serial Communication | `Serial.shn` |
| Secure Coding | `Secure.shn` |
| Micro-C OS/II | `MicroCos.shn` |
| Critical Sections | `CritSect.shn` |
| USB | `USB.shn` |

### Figure directories
Each chapter has a corresponding `*_figs/` directory for its images. Numbered `.eps` files (e.g., `hwio_figs/00156.eps`) are scanned figures from external sources; named `.png` files are other graphics.
