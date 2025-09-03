#!/usr/bin/env python3

import yt_dlp

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

name = "%(title)s [%(id)s](%(channel)s).%(ext)s"
playlist = "https://www.youtube.com/playlist?list=PLbtaNY5hOUWllKafXAqHG7aJVwPXOhH-G"
with open("down.py", "w") as out:
    print("#!/usr/bin/env python3\n", file=out)
    print("urls = [", file=out)
    for cnt, url in enumerate(get_playlist_videos(playlist), 33):
        print(f'  ["yt-dlp", "{url}", "-o", "{cnt:02}. {name}"],', file=out)
    print("]\n", file=out)

    print(r"""import concurrent.futures, subprocess

def download(cmd):
    while True:
        try:
            result = subprocess.run(cmd, shell=False, capture_output=True)
            if result.returncode == 0:
                break
        except:
            continue


def progress(current, total, length=50):
    fraction = current / total
    fill = int(fraction * length) * '█'
    padding = (length - len(fill)) * ' '
    ending = '\033[?25h\n' if current == total else '\r'
    print(f"\033[?25l\033[KProgress: |{fill}{padding}| {round(fraction * 100, 2)}% ({current}/{total})", end=ending)


total_length = len(urls)
progress(0, total_length)
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_to_task = { executor.submit(download, cmd) for cmd in urls }

    for i, _ in enumerate(concurrent.futures.as_completed(future_to_task), 1):
        progress(i, total_length)""", file=out)
