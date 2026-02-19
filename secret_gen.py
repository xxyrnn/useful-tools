import secrets
import string
import sys

if len(sys.argv) != 3:
    print("Usage: python3 main.py <PASS|PIN> <length>")
    sys.exit(1)

mode = sys.argv[1].upper()
length = int(sys.argv[2])

if mode == "PASS":
    alphabet = string.ascii_letters + string.digits + "!?@#$&_."
elif mode == "PIN":
    alphabet = string.digits
else:
    print("[!] Invalid mode: choose either PASS or PIN")
    sys.exit(1)

print("Secret Token:", "".join(secrets.choice(alphabet) for _ in range(length)))
