#!/usr/bin/env python3

import os, subprocess, sys

true = True
false = False

class Color:
    NEUTRAL: str = "\033[0m"
    RED: str = "\033[0;31m"

def colored(sToColor: str, color: Color = Color.NEUTRAL) -> str:
    return f"{color}{sToColor}{Color.NEUTRAL}"

def isQuoted(sToCheck: str) -> bool:
    return sToCheck[0] == sToCheck[-1] and sToCheck[0] in ("'", '"')

def quoted(sToQuote: str) -> str:
    if (isQuoted(sToQuote)):
        return sToQuote
    sQuote: str = '"' if "'" in sToQuote else "'"
    return f"{sQuote}{sToQuote}{sQuote}"

def clearPath(path: str) -> str:
    if path == "./" or path == ".":
        return "."
    if path == "../" or path == "..":
        return ".."
    
    result: str = path
    if result[-1] == "/":
        result = result[:-1]
    if result[:2] == "./":
        result = result[2:]
    return result

def main(args: list[str]):
    sWrongFiles: list[str] = list()
    sCurrentDir: str = os.getcwd()
    sSaveDir: str = "/home/vovchik/Disks/1Tb/Audio/Favorites/"
    for arg in args:
        sWorkingFile: str = f"{sCurrentDir}/{clearPath(arg)}"
        if os.path.isfile(sWorkingFile):
            sBaseName: str = os.path.basename(arg)
            subprocess.run(["ln", "-sf", sWorkingFile, f"{sSaveDir}{sBaseName}"], capture_output=True)
        else:
            sWrongFiles.append(arg)

    if len(sWrongFiles) > 0:
        print(f"{colored("Error.", Color.RED)} These files are incorrect, can't create links:")
        for file in sWrongFiles:
            print(f"  {quoted(file)}")

if __name__ == "__main__":
    main(sys.argv[1:])
