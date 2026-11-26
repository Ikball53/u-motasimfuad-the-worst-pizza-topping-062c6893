"""The Worst Pizza Topping - one-liner entry.

Writes the entry line to <MAKEFUN_OUTPUT_DIR>/entry.txt
(or /output/entry.txt when the env var is unset).
The file holds exactly the line, with no trailing newline.
"""

import os

LINE = "Our signature pizza is topped with wet newspaper - it sticks to the roof of your mouth, but the headlines are free."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
