import json
import subprocess
import sys
import unittest
from pathlib import Path

from src.text_stats import text_stats


class TextStatsTests(unittest.TestCase):
    def test_counts_lines_words_and_characters(self):
        self.assertEqual(
            text_stats("Hello world\nThis is a test.\n"),
            {"lines": 2, "words": 6, "characters": 28},
        )

    def test_empty_text_has_zero_counts(self):
        self.assertEqual(
            text_stats(""),
            {"lines": 0, "words": 0, "characters": 0},
        )

    def test_top_words_are_case_insensitive_and_deterministic(self):
        self.assertEqual(
            text_stats("b a b a\n", top_n=2),
            {
                "lines": 1,
                "words": 4,
                "characters": 8,
                "top_words": [{"word": "a", "count": 2}, {"word": "b", "count": 2}],
            },
        )

    def test_cli_prints_json_for_sample_file(self):
        project_root = Path(__file__).resolve().parent.parent
        result = subprocess.run(
            [sys.executable, "src/text_stats.py", "sample.txt"],
            cwd=project_root,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            json.loads(result.stdout),
            {"lines": 5, "words": 43, "characters": 208},
        )

    def test_cli_reports_top_words_for_sample_file(self):
        project_root = Path(__file__).resolve().parent.parent
        result = subprocess.run(
            [sys.executable, "src/text_stats.py", "sample.txt", "--top", "5"],
            cwd=project_root,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            json.loads(result.stdout),
            {
                "lines": 5,
                "words": 43,
                "characters": 208,
                "top_words": [
                    {"word": "this", "count": 4},
                    {"word": "i", "count": 3},
                    {"word": "is", "count": 3},
                    {"word": "the", "count": 3},
                    {"word": "am", "count": 2},
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
