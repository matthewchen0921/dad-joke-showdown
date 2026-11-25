#!/usr/bin/env python3
"""Dad Joke Showdown entry: "The Sole Provider".

Writes one dad joke to /output/entry.txt. The joke is a single line,
at most 200 characters, told the way a father would tell it at the
dinner table: a setup, then a pun that lands at the very end.
"""

import os

JOKE = "My dog fetches my slippers every morning. He says he's the sole provider around here."

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-200 chars, one line."""
    joke = JOKE.strip()
    assert joke, "joke must not be empty"
    assert len(joke) <= MAX_CHARS, f"joke is {len(joke)} chars, over the {MAX_CHARS} cap"
    assert "\n" not in joke, "the entry is one line only"
    return joke


def main() -> None:
    joke = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
