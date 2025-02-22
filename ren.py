#!/usr/bin/env python3

import sys, os, datetime, re
true = True
false = False

def getSortKey(name):
    sDate = re.findall(r'.*(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d).*', name)[0]
    dDate = datetime.datetime.strptime(sDate, "%Y-%m-%d %H:%M:%S")
    sId = re.findall(r'.*\[(.*)\]', name)[0]
    id = int(sId)
    sExt = os.path.splitext(name)[-1]
    sName = re.findall(r'.*\((.*)\).*', name)[0]
    return (dDate, id, f"{sDate}({sName})[{sId}]{sExt}", name)


def main():
    saFiles = [getSortKey(file) for file in os.listdir()]
    saFiles.sort(reverse=true)
    nAlign = len(str(len(saFiles)))
    for counter, metaInfTuple in enumerate(saFiles, 1):
        sNewName = f"{counter:0{nAlign}}. {metaInfTuple[2]}"
        if sNewName != metaInfTuple[3]:
            os.rename(metaInfTuple[3], sNewName)
            # print(sNewName)


if __name__ == "__main__":
    main()
