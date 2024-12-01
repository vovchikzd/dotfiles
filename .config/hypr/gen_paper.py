#!/usr/bin/env python3

import os, random, subprocess

def main():
    sConfigFile: str = "/home/vovchik/dotfiles/.config/hypr/hyprpaper.conf"
    sPapersDir: str = "/home/vovchik/dotfiles/images/wallpapers"
    saFilesPaths: list[str] = [f"{sPapersDir}/{sFileName}" for sFileName in os.listdir(sPapersDir)]
    sFilePath: str = random.choice(saFilesPaths)
    with open(sConfigFile, "w") as fConfigFile:
        print(f"preload = {sFilePath}", file=fConfigFile)
        print(f"wallpaper = , {sFilePath}", file=fConfigFile)
    # subprocess.Popen("/usr/bin/hyprpaper", start_new_session=True)


if __name__ == "__main__":
    main()
