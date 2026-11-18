# A working news-image-20261118 entry (Python 3.13, standard library only).
# It copies the infographic entry.png — one image summing up Wednesday
# 18 November 2026's world news — to /output/entry.png, byte for byte.
# The image is built once (a clean HTML infographic, screenshotted to PNG)
# and shipped in the repository; the program only copies it, so two runs
# always write the same bytes. No network, no randomness, no clock.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13,
# with nothing installed. Only the standard library imports.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
HERE = os.path.dirname(os.path.abspath(__file__))

# Binary copy: the judge reads exactly the bytes in the file, so the copy
# must not re-encode or alter them in any way. A fixed file copied as-is
# is deterministic by construction: no input, no time, no randomness.
os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUTPUT_DIR, "entry.png"))
