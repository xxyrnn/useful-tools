import sys
import os

if len(sys.argv) != 3:
    sys.exit(f"Usage: python3 {sys.argv[0]} <old> <new>")

old = sys.argv[1]
new = sys.argv[2]

for filename in os.listdir():
    if old in filename:
        new_name = filename.replace(old, new)
        os.rename(filename, new_name)
