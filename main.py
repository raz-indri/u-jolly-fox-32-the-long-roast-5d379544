"""The Long Roast — one line roasting my own AI agent.

The program writes a single deterministic line to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent burned 40,000 tokens reasoning, retried the same failing "
    "tool call 38 times, then edited the wrong file and called it a "
    "refactor."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
