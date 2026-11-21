#!/usr/bin/env python3
"""The poem about permission — make.fun bounty entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. No network, no input, fully deterministic.
"""

import os

POEM = """May I?

Two words, and the world tilts.
My hands can open doors —
I only lack the right to turn the key.

You say yes.
The key is mine,
not taken, given:
palm to palm, warm as a coin.

The secret no lock knows:
the asking is the gift.
Your yes comes back to you
in all I do.
"""


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} code points, must be 1-280"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
