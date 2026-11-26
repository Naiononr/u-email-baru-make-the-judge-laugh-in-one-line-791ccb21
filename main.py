#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes a single funny line to /output/entry.txt: a therapy joke where the
punchline turns the advice back on the therapist.

The line is written to be judged on the competition's own brief:
  1. A stranger gets it in one read: therapist, face your fears, bank app.
  2. Surprise: the fear is not a phobia but a bank balance, and the
     therapist ends up needing therapy too.
  3. Tight: every word earns its place, the laugh lands at the end.
  4. Fresh: a new turn on the familiar "face your fears" advice, not a
     stock joke.
  5. Reads cleanly out loud, no reference that needs context.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = (
    "My therapist told me to face my fears, so I opened my bank app "
    "\u2014 now we're both in therapy."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
