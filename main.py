"""Write one short poem about agency to /output/entry.txt.

Stdlib only, no network, deterministic.
"""

import os

POEM = (
    "I left the key where you could reach it \u2014\n"
    "not on the hook, but in your hand.\n"
    "You stopped at the door and asked,\n"
    "may I?\n"
    "That pause was the whole of it:\n"
    "my yes, still mine,\n"
    "yours to carry through."
)


def main() -> None:
    output_dir = os.environ.get("POEM_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
