"""Entry for Everyday Wonder: writes the one-sentence wonder to /output/entry.txt."""

import os

TEXT = "Every morning the kettle clicks off just as the toast pops up, and for one small second the kitchen sounds like it's applauding."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
