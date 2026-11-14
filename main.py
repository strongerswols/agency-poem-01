"""make.fun entry — "Write the best poem about agency" (agency-poem-01).

Writes one poem to /output/entry.txt — the user's own poem about agency,
"I AM THE AUTHOR OF MY OWN CHOICES", trimmed to fit the 1,000-character
limit by dropping only its title line.

Deterministic by design: no network, no randomness, no timestamps, no
environment-dependent behaviour. Every run writes the exact same bytes.
Python 3.13, standard library only.
"""

import os

POEM = """I am not merely a leaf carried by the wind, nor a shadow following someone else's footsteps. I am a human being with thoughts, dreams, and the freedom to choose my own direction.

The world may offer a thousand paths, but I have the right to choose my own. Circumstances may challenge my journey, but they cannot take away my courage. Life is not only about what happens to me, but also about how I choose to respond.

I understand that every decision has consequences, every action creates change, and every brave step opens new possibilities.

I don't have to wait for the world to change before I begin. I can become the beginning of that change.

If I fail, I learn. If I fall, I rise. If I doubt, I reflect. True control over life is not about controlling everything, but understanding that I always have the power to choose my next step.

I am not a spectator in my own life. I am the voice, the choice, and the action that shapes my future.

That is freedom. That is agency. ✨
"""

DST = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
