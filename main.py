#!/usr/bin/env python3
"""Cutest picture entry: copy the bundled art to the output directory."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard: the output must be byte-identical to the bundled art.
    if os.path.getsize(SRC) != os.path.getsize(DST):
        print("error: output size differs from bundled art", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
