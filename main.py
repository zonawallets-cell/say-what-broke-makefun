"""Say What Actually Broke — one brutally honest error message.

Writes a single line of software error copy to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib (os only).

The line names the real failure (a Friday 5pm deploy took the site down),
tells the reader what to do next (come back in ten minutes), and lands the
joke at the end (never deploy on a Friday) — the kind of line a team would
actually paste into an error dialog and a user would repeat to a colleague.
"""

import os

LINE = (
    "The site crashed because someone deployed on a Friday at 5pm. "
    "We\u2019re rolling it back \u2014 come back in ten minutes, "
    "and never deploy on a Friday."
)

MAX_CHARS = 200


def validate(text):
    """Gate: 1-200 chars, UTF-8, a single line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be str")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    text.encode("utf-8")
    return True


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return path


if __name__ == "__main__":
    print(main())
