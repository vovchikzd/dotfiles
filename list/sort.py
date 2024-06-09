#!/usr/bin/env python3

def get_tuple(line: str) -> tuple[str, int]:
    tup: list[str] = line.split(" ~ ")
    return (tup[0], int(tup[1]))


def main():
    sorted_tmp: list[tuple[str, int]] = list()
    with open("template.txt", "r") as tmp:
        lines: list[tuple[str, int]] = [get_tuple(line.strip()) for line in tmp.readlines()]
        lines.sort(key=lambda tup: tup[1])
        sorted_tmp = lines

    with open("list.tex", "w") as tord:
        print("\\documentclass[a4paper, 11pt]{proc} % proc для двух колонок\n\\input{preamble.tex}\n", file=tord)
        print("\\begin{document}\n\n\\begin{enumerate}", file=tord)
        for line in sorted_tmp:
            print(f"    \\item {line[0]} -- {line[1]}", file=tord)
            if (("(" not in line[0] or ")" not in line[0])
                    and ("Лагерлеф" not in line[0] and "Sullivan" not in line[0]
                        and "Ида Мартин" not in line[0] and "Strout" not in line[0]
                        and "Galbraith" not in line[0] and "Covenant" not in line[0]
                        and "Guy Gavriel Kay" not in line[0])):
                print(line)
        print("\\end{enumerate}\n\n\\end{document}", file=tord)


if __name__ == "__main__":
    main()
