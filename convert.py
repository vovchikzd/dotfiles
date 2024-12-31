#!/usr/bin/env python3

import os, sys, subprocess, humanize

saFormats: list[str] = [".webm", ".mkv", ".mp4", ".avi", ".ts"]
sSuffix: str = ".converted.webm"
sTargetExt: str = ".webm"
nFreedUpSpace: int = 0

def getFiles(sStartDir: str) -> list[str]:
    saDirectories: list[str] = [sStartDir]
    saFiles: list[tuple[int, str]] = list()
    while len(saDirectories) > 0:
        sWorkingDirectory = saDirectories.pop(0)
        for sFile in os.listdir(sWorkingDirectory):
            sWorkingFile = f"{sWorkingDirectory}/{sFile}"
            if os.path.isdir(sWorkingFile):
                saDirectories.append(sWorkingFile)
            elif os.path.isfile(sWorkingFile) and os.path.splitext(sWorkingFile)[1] in saFormats:
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
        print(f"\033[0;33mConverting file {counter} of {nFileNumbers}\033[0m")
        completedProcess = subprocess.run(["ffmpeg","-hide_banner", "-i", sFile, sNewFileName], capture_output=False)
        nReturnCode = completedProcess.returncode
        if nReturnCode != 0:
            sys.exit(nReturnCode)
        deleteBiggerFile(sFile, sNewFileName)


def main():
    saFilesToConvert: list[str] = getFiles(os.getcwd())
    convertFiles(saFilesToConvert)
    if nFreedUpSpace != 0:
        print()
        print(f"\033[0;34mFreed up {humanize.naturalsize(nFreedUpSpace, binary=True)}\033[0m")

if __name__ == "__main__":
    main()
