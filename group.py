#!/usr/bin/env python3

import os, re, sys

sHelpMessage = """Usage: ./group.py [Args]

Args:
    -a, --all      group all videos, even single ones
    -h, --help     print this help message and exit
    -i, --ignore   ignore videos without channel
    -q, --quiet    dont't print anything
    -s, --show     print formed groups to stdout

If directory already exist, video will be moved there even if it is a single video for group
Videos without channel will be placed in separate folder
Videos without vid's id ignored
"""

class Config:
    bIsGroupSingle: bool = False
    bIsShowGroups: bool = False
    bIsIgnoreUnknown: bool = False

    def __init__(self, args: list[str] | None = None):
        if args is None or len(args) == 0:
            return
        saAllArgs: list[str] = list()
        for sArg in args:
            if sArg.startswith("--"):
                saAllArgs.append(sArg[2:])
            elif sArg.startswith("-"):
                for ch in sArg[1:]:
                    saAllArgs.append(ch)
            else:
                print(f"Invalid arg `{sArg}`; ignored")

        if "help" in saAllArgs or "h" in saAllArgs:
            print(sHelpMessage, end='')
            sys.exit(0)

        if "quiet" in saAllArgs or "q" in saAllArgs:
            devnull = open(os.devnull, "w")
            sys.stdout = devnull
            sys.stderr = devnull

        while len(saAllArgs) > 0:
            arg = saAllArgs.pop(0)
            match arg:
                case "all" | "a":
                    self.bIsGroupSingle = True
                case "show" | "s":
                    self.bIsShowGroups = True
                case "ignored" | "i":
                    self.bIsIgnoreUnknown = True
                case "quiet" | "q":
                    pass
                case _:
                    print(f"Unknown arg: '{arg}'. Ingored.", file=sys.stderr)

def main():
    conf: Config = Config(sys.argv[1:])
    sFolderToFiles: dict[str, list[str]] = dict()
    sToFindChannel: list[tuple[str, str]] = list()
    saIgnoredFiles: list[str] = list()

    for sFile in os.listdir():
        if not os.path.isfile(sFile):
            continue

        if not os.path.splitext(sFile)[-1] in ['.mkv', '.mp4', '.webm', '.avi']:
            saIgnoredFiles.append(sFile)
            continue

        saChannel: list[str] = re.findall(r"^.*\[.*\]\((.*)\)\..+$", sFile)
        if len(saChannel) == 1:
            sFolder = saChannel[0]
            sFolderToFiles[sFolder] = sFolderToFiles.get(sFolder, list()) + [sFile]
        else:
            saId: list[str] = re.findall(r"^.*\[(.*)\]\..+$", sFile)
            if len(saId) == 1:
                if conf.bIsIgnoreUnknown:
                    saIgnoredFiles.append(sFile)
                else:
                    sToFindChannel.append((sFile, f"https://www.youtube.com/watch?v={saId[0]}"))
            else:
                saIgnoredFiles.append(sFile)

    for sFolder, saFiles in sFolderToFiles.items():
        if not conf.bIsGroupSingle and len(saFiles) < 2 and not os.path.isdir(sFolder):
            continue

        if not os.path.isdir(sFolder):
            os.mkdir(sFolder)

        if conf.bIsShowGroups:
            print(f"{sFolder}:")
        for sFile in saFiles:
            if conf.bIsShowGroups:
                print(f"  {sFile}")
            os.rename(sFile, os.path.join(sFolder, sFile))

    if len(sToFindChannel) > 0:
        sFindDir: str = "find_channel_vids"
        if not os.path.isdir(sFindDir):
            os.mkdir(sFindDir)
        if conf.bIsShowGroups:
            print(f"{sFindDir}:")
        with open(os.path.join(sFindDir, "links.txt"), "a") as fLinks:
            for sFile, sUrl in sToFindChannel:
                if conf.bIsShowGroups:
                    print(f"  {sFile}")
                os.rename(sFile, os.path.join(sFindDir, sFile))
                print(f"{sUrl} --> {sFile}", file=fLinks)

    # if len(saIgnoredFiles) > 0:
    #     print("Ignored Files:")
    #     for sIgnoredFile in saIgnoredFiles:
    #         print(f"  {sIgnoredFile}")


if __name__ == "__main__":
    main()
