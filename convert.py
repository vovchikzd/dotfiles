#!/usr/bin/env python3

import os, sys, subprocess, humanize, cv2, inspect

nFreedUpSpace: int = 0

def printHelp(file = sys.stdout):
    print(inspect.cleandoc(
        """
        Usage:
            convert [OPTIONS]

            Options:
                -d,                 provide working directory, in which find files (by default cwd)
                -f,                 add format to seart formats list, allow to use multiple time
                -h,  --help         print this help message
                -i,                 paths or files to ignore, allow to use multiple time
                -n,                 if passed old file will be deleted instead of smaller ones
                -p,                 provide processed file from older starts, allow to use multiple time
                -r,                 sort files in reverse order (by default descending)
                -s,                 only read, sort and print files to stdout
                -ss,                only read, sort and print files to stdout, except those from
                                    processed file (see -p option)
                     --scale        provide a height to scale to
                     --save-proc    if passed processed file (see -p option) will not be deleted
                -t,                 provide an extension to convert to (by default is webm)
                --                  all from here will be passed as ffmpeg arguments
        """
    ), file=file)

def clearPath(path: str) -> str:
    if path == "./" or path == ".":
        return "."
    if path == "../" or path == "..":
        return ".."

    result: str = path
    if result[-1] == "/":
        result = result[:-1]
    if result[:2] != "./" and result[0] != "/" and result[:3] != "../":
        result = "./" + result
    return result


def getQuotes(sString: str) -> str:
    return '"' if "'" in sString else "'"


class WorkingInformation:
    saFormats: list[str] = [".webm", ".mkv", ".mp4", ".avi", ".ts"]
    saPathsToIgnoge: list[str] = list()
    saProcessedPaths: list[str] = list()
    sTargetExt: str = ".webm"
    sSuffix: str = None
    sProcessedFile: str = "./processed.txt"
    sWorkingDirectory: str = "."
    bShowOnly: bool = False
    bShowAll: bool = True
    bIsReverse: bool = True
    nOutputHeight: int = None
    saFfmpegArgs: list[str] = list()
    bIsDeleteSmaller: bool = True
    bIsDeleteProcFile: bool = True

    def __init__(self):
        args: list[str] = sys.argv[1:]
        if "--help" in args or "-h" in args:
            printHelp()
            sys.exit(0)
        while len(args) > 0:
            sArgument: str = args.pop(0)
            match sArgument:
                case "-t" if len(args) > 0:
                    sPassedExt = args.pop(0)
                    if sPassedExt[0] != '.':
                        sPassedExt = f".{sPassedExt}"
                    self.sTargetExt = sPassedExt
                case "-s":
                    self.bShowOnly = True
                case "-ss":
                    self.bShowOnly = True
                    self.bShowAll = False
                case "-d" if len(args) > 0:
                    sPassedDir: str = clearPath(args.pop(0))
                    if os.path.isdir(sPassedDir):
                        self.sWorkingDirectory = sPassedDir
                    else:
                        sQuotes: str = getQuotes(sPassedDir)
                        print(f"\033[0;31mInvalid directory {sQuotes}{sPassedDir}{sQuotes}\033[0m", file=sys.stderr)
                        sys.exit(1)
                case "-i" if len(args) > 0:
                    self.saPathsToIgnoge.append(clearPath(args.pop(0)))
                case "-r":
                    self.bIsReverse = False
                case "--scale" if len(args) > 0:
                    self.nOutputHeight = int(args.pop(0))
                case "-f" if len(args) > 0:
                    sPassedExt = args.pop(0)
                    if sPassedExt[0] != '.':
                        sPassedExt = f".{sPassedExt}"
                    self.saFormats.append(sPassedExt)
                case "-n":
                    self.bIsDeleteSmaller = False
                case "--save-proc":
                    self.bIsDeleteProcFile = False
                case "-p" if len(args) > 0:
                    sPassedFile: str = clearPath(args.pop(0))
                    self.sProcessedFile = sPassedFile
                    if os.path.isfile(sPassedFile):
                        with open(self.sProcessedFile, "r") as fileProcessed:
                            global nFreedUpSpace
                            sFirstLine = fileProcessed.readline().strip()
                            nFreedUpSpace += int(sFirstLine) if sFirstLine.isdigit() else 0
                            saReadedLines = [clearPath(line.strip()) for line in fileProcessed.readlines()]
                            if len(saReadedLines) > 0:
                                self.saProcessedPaths.extend([line for line in saReadedLines if os.path.isfile(line) and line not in self.saProcessedPaths])
                case "--":
                    self.saFfmpegArgs = args.copy()
                    args.clear()
                case _:
                    print(f"\033[0;31mInvalid argument or too few arguments passed\033[0m", file=sys.stderr)
                    printHelp(sys.stderr)
                    sys.exit(1)
        self.sSuffix = f".converted{self.sTargetExt}"

    def path(self) -> str:
        return self.sWorkingDirectory

    def isIgnore(self, sPath: str) -> bool:
        return sPath in self.saPathsToIgnoge

    def isNeededFile(self, sPath: str) -> bool:
        return (os.path.splitext(sPath)[1] in self.saFormats
                and self.sSuffix not in sPath)

    def isShowOnly(self) -> bool:
        return self.bShowOnly

    def isShowAll(self) -> bool:
        return self.bShowAll

    def isProcessed(self, sPath: str) -> bool:
        return sPath in self.saProcessedPaths

    def addProcessed(self, sPath: str):
        self.saProcessedPaths.append(sPath)


workInfo: WorkingInformation = None


def getFiles(sStartDir: str) -> list[tuple[int, str]]:
    global workInfo
    saDirectories: list[str] = [sStartDir]
    saFiles: list[tuple[int, str]] = list()
    while len(saDirectories) > 0:
        sWorkingDirectory: str = saDirectories.pop(0)
        if not workInfo.isIgnore(sWorkingDirectory):
            for sFile in os.listdir(sWorkingDirectory):
                sWorkingFile = f"{sWorkingDirectory}/{sFile}"
                if (not workInfo.isIgnore(sFile)
                        and not workInfo.isIgnore(sWorkingFile)):
                    if os.path.isdir(sWorkingFile):
                        saDirectories.append(sWorkingFile)
                    elif (os.path.isfile(sWorkingFile)
                          and workInfo.isNeededFile(sWorkingFile)):
                        saFiles.append((os.path.getsize(sWorkingFile), sWorkingFile))
    saFiles.sort(reverse=workInfo.bIsReverse)
    return list(map(lambda x: x[1], saFiles))


def printFiles(saFiles: list[str]):
    global workInfo, nFreedUpSpace
    saFilesToPrint: list[str] = list() 
    if workInfo.isShowAll():
        saFilesToPrint = [sFile for sFile in saFiles]
    else:
        saFilesToPrint = [sFile for sFile in saFiles if not workInfo.isProcessed(sFile)]

    nNumberOfFiles: int = len(saFilesToPrint)
    print(f"\033[0;34mNuber of files: {nNumberOfFiles}{
        f", Freed up: {humanize.naturalsize(nFreedUpSpace, binary=True, format='%.2f')
    }" if nFreedUpSpace > 0 else ""}\033[0m")
    for sFile in saFilesToPrint:
        sQuotes: str = getQuotes(sFile)
        sQuotedName = f"{sQuotes}{sFile}{sQuotes}"
        print(f"\033[0;32m{sQuotedName}\033[0m" if workInfo.isProcessed(sFile) else sQuotedName)


def removeExtraFile(sFirstFile: str, sSecondFile: str) -> str:
    global workInfo, nFreedUpSpace
    if workInfo.bIsDeleteSmaller:
        taFiles: list[tuple[int, str]] = [(os.path.getsize(sFirstFile), sFirstFile)
                                          , (os.path.getsize(sSecondFile), sSecondFile)]
        taFiles.sort(reverse=True)

        tDelete: tuple[int, str] = taFiles[0]
        os.remove(tDelete[1])

        sRemainFile: str = taFiles[1][1]
        sProcessedName: str = sRemainFile

        if workInfo.sSuffix in sRemainFile:
            nFreedUpSpace += abs(taFiles[0][0] - taFiles[1][0])
            sNewName: str = sRemainFile.replace(workInfo.sSuffix, workInfo.sTargetExt)
            os.rename(sRemainFile, sNewName)
            sProcessedName = sNewName

        return sProcessedName
    else:
        nFirsSize = os.path.getsize(sFirstFile)
        nSecondSize = os.path.getsize(sSecondFile)
        if nSecondSize < nFirsSize:
            nFreedUpSpace += nFirsSize - nSecondSize
        os.remove(sFirstFile)
        sNewName = sSecondFile.replace(workInfo.sSuffix, workInfo.sTargetExt)
        os.rename(sSecondFile, sNewName)
        return sNewName


def fillProcessedFile():
    global workInfo, nFreedUpSpace
    if len(workInfo.saProcessedPaths) > 0:
        with open(workInfo.sProcessedFile, "w") as fileProcessed:
            print(nFreedUpSpace, end="\n", file=fileProcessed)
            print(*workInfo.saProcessedPaths, sep="\n", file=fileProcessed)


def getVideoScale(sFile):
    nInputFormat = cv2.VideoCapture(sFile)
    nInputHeight = int(nInputFormat.get(cv2.CAP_PROP_FRAME_HEIGHT))
    nInputWidth = int(nInputFormat.get(cv2.CAP_PROP_FRAME_WIDTH))
    return (nInputWidth, nInputHeight)


def getOutputScale(nTupleInputScale):
    global workInfo
    nOutputHeight = workInfo.nOutputHeight
    nOutputWidth = int((nOutputHeight * nTupleInputScale[0]) / nTupleInputScale[1])
    if not nOutputWidth % 2 == 0:
        nOutputWidth += 1
    return (nOutputWidth, nOutputHeight)


def convertFiles(saFiles: list[str]):
    global workInfo, nFreedUpSpace
    nFileNumbers: int = len(saFiles)
    for counter, sFile in enumerate(saFiles, 1):
        if workInfo.isProcessed(sFile):
            continue

        saArgs = ["ffmpeg", "-y", "-hide_banner", "-i", sFile]

        nTupleInputScale = getVideoScale(sFile)
        nTupleOutputScale = None
        if workInfo.nOutputHeight is not None and nTupleInputScale[1] > workInfo.nOutputHeight:
            nTupleOutputScale = getOutputScale(nTupleInputScale)
            saArgs.extend(["-vf", f"scale={nTupleOutputScale[0]}:{nTupleOutputScale[1]}"])

        if len(workInfo.saFfmpegArgs) > 0:
            saArgs.extend(workInfo.saFfmpegArgs)
        # else:
        #     saArgs.extend(["-map", "0"])
        sNewFileName: str = f"{os.path.splitext(sFile)[0]}{workInfo.sSuffix}"
        saArgs.extend([sNewFileName])
        subprocess.run("clear")
        print(f"\033[0;33mConverting file {counter} of {nFileNumbers}{
            "" if nTupleOutputScale is None else f" [scale from {nTupleInputScale[0]}x{nTupleInputScale[1]} to {nTupleOutputScale[0]}x{nTupleOutputScale[1]}]"
        } ({round((counter * 100) / nFileNumbers, 2)}%){
            f"; Freed up: {humanize.naturalsize(nFreedUpSpace, binary=True, format='%.2f')}" if nFreedUpSpace > 0 else ""
        }\033[0m")

        try:
            subprocess.run(saArgs, capture_output=False)
        except:
            os.remove(sNewFileName)
            print()
            sys.exit(1)

        workInfo.addProcessed(removeExtraFile(sFile, sNewFileName))
        fillProcessedFile()


def main():
    global workInfo
    saFilesToConvert: list[str] = getFiles(workInfo.path())

    if workInfo.isShowOnly():
        printFiles(saFilesToConvert)
        sys.exit(0)

    convertFiles(saFilesToConvert)
    global nFreedUpSpace
    if nFreedUpSpace > 0:
        print()
        print(f"\033[0;34mFreed up {humanize.naturalsize(nFreedUpSpace, binary=True, format='%.2f')}\033[0m")

    if os.path.isfile(workInfo.sProcessedFile) and workInfo.bIsDeleteProcFile:
        os.remove(workInfo.sProcessedFile)


if __name__ == "__main__":
    workInfo = WorkingInformation()
    main()
