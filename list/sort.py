#!/usr/bin/env python3

import sys

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))

def main() -> int:
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        sorted_tmp = [get_tuple(line.strip()) for line in tmp.readlines()]

    sorted_tmp.sort(key=lambda tup: (tup[1], tup[0]))
    with open("list.tex", "w") as tord:
        print("\\documentclass[a4paper, 11pt]{proc} % proc для двух колонок\n\\input{preamble.tex}\n", file=tord)
        print("\\begin{document}\n\n\\begin{enumerate}", file=tord)
        for line in sorted_tmp:
            print(f"    \\item {line[0]} -- {line[1]}", file=tord)
            if ("(" not in line[0] or ")" not in line[0]):
                print(f"\033[0;33m{line}\033[0m")
        print("\\end{enumerate}\n\n\\end{document}", file=tord)
    return 0


if __name__ == "__main__":
    sys.exit(main())
