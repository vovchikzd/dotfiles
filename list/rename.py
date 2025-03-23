#!/usr/bin/env python3

import os

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


def main():
    saFilesToRename = [sFile for sFile in getFiles() if 'Z-Library' in sFile or 'z-lib.org' in sFile]
    for sFile in saFilesToRename:
        sNewName = sFile.replace(" (Z-Library)", '') if 'Z-Library' in sFile else sFile.replace(" (z-lib.org)", '')
        os.rename(sFile, sNewName)

if __name__ == "__main__":
    main()
