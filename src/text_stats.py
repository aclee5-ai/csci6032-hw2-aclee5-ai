"""Count lines, words, and characters in a UTF-8 text file."""

import argparse
import json
from pathlib import Path
from typing import Dict


def text_stats(text: str) -> Dict[str, int]:
    """Return line, word, and character counts for text."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def main() -> None:
    """Read a UTF-8 file and print its statistics as JSON."""
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the UTF-8 text file")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    print(json.dumps(text_stats(text), sort_keys=True))


if __name__ == "__main__":
    main()
