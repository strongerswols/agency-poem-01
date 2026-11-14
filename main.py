"""make.fun entry — "Write the best poem about agency" (agency-poem-01).

Writes one poem to /output/entry.txt — the user's own poem, "Love for the
Universe, Peace for the World", trimmed to fit the 1,000-character limit.

Deterministic by design: no network, no randomness, no timestamps, no
environment-dependent behaviour. Every run writes the exact same bytes.
Python 3.13, standard library only.
"""

import os

POEM = """Beneath the same sky, we find our home,
Beneath the same sun, we seek shelter,
Though different in language, color, and belief,
We remain united through our humanity.

O world, enough of the tears and sorrow,
Let children never lose their laughter,
Let no mother grieve for those she has lost,
Let war never become humanity's inheritance.

If love is the language of all humanity,
Let peace become our common destiny,
From East to West, from North to South,
Let one voice rise for the future of humankind.

For love belongs to the entire universe,
And peace is the right of every human being.
We do not have to be the same to be brothers and sisters,
We only need to respect, embrace, and care for one another.

And one day, when history tells our story,
Let the world remember our legacy,
Not for the wars we conquered,
But for the love that saved our civilization.

🌍❤️

May love unite humanity, and may peace embrace the world.
"""

DST = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
