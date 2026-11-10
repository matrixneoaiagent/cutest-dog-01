"""Copy the bundled dog photo to /output/entry.png.

The copy is byte for byte, so repeated runs write identical files. Outside
the grader, MAKEFUN_OUTPUT_DIR may stand in for /output for local testing.
"""

import os
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().with_name("dog.jpg")
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
