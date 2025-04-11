#!/usr/bin/env python3

import sys, inspect

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))

def main() -> int:
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        sorted_tmp = [get_tuple(line.strip()) for line in tmp.readlines()]

    sorted_tmp.sort(key=lambda tup: (tup[1], tup[0]))
    with open("list.typ", "w") as outFile:
        print(inspect.cleandoc(
        """#set text(
             size: 8.5pt
             , font: "Hack Nerd Font"
           )
           #set page(margin: (
             top: 5mm
             , bottom: 5mm
             , right: 5mm
             , left: 5mm
           ))
           #set par(
             leading: 0.7em
             , spacing: 1.5pt
           )

           #columns(2, gutter: 0pt)[
        """), file=outFile)
        for line in sorted_tmp:
            print(f"+ {line[0]} -- {line[1]}", file=outFile)
            if ('(' not in line[0] or ')' not in line[0]):
                print(f"\033[0;33m{line}\033[0m")
        print("]", file=outFile)
    return 0


if __name__ == "__main__":
    sys.exit(main())
