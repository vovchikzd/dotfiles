#!/usr/bin/env python3

import yt_dlp, subprocess

def get_playlist_videos(url):
    ydl_opts = {
        "extract_flat": True
        , "quiet": True
        , "no_warnings": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)

        if "entries" in result:
            return [entry["url"] for entry in result["entries"]]
        return list()

file = "down.py"
name = "%(title)s [%(id)s](%(channel)s).%(ext)s"
playlist = "https://www.youtube.com/playlist?list=PLbtaNY5hOUWllKafXAqHG7aJVwPXOhH-G"
# playlist = "https://www.youtube.com/@SanctusEchinus/streams"
with open(file, "w") as out:
    print("#!/usr/bin/env python3\n", file=out)
    print("urls = [", file=out)
    vids = get_playlist_videos(playlist)
    for cnt, url in enumerate(vids, 1):
        print(f'  ["yt-dlp", "{url}", "-o", "{cnt:02}. {name}", "--paths", "temp:."],', file=out)
    print("]\n", file=out)

    print(r"""import concurrent.futures, subprocess, os

MAX_WORKERS=5
total_length = len(urls)
bIsShowProgressBar = MAX_WORKERS > 1 and total_length > 1

def download(cmd):
    while True:
        try:
            result = subprocess.run(cmd, shell=False, capture_output=bIsShowProgressBar)
            if result.returncode == 0:
                break
        except:
            continue


def progress(current, total, length=75):
    fraction = current / total
    fill = int(fraction * length) * '█'
    padding = (length - len(fill)) * ' '
    ending = '\r\x1b[K\x1b[1A\x1b[?25h\n' if current == total else ''
    print(f"\r\x1b[?25l\x1b[KProgress: |{fill}{padding}| {round(fraction * 100, 2)}% ({current}/{total})", end=ending)


with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    future_to_task = { executor.submit(download, cmd) for cmd in urls }

    if bIsShowProgressBar:
        progress(0, total_length)
        for i, _ in enumerate(concurrent.futures.as_completed(future_to_task), 1):
            progress(i, total_length)


if os.path.isfile("rename.py"):
    subprocess.run("./rename.py")""", file=out)

subprocess.run(["chmod", "+x", file], shell=False, capture_output=False)
