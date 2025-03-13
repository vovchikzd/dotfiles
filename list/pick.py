#!/usr/bin/env python3

import sys, random, re, subprocess

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))

def getRes(sTitle, nSize):
    if '(' in sTitle and ')' in sTitle:
        sAuthor = re.findall(r"\((.*)\)", sTitle)[0]
        sName = re.findall(r"(.*)\s+\(.*\).*", sTitle)[0]
        return f"{sName} by {sAuthor} ({nSize})"
    else:
        return f"{sTitle} ({nSize})"

def main() -> int:
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        sorted_tmp = [get_tuple(line.strip()) for line in tmp.readlines()]

    # for _ in range(100):
    #     random.shuffle(sorted_tmp)

    print(getRes(*random.choice(sorted_tmp)))

    return 0


if __name__ == "__main__":
    sys.exit(main())
