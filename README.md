# Useful Tools

A set of useful tools written in various languages to accelerate the workflow
in both Windows and Linux

---

# Tools Description

## batch_rename.py

Rename all files in the current directory at once changing every occurrence of
`old` with `new`

### Usage

`python3 batch_rename.py <old> <new>`

### Examples

- Change every occurrence of "wrong" (e.g. `file_wrong.txt`) in filenames to
    "right" (e.g. `file_right.txt`)

    ```bash
    python3 batch_rename.py "wrong" "right"
    ```

### TODO

- add "case insensitive search" flag

---

## secret_gen.py

Generate random, cryptographically secure passwords and PINs

### Usage

`python3 secret_gen.py <PASS|PIN> <length>`

### Examples

- Generate a 20-character-long password

    ```bash
    python3 secret_gen.py PASS 20
    ```

- Generate a 6-digit-long PIN

    ```bash
    python3 secret_gen.py PIN 6
    ```
