import sys

def info(msg: str):
    print(msg)

def warn(msg: str):
    print(f"\033[0;33mWarning:\033[0m {msg}", file=sys.stderr)

def error(msg: str):
    print(f"\033[0;31mError:\033[0m {msg}", file=sys.stderr)
    exit(1)
