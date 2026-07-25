#!/usr/bin/env python3

import os, json
from sys import stderr
from subprocess import run as def_run
ffprobe = "ffprobe" if (def_run(["ffprobe", "-versoin"], capture_output=True).returncode == 0) else "/home/vovchik/ffmpeg_latest/ffmpeg-master-latest-linux64-gpl/bin/ffprobe"
if (def_run([ffprobe, "-version"], capture_output=True).returncode != 0):
    print("Can't find working ffprobe", file=stderr)
    exit(1)

base_get_streams_cmd = [ffprobe, "-v", "quiet", "-print_format", "json", "-show_streams", "-select_streams"]

def run(*args, **kwargs):
    kwargs["check"] = True
    return def_run(*args, **kwargs)

def clrun(*args, **kwargs):
    run("clear")
    return run(*args, **kwargs)

def catch_run(*args, **kwargs):
    kwargs["capture_output"] = True
    kwargs["text"] = True
    kwargs["encoding"] = 'utf-8'
    return def_run(*args, **kwargs)

def del_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)

def get_meta(file_path: str, meta: str) -> str:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} doesn't exist")

    cmd = [ffprobe, "-v", "error", "-show_entries", f"format_tags={meta}"
           , "-of", "default=noprint_wrappers=1:nokey=1", file_path]

    res = catch_run(cmd)
    if res.returncode != 0:
        print(f"Error occured while getting {meta} for {file_path}", file=stderr)
        exit(5)

    return res.stdout.strip()

def get_duration(file_path: str) -> float:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} doesn't exist")

    cmd = [ffprobe, "-v", "error", "-show_entries", "format=duration"
           , "-of", "default=noprint_wrappers=1:nokey=1", file_path]

    res = catch_run(cmd)
    if res.returncode != 0:
        print(f"Error occured while getting duration for {file_path}", file=stderr)
        exit(5)

    return float(res.stdout)


class Stream:
    index: int
    title: str | None
    dispositions: list[str]
    metadata: dict[str, str]
    type_name: str

    def __init__(self, type_name: str, index: int, title: str | None, dispositions: list[str], metadata: dict[str, str]):
        if type_name not in ['audio', 'video', 'sub']:
            raise AttributeError("Invalid stream type")
        self.type_name = type_name
        self.index = index
        self.title = title
        self.dispositions = dispositions
        self.metadata = metadata

    def __str__(self):
        return f"{{index: {self.index}, title: {self.title}, dispositions: {self.dispositions}, metadata: {self.metadata}, type: {self.type_name}}}"


def get_streams(file_path: str, stream_specifier: str) -> list[Stream]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} doesn't exist")

    get_streams_cmd = base_get_streams_cmd + [stream_specifier, file_path]

    stream_type = None
    match stream_specifier:
        case 'a':
            stream_type = 'audio'
        case 'v' | "V":
            stream_type = 'video'
        case 's':
            stream_type = 'sub'
        case _:
            raise AttributeError("Invalid stream specifier")


    streams_from_video = json.loads(catch_run(get_streams_cmd).stdout).get("streams")
    streams = list()

    for stream in streams_from_video:
        index = stream.get("index")
        tags = dict([(str(key), str(value)) for key, value in stream.get("tags").items()])
        dispositions = [str(key) for key, value in stream.get("disposition").items() if value == 1]
        streams.append(
            Stream(
                type_name = stream_type
                , title = tags.get("title")
                , index = index
                , dispositions = dispositions
                , metadata = tags
            )
        )
    return streams


def get_audio_streams(file_path: str) -> list[Stream]:
    return get_streams(file_path, "a")


def get_video_streams(file_path: str) -> list[Stream]:
    return get_streams(file_path, "V")

def get_subtitle_streams(file_path: str) -> list[Stream]:
    return get_streams(file_path, "s")

def select_audio(file_path: str, language: str = "eng") -> int | None:
    streams = get_audio_streams(file_path)

    index = None
    if len(streams) == 1:
        index = streams[0].index
    else:
        selected_streams = [s for s in streams if s.metadata.get("language") == language and (not s.title or 'comment' not in s.title.lower())]
        if len(selected_streams) == 1:
            index = selected_streams[0].index
    return index

def select_subtitle(file_path: str, language: str = "eng") -> int | None:
    streams = [s for s in get_subtitle_streams(file_path) if s.metadata.get("language") == language]

    index = None
    if len(streams) == 1:
        index = streams[0].index

    if index is None:
        selected_streams = [
            s for s in streams if (
                (s.title is None or
                ('sdh' not in s.title.lower()
                and 'forced' not in s.title.lower()
                and 'comment' not in s.title.lower()))
                and 'forced' not in s.dispositions
                and 'hearing_impaired' not in s.dispositions
            )
        ]
        if len(selected_streams) == 1:
            index = selected_streams[0].index
    return index
