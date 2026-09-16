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

Run the tests with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover -s tests
```
