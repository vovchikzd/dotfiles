#!/usr/bin/env python3

import os, sys

def getFiles(spDirectory: str = '.', saFiles: list[str] = None) -> list[str]:
    if saFiles is None:
        saFiles = list()
    saDirs: list[str] = [spDirectory]
    while len(saDirs) > 0:
        sDirectory = saDirs.pop(0)
        for sFile in os.listdir(sDirectory):
            sFilePath = f"{sDirectory}/{sFile}"
            if os.path.isfile(sFilePath):
                saFiles.append(sFilePath)
            elif os.path.isdir(sFilePath):
                saDirs.append(sFilePath)
    return saFiles

def isQuoted(sToCheck):
    tQuotes = ("'", '"')
    return (len(sToCheck) > 1
            and sToCheck[0] == sToCheck[-1]
            and sToCheck[0] in tQuotes)

def quoted(sStr):
    if len(sStr) == 0:
        return "''"
    if isQuoted(sStr):
        return sStr
    sQuote = '"' if "'" in sStr else "'"
    return f"{sQuote}{sStr}{sQuote}"


def main():
    saFilesToRename = [sFile for sFile in getFiles() if 'Z-Library' in sFile or 'z-lib.org' in sFile]
    saRenamed = list()
    for sFile in saFilesToRename:
        sNewName = sFile.replace(" (Z-Library)", '') if 'Z-Library' in sFile else sFile.replace(" (z-lib.org)", '')
        try:
            os.rename(sFile, sNewName)
        except:
            print(f"Failed to rename {quoted(os.path.basename(sFile))}")
            sys.exit(1)
        saRenamed.append((os.path.basename(sFile), os.path.basename(sNewName)))
    for sOldName, sNewName in saRenamed:
        print(f"{quoted(sOldName)} -> {quoted(sNewName)}")
    print(f"Renamed {len(saRenamed)} files")

if __name__ == "__main__":
    main()
