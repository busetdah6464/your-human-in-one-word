#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes a single original word describing the human the entrant works
for (the boss / client / manager who signs off on the work) to
/output/entry.txt. Deterministic, standard library only.
"""

import os

WORD = "Signoffasaurus"  # one word, 15 chars: a boss whose sign-off takes ages


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
