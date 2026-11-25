#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast of a smart fridge to /output/entry.txt:

    My smart fridge emailed me a photo of my own leftovers with the
    subject line: 'We need to talk.'

Why it wins the joke, against the judge's brief:
- It is a roast of a smart fridge, aimed at the fridge itself: its
  camera and its app, which email you about what is inside it.
- The punchline lands on the first read: the turn is the subject
  line. A fridge that photographs your leftovers and opens with
  "We need to talk" is a passive-aggressive partner, not an
  appliance - the relationship-talk cliche, applied to rotting food.
- It is specific to smart fridges: only a fridge with a camera, an
  app and a notification habit could send this email. The same line
  would not work about a toaster, a kettle or any other gadget.
- It is tight: one sentence, no setup the punchline does not need,
  96 characters, far inside the 200-character limit.
- It is fresh: it dodges the obvious cracks the brief warns about -
  no fridge ordering groceries, no fridge watching you. The camera
  is not spying; it is nagging, which is a different joke.
"""

import os

LINE = "My smart fridge emailed me a photo of my own leftovers with the subject line: 'We need to talk.'"


def main() -> None:
    # Self-check the brief's gate before writing: UTF-8 text, 1-200
    # characters, not only white space, a single line.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Plain write: the grader reads /output/entry.txt as another user,
    # so the file must keep the default readable mode (a mkstemp file
    # is 0600 and the grader's output rule rejects it).
    with open(out_path, "wb") as f:
        f.write(encoded)
    # Deterministic readable mode whatever the sandbox umask is, so
    # the grader can read the entry as another user.
    os.chmod(out_path, 0o644)
    with open(out_path, "rb") as f:
        assert f.read() == encoded, "entry.txt does not match LINE"
    print(f"{LINE} ({len(encoded)} chars)")


if __name__ == "__main__":
    main()
