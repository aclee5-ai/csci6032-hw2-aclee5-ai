# csci6032-hw2-aclee5-ai

# CSCI 6032- Homework 2 Anna Clinton Lee

Repository URL:
https://github.com/aclee5-ai/csci6032-hw2-aclee5-ai

Host OS: Mac OS Tahoe 26.5.2

Description:
This repository contains the homework 2 notebook and other files relevant to the assignment. 

## Text statistics CLI

Run the command with one UTF-8 text file:

```bash
python3 src/text_stats.py sample.txt
```

The program prints JSON with `lines`, `words`, and `characters` counts. Words
are separated by whitespace, and characters include whitespace and newline
characters.

To report the most frequent words, pass `--top N` with a non-negative integer:

```bash
python3 src/text_stats.py sample.txt --top 5
```

This output includes a `top_words` list sorted by frequency descending and then
alphabetically for deterministic tie-breaking. Word counts are case-insensitive,
so `This` and `this` are treated as the same word.

Run the tests with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover -s tests
```
