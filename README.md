# Useful Tools

A set of useful tools written in various languages to accelerate the workflow
in both Windows and Linux

## Index

- [batch_rename](#batch_rename)
- [secret_gen](#secret_gen)
- [refind](#refind)

## batch_rename

Rename all files in the current directory at once changing every occurrence of
`old` with `new`

### Usage

`python3 batch_rename.py <old> <new>`

### Examples

- Change every occurrence of "wrong" in filenames (e.g. `file_wrong.txt`) to
"right" (e.g. `file_right.txt`)

```bash
python3 batch_rename.py "wrong" "right"
```

### TODO

- add "case insensitive search" flag

---

## secret_gen

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

---

## refind

Search for the given pattern in all files found within the given path and its subdirectories

### Usage

`python3 refind.py [OPTIONS] <path> <pattern>`

Options:

- `-c`: maximum number of files to find
- `-r`: search all the subdirectories of the specified path

![NOTE]
> `pattern` is parsed as a raw string, so characters like parenthesis, brackets
> and `.*?` must be escaped (e.g. `\)`, `\.`) if you want them to be read as
> normal symbols, otherwise they will be parsed as special flags

### Examples

- Search in the Desktop folder for files containing a word of at least one lowercase
letter

```bash
python3 refind.py "~/Desktop" "[a-z]+"
```

- Search recursively in `./folder` for all the files containing the word "word"

```bash
python3 refind.py -r "./folder" "word"
```

- Search recursively in the root folder for maximum 10 files containing a three-digit number

```bash
python3 refind.py -r -c 10 "/" "\b[0-9]{3}\b"
```
