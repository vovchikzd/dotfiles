#!/usr/bin/env python3

import sys, random, re

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))

def main() -> int:
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        sorted_tmp = [get_tuple(line.strip()) for line in tmp.readlines()]

    for _ in range(10):
        random.shuffle(sorted_tmp)

    sTitle, nSize = random.choice(sorted_tmp)
    if '(' in sTitle and ')' in sTitle:
        sAuthor = re.findall(r"\((.*)\)", sTitle)[0]
        sName = re.findall(r"(.*)\s+\(.*\).*", sTitle)[0]
        print(f"{sName} by {sAuthor} ({nSize})")
    else:
        print(f"{sTitle} ({nSize})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
