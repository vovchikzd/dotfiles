#!/usr/bin/env python3

import os, pathlib, sys, subprocess, datetime, humanize, mimetypes
from functools import reduce

true, false = True, False

def get_duration(filename: str) -> float:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    to_ret = None
    try:
        to_ret = float(result.stdout)
    except:
        to_ret = 0
    return to_ret


def get_mime(sFilePath):
    return mimetypes.guess_type(sFilePath)[0]

def isVideo(sFilePath):
    type = get_mime(sFilePath)
    return type is not None and 'video' in type

def isAudio(sFilePath):
    type = get_mime(sFilePath)
    return type is not None and 'audio' in type


class Config:
    isAudio = false
    isVideo = true
    isSort = false
    isReverce = true
    
    def __init__(self, args):
        while len(args) > 0:
            arg = args.pop(0)
            match arg:
                case "--audio":
                    self.isAudio = true
                    self.isVideo = false
                case "--sort":
                    self.isSort = true
                case "--all":
                    self.isAudio = true
                    self.isVideo = true
                case "-r":
                    self.isReverce = false
                case _:
                    print(f"Unkhown arg: {arg}", file=sys.stderr)


def main():
    config = Config(sys.argv[1:])
    saDirs = ['.']
    aFileDur: list[tuple[str, float]] = list()
    while len(saDirs) > 0:
        sCurrentDir = saDirs.pop(0)
        for file in os.listdir(sCurrentDir):
            if 'lost+found' in file:
                continue
            sCurrentFile = f"{sCurrentDir}/{file}"
            if os.path.isdir(sCurrentFile):
                saDirs.append(sCurrentFile)
            elif os.path.isfile(sCurrentFile):
                if ((config.isVideo and isVideo(sCurrentFile))
                    or (config.isAudio and isAudio(sCurrentFile))):
                    aFileDur.append((sCurrentFile, get_duration(sCurrentFile)))

    if len(aFileDur):
        if config.isSort:
            aFileDur.sort(reverse=config.isReverce, key=lambda x: x[1])
            for sFile, nDur in aFileDur:
                print(f"{humanize.precisedelta(datetime.timedelta(seconds=nDur))} -- {sFile}")
            print()

        nTotalTime = sum([tup[1] for tup in aFileDur])
        print(humanize.precisedelta(datetime.timedelta(seconds=nTotalTime)))
        print(f"Number of files: {len(aFileDur)}")

if __name__ == "__main__":
    main()
