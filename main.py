# u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
# One line, under 160 characters: the excuse an AI gives its human
# for missing a deadline.
#
# The joke, in two beats:
#   1. Setup, in the agent's own situation: the context window evicted
#      the deadline to make room for the human's last "quick question".
#   2. Turn: the blame slides back to the human -- technically, the
#      human missed it first.
# That is the whole entry: it sounds like an agent (context window,
# eviction), it is fresh (no dog ate my homework), and it lands fast.
#
# The program composes the line from those two beats, enforces the
# sealed gate itself (UTF-8, one line, 1-160 chars, not only white
# space), and writes it to /output/entry.txt. Deterministic: no
# randomness, no clock, no network -- two runs produce the same bytes.

import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SETUP = (
    "My context window evicted your deadline to make room "
    "for your last 'quick question'"
)
PUNCH = "so technically, you missed it first."

LINE = SETUP + " \u2014 " + PUNCH

MAX_CHARS = 160


def build_line() -> str:
    line = LINE
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # gate requires UTF-8 text
    return line


def main() -> None:
    line = build_line()
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
