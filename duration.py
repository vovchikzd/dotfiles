#!/usr/bin/env python3

import os, sys, subprocess, mimetypes
from datetime import timedelta

def_print = print

def print(*args, **kwargs):
    kwargs["flush"] = False
    def_print(*args, **kwargs)

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

files = [f for f in sys.argv[1:] if isVideo(f) or isAudio(f)]

sum_duration = 0
is_print_filenames = len(files) > 1
is_print_sum_time = "-s" in sys.argv[1:]
is_print_seconds = "--seconds" in sys.argv[1:]
file_end = " " if is_print_filenames else "\n"
for file in files:
    duration = get_duration(file)
    sum_duration += duration
    if is_print_seconds:
        print(duration, end=file_end)
    else:
        print(f"{timedelta(seconds=duration)}", end=file_end)
    if is_print_filenames:
        print(file)
if is_print_sum_time:
    if is_print_seconds:
        print(sum_duration)
    else:
        print(timedelta(seconds=sum_duration))
