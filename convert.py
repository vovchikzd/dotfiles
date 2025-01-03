#!/usr/bin/env python3

import os, sys, subprocess, humanize

saFormats: list[str] = [".webm", ".mkv", ".mp4", ".avi", ".ts"]
saPathsToIgnoge: list[str] = list()
sSuffix: str = ".converted.webm"
sTargetExt: str = ".webm"
nFreedUpSpace: int = 0


def clearPath(path: str) -> str:
    result: str = path
    if result[-1] == "/":
        result = result[:-1]
    if result[:2] != "./":
        result = "./" + result
    return result


def getFiles(sStartDir: str) -> list[str]:
    saDirectories: list[str] = [sStartDir]
    saFiles: list[tuple[int, str]] = list()
    while len(saDirectories) > 0:
        sWorkingDirectory = saDirectories.pop(0)
        for sFile in os.listdir(sWorkingDirectory):
            sWorkingFile = f"{sWorkingDirectory}/{sFile}"
            if sWorkingFile not in saPathsToIgnoge:
                if os.path.isdir(sWorkingFile):
                    saDirectories.append(sWorkingFile)
                elif (os.path.isfile(sWorkingFile) 
                      and os.path.splitext(sWorkingFile)[1] in saFormats
                      and sSuffix not in sWorkingFile):
                    saFiles.append((os.path.getsize(sWorkingFile), sWorkingFile))
    saFiles.sort(reverse=True)
    return list(map(lambda x: x[1], saFiles))


def deleteBiggerFile(sFirstFile: str, sSecondFile: str):
    nFirstFileSize: int = os.path.getsize(sFirstFile)
    nSecondFileSize: int = os.path.getsize(sSecondFile)
    sFileToDelete: str = sFirstFile if nFirstFileSize > nSecondFileSize else sSecondFile
    bIsRename: bool = False if sSuffix in sFileToDelete else True
    os.remove(sFileToDelete)
    if bIsRename:
        global nFreedUpSpace
        nFreedUpSpace += abs(nFirstFileSize - nSecondFileSize)
        os.rename(sSecondFile, sSecondFile.replace(sSuffix, sTargetExt))


def convertFiles(saFiles: list[str]):
    nFileNumbers: int = len(saFiles)
    for counter, sFile in enumerate(saFiles, 1):
        sNewFileName: str = f"{os.path.splitext(sFile)[0]}{sSuffix}"
        subprocess.run("clear")
        print(f"\033[0;33mConverting file {counter} of {nFileNumbers} ({round((counter / nFileNumbers) * 100, 2)}%)\033[0m")
        try:
            completedProcess = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-i", sFile, sNewFileName], capture_output=False)
        except:
            print()
            sys.exit(1)
        deleteBiggerFile(sFile, sNewFileName)


def main():
    sWorkingDir: str = "."
    bShowOnly = False
    args: list[str] = sys.argv[1:]
    while len(args) != 0:
        sArgument = args.pop(0)
        match sArgument:
            case "-s":
                bShowOnly = True
            case "-d" if len(args) > 0:
                sPassedDir = clearPath(args.pop(0))
                if os.path.isdir(sPassedDir):
                    sWorkingDir = sPassedDir
                else:
                    print(f"\033[0;31m{sPassedDir} is not a directory", file=sys.stderr)
                    sys.exit(1)
            case "-i" if len(args) > 0:
                saPathsToIgnoge.append(clearPath(args.pop(0)))
            case _:
                print("\033[0;31mDon't know such argument or too few arguments passed\033[0m", file=sys.stderr)
                sys.exit(1)

    saFilesToConvert: list[str] = getFiles(sWorkingDir)
    if bShowOnly:
        for sFile in saFilesToConvert:
            sQuotes = "\"" if "'" in sFile else "'"
            print(f"{sQuotes}{sFile}{sQuotes}")
        print()
        print(f"\033[0;34mNuber of files: {len(saFilesToConvert)}\033[0m")
        sys.exit(0)

    convertFiles(saFilesToConvert)
    if nFreedUpSpace != 0:
        print()
        print(f"\033[0;34mFreed up {humanize.naturalsize(nFreedUpSpace, binary=True)}\033[0m")

if __name__ == "__main__":
    main()
