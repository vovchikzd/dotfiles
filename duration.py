#!/usr/bin/env python3

import os, pathlib, sys, subprocess, datetime, humanize, mimetypes

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

def main():
    saDirs = ['.']
    nFileCounter = 0
    nTotalTime = 0
    while len(saDirs) > 0:
        sCurrentDir = saDirs.pop(0)
        for file in os.listdir(sCurrentDir):
            if 'lost+found' in file:
                continue
            sCurrentFile = f"{sCurrentDir}/{file}"
            if os.path.isdir(sCurrentFile):
                saDirs.append(sCurrentFile)
            elif os.path.isfile(sCurrentFile) and isVideo(sCurrentFile):
                nFileCounter += 1
                nTotalTime += get_duration(sCurrentFile)
    if nFileCounter > 0:
        print(humanize.precisedelta(datetime.timedelta(seconds=nTotalTime)))
        print(f"Number of files: {nFileCounter}")

if __name__ == "__main__":
    main()
