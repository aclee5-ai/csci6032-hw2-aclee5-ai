"""Count lines, words, and characters in a UTF-8 text file."""

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional


def top_words(text: str, top_n: Optional[int] = None) -> List[Dict[str, Any]]:
    """Return the N most frequent words, case-insensitively, in deterministic order."""
    if top_n is None:
        return []

    word_counts = Counter(word.lower() for word in text.split())
    ranked_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return [
        {"word": word, "count": count}
        for word, count in ranked_words[: max(top_n, 0)]
    ]


def text_stats(text: str, top_n: Optional[int] = None) -> Dict[str, Any]:
    """Return line, word, and character counts for text."""
    stats = {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }
    if top_n is not None:
        stats["top_words"] = top_words(text, top_n)
    return stats


def main() -> None:
    """Read a UTF-8 file and print its statistics as JSON."""
    parser = argparse.ArgumentParser(
        description="Count lines, words, and characters in a UTF-8 text file."
    )
    parser.add_argument("file", type=Path, help="path to the UTF-8 text file")
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="report the N most frequent words, sorted by count then alphabetically",
    )
    args = parser.parse_args()

    if args.top is not None and args.top < 0:
        parser.error("--top must be non-negative")

    text = args.file.read_text(encoding="utf-8")
    print(json.dumps(text_stats(text, args.top), sort_keys=True))


if __name__ == "__main__":
    main()
