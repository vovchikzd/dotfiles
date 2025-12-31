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
        print( "wallpaper {", file=fConfigFile)
        print( "  monitor = DP-2", file=fConfigFile)
        print(f"  path = {sFirstFile}", file=fConfigFile)
        print( "  fit_mode = cover", file=fConfigFile)
        print( "}", file=fConfigFile)
        print(file=fConfigFile)
        print( "wallpaper {", file=fConfigFile)
        print( "  monitor = DP-3", file=fConfigFile)
        print(f"  path = {sSeconFile}", file=fConfigFile)
        print( "  fit_mode = cover", file=fConfigFile)
        print( "}", file=fConfigFile)
    subprocess.Popen(
        "/usr/bin/hyprpaper"
        , start_new_session=True
    )


if __name__ == "__main__":
    main()
