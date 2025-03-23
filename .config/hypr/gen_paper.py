#!/usr/bin/env python3

import os, random, subprocess
from hashlib import md5

def main():
    sConfigFile: str = "/home/vovchik/dotfiles/.config/hypr/hyprpaper.conf"
    sPapersDir: str = "/home/vovchik/dotfiles/images/wallpapers"
    saFilesPaths: list[str] = [f"{sPapersDir}/{sFileName}" for sFileName in os.listdir(sPapersDir)]
    sFirstFile: str = random.choice(saFilesPaths)
    sSeconFile: str = random.choice(saFilesPaths)
    while (
        md5(open(sFirstFile, 'rb').read()).hexdigest() ==
            md5(open(sSeconFile, 'rb').read()).hexdigest()
    ):
        sSeconFile = random.choice(saFilesPaths)
    with open(sConfigFile, "w") as fConfigFile:
        print(f"preload = {sFirstFile}", file=fConfigFile)
        print(f"preload = {sSeconFile}", file=fConfigFile)
        print(f"wallpaper = DP-2, {sFirstFile}", file=fConfigFile)
        print(f"wallpaper = DP-3, {sSeconFile}", file=fConfigFile)
    subprocess.Popen(
        "/usr/bin/hyprpaper"
        , start_new_session=True
    )


if __name__ == "__main__":
    main()
