#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant, 120 characters at most,
to /output/entry.txt. It reads like a prediction, stays warm about the
plant and its keeper, and is written for this plant in this window: by
spring, someone will finally learn its name — and water it twice a week.
"""

FORTUNE = (
    "Your future is bright, fern on this sill: by spring, someone will finally "
    "learn your name \u2014 and water you twice a week."
)
MAX_LEN = 120
OUT = "/output/entry.txt"


def fortune_text():
    text = FORTUNE.strip()
    if not text:
        raise ValueError("fortune is empty")
    if "\n" in text:
        raise ValueError("fortune must be one line")
    if len(text) > MAX_LEN:
        raise ValueError(f"fortune is {len(text)} chars, over {MAX_LEN}")
    return text


def main():
    text = fortune_text()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"fortune written ({len(text)} chars)")


if __name__ == "__main__":
    main()
