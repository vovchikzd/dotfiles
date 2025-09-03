#!/usr/bin/env python3

import sys, random, re, os, ezodf

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
    sorted_tmp: list[str] = list()
    with open("template.txt", "r") as tmp:
        sorted_tmp = [getRes(*get_tuple(line.strip())) for line in tmp.readlines()]

    ods_file_path = "/home/vovchik/dotfiles/list/Библиотека.ods"
    if os.path.isfile(ods_file_path):
        for row in list(ezodf.opendoc(ods_file_path).sheets[0].rows())[1:]:
            if row[6].value == "нет" or row[6].value == "no":
                sorted_tmp.append(f"{row[2].value} by {row[1].value}")

    print(random.choice(sorted_tmp))

    return 0


if __name__ == "__main__":
    sys.exit(main())
