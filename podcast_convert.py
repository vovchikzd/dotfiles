#!/usr/bin/env python3

import os, subprocess, concurrent.futures, sys

class FileToConvert:
    sOrigName: str
    sConvertedName: str
    sNewName: str

    def __init__(self, sFile: str) -> None:
        sFileName, _ = os.path.splitext(sFile)
        self.sOrigName = sFile
        self.sConvertedName = f"{sFileName}.converted.mkv"
        self.sNewName = f"{sFileName}.mkv"

    def getCmd(self) -> list[str]:
        return ["ffmpeg", "-i", self.sOrigName, "-vn", "-map", "0:a", "-map", "0:t?", "-map_metadata", "0", "-c", "copy", "-c:a", "libopus", "-preset", "veryslow", self.sConvertedName]

    def successClear(self):
        if os.path.isfile(self.sConvertedName):
            os.remove(self.sOrigName)
            os.rename(self.sConvertedName, self.sNewName)

    def errorClear(self):
        if os.path.isfile(self.sConvertedName):
            os.remove(self.sConvertedName)
        if self.sNewName != self.sOrigName and os.path.isfile(self.sNewName):
            os.remove(self.sNewName)

def getFiles() -> list[str]:
    saFormats: list[str] = [".mp4", ".mkv", ".webm", ".mp4"]
    saDirs: list[str] = ["."]
    sFiles: list[str] = list()
    while len(saDirs) > 0:
        sDir = saDirs.pop(0)
        for sFile in os.listdir(sDir):
            sCurrentFilePath = os.path.join(sDir, sFile)
            _, sFileExtension = os.path.splitext(sCurrentFilePath)
            if os.path.isdir(sCurrentFilePath):
                saDirs.append(sCurrentFilePath)
            elif os.path.isfile(sCurrentFilePath) and sFileExtension in saFormats:
                sFiles.append(sCurrentFilePath)
    return sFiles


aFailedFiles: list[FileToConvert] = list()


def convert(fileToConvert: FileToConvert):
    try:
        result = subprocess.run(fileToConvert.getCmd(), shell=False, capture_output=True)
        if result.returncode == 0:
            fileToConvert.successClear()
        else:
            aFailedFiles.append(fileToConvert)
            fileToConvert.errorClear()
    except:
        aFailedFiles.append(fileToConvert)
        fileToConvert.errorClear()

def progress(current, total, length=75):
    fraction = current / total
    fill = int(fraction * length) * '█'
    padding = (length - len(fill)) * ' '
    ending = '\r\x1b[K\x1b[1A\x1b[?25h\n' if current == total else ''
    print(f"\r\x1b[?25l\x1b[KProgress: |{fill}{padding}| {round(fraction * 100, 2)}% ({current}/{total})", end=ending)

def main():
    saFiles: list[str] = getFiles()
    aFilesToConvert: list[FileToConvert] = [FileToConvert(sFile) for sFile in saFiles]

    total_lengt = len(aFilesToConvert)
    progress(0, total_lengt)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_task = { executor.submit(convert, fileToConvert) for fileToConvert in aFilesToConvert }

        for cnt, _ in enumerate(concurrent.futures.as_completed(future_to_task), 1):
            progress(cnt, total_lengt)

    if len(aFailedFiles) > 0:
        print("Failed files:", file=sys.stderr)
        for failed in aFailedFiles:
            print(failed.sOrigName, file=sys.stderr)


if __name__ == "__main__":
    main()
