import argparse
import re
import sys
from pathlib import Path


def find_valid_files(path: Path, regex: str, recursive: bool, count: int) -> list[Path]:
    if not path.is_dir(): sys.exit("[!] ERROR: path must be a directory")

    files = list()
    pattern = "**/*.*" if recursive else "*"

    for file in path.glob(pattern):
        if file.is_file():
            try:
                with file.open("r", encoding="utf-8") as f:
                    if re.search(rf"{regex}", f.read()): files.append(file)
            except UnicodeDecodeError:
                continue

    return files[:count] if count else files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for the given pattern in all the files within the given path and its subdirectories",
    )
    parser.add_argument("path", help="directory to search for files")
    parser.add_argument("pattern", help="pattern to search in the files")
    parser.add_argument("-r", "--recursive", action="store_true", help="search for files recursively")
    parser.add_argument("-c", "--count", type=int, help="max number of times to find pattern")

    args = parser.parse_args()
    p = Path(args.path)
    files = find_valid_files(p, args.pattern, args.recursive, args.count)

    if not files: sys.exit("[-] No files found")

    print(f"[*] Found {len(files)} files")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file.absolute()}")
