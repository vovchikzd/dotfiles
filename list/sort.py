#!/usr/bin/env python3

import sys

names = [
        "Лагерлеф", "Sullivan", "Ида Мартин", "Strout", "Galbraith"
         , "Covenant", "Guy Gavriel Kay"
         ]

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))

def is_cross_names(line: str) -> bool:
    res: bool = False
    for name in names:
        if name in line:
            res = True
    return res

def main() -> int:
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        lines: list[tuple[str, int]] = [get_tuple(line.strip()) for line in tmp.readlines()]
        lines.sort(key=lambda tup: (tup[1], tup[0]))
        sorted_tmp = lines

    with open("list.tex", "w") as tord:
        print("\\documentclass[a4paper, 11pt]{proc} % proc для двух колонок\n\\input{preamble.tex}\n", file=tord)
        print("\\begin{document}\n\n\\begin{enumerate}", file=tord)
        for line in sorted_tmp:
            print(f"    \\item {line[0]} -- {line[1]}", file=tord)
            if ("(" not in line[0] or ")" not in line[0]) and not is_cross_names(line[0]):
                print(line)
        print("\\end{enumerate}\n\n\\end{document}", file=tord)
    return 0


if __name__ == "__main__":
    sys.exit(main())
