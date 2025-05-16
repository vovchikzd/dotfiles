#!/usr/bin/env python3

import os, sys

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
    saDirs = ["."]
    saRenamed = 0
    while len(saDirs) > 0:
        sDirectory = saDirs.pop(0)
        for sFile in os.listdir(sDirectory):
            sFilePath = f"{sDirectory}/{sFile}"
            if sFile == 'lost+found':
                continue
            if os.path.isdir(sFilePath):
                saDirs.append(sFilePath)
            elif os.path.isfile(sFilePath):
                try:
                    match sFilePath:
                        case sFileName if " (Z-Library)" in sFileName:
                            sNewName = sFileName.replace(" (Z-Library)", "")
                            os.rename(sFileName, sNewName)
                            saRenamed += 1
                        case sFileName if " (z-lib.org)" in sFileName:
                            sNewName = sFileName.replace(" (z-lib.org)", "")
                            os.rename(sFileName, sNewName)
                            saRenamed += 1
                        case _:
                            continue
                except:
                    print(f"Failed to rename {quoted(os.path.basename(sFile))}", file=sys.stderr)
                    sys.exit(1)
    print(f"Renamed {saRenamed} files")


if __name__ == "__main__":
    main()
