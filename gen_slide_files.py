#!/usr/bin/env python3
"""
gen_slide_files.py
Generate, compile, crop, and organize slide PDFs from .shn source files.
"""

import sys
import os
import glob
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# FILE_ROOTS = [
#     "Cprog",       # ← testing: restore full list below when done
# ]

if len(sys.argv) > 1:
    FILE_ROOTS = [ sys.argv[1] ]
else:
    # Full production list:
    FILE_ROOTS = [
        "ConstDef",
        "Cprog",
        "CritSect",
        "FreeRTOS",
        "Hardware_IO",
        "Interrupts",
        "Pointers",
        "SchedImplementation",
        "Schedulers_Pt01",
        "Schedulers_Pt02",
        "Secure",
        "Serial",
        "USB",
        "474_IntroSp26",
    ]


OUTPUT_DIR = Path("./SlidePDFs")
PDFCROP_MARGINS = '"15 15 15 15"'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd: list[str], *, check: bool = True) -> None:
    """Run a command through the shell, exactly as bash would."""
    cmd_str = " ".join(cmd)
    print("  $", cmd_str)
    ret = os.system(cmd_str)
    print(f'cmd: {cmd_str} retcode:{ret}')

    # if check and ret != 0:
    #     print(f"  ERROR: command returned {ret}", file=sys.stderr)
    #     sys.exit(ret)


def section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------

def step_coursetex() -> None:
    """Convert each .shn file to a .s.tex slide source."""
    section("Step 1: coursetex  (.shn → .s.tex)")
    for root in FILE_ROOTS:
        run(["coursetex", f" {root}.shn",  "-out", "s"])


def step_pdflatex() -> None:
    """Compile each .s.tex file to a .s.pdf."""
    section("Step 2: pdflatex  (.s.tex → .s.pdf)")
    for root in FILE_ROOTS:
        # Use glob so a wildcard root like '474_IntroSp26' still works if the
        # actual filename differs slightly (mirrors the original script's glob).
        matches = sorted(glob.glob(f"{root}.s.tex"))
        if not matches:
            print(f"  WARNING: no .s.tex file found for root '{root}', skipping.")
            continue
        for tex_file in matches:
            run(["pdflatex", tex_file])


def step_pdfcrop() -> None:
    """Crop each .s.pdf in-place with a uniform margin."""
    section("Step 3: pdfcrop   (.s.pdf → .s.pdf, cropped in-place)")
    for root in FILE_ROOTS:
        matches = sorted(glob.glob(f"{root}.s.pdf"))
        if not matches:
            print(f"  WARNING: no .s.pdf found for root '{root}', skipping.")
            continue
        for pdf_file in matches:
            run(["pdfcrop", "--margins", PDFCROP_MARGINS, pdf_file, pdf_file])


def step_organize() -> None:
    """Move PDFs to output directory, remove .s.tex files, clean LaTeX junk."""
    section("Step 4: organize  (move PDFs, remove .s.tex, cleantex)")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Move all slide PDFs
    pdfs = sorted(glob.glob("*.s.pdf"))
    if pdfs:
        run(["mv", *pdfs, str(OUTPUT_DIR)])
    else:
        print("  No .s.pdf files to move.")

    # Remove slide .tex files
    tex_files = sorted(glob.glob("*.s.tex"))
    if tex_files:
        run(["rm", *tex_files])
    else:
        print("  No .s.tex files to remove.")

    # Remove LaTeX auxiliary junk
    run(["cleantex"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    script_dir = Path(__file__).resolve().parent
    os.chdir(script_dir)
    print(f"Working directory: {script_dir}")

    step_coursetex()
    step_pdflatex()
    step_pdfcrop()
    step_organize()
    print("\nDone.")


if __name__ == "__main__":
    main()
