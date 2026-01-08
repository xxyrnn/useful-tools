# Useful Tools

A set of useful tools written in various languages to accelerate the workflow
in both Windows and Linux

---

## Tools Description

## batch_rename.py

Usage: `python3 batch_rename.py <old> <new>`

Rename all files in the current directory at once changing every occurrence of
`old` with `new`

Examples:
- change every occurrence of "wrong" (e.g. `file_wrong.txt`) in filenames to
    "right" (e.g. `file_right.txt`)

    ```bash
    python3 batch_rename.py "wrong" "right"
    ```

### TODO:
- add "case insensitive search" flag
