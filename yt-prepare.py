#!/usr/bin/env python3

import os, sys, subprocess
from pytube import Playlist

true = True
false = False


sHelpMessage: str = (
"""
Usage: yt-prepare [Arguments...] playlist... [-- yt-dlp argument...]

Arguments:
    -a, --append     append result to an existing file
    -f, --force      allow rewriting existing file
    -h, --help       show this help message
    -n, --numbering  numbering created directories by passed order
    -o <file>        print result to <file>, default name is 'down.sh'

    --               all after this will go as arguments to yt-dlp
"""
)


class Color:
    NEUTRAL: str = "\033[0m"
    RED: str = "\033[0;31m"
    GREEN: str = "\033[0;32m"
    YELLOW: str = "\033[0;33m"
    BLUE: str = "\033[0;34m"


def colored(sToColor: str, color: Color = Color.NEUTRAL):
    return f"{color}{sToColor}{Color.NEUTRAL}"


def isQuoted(sToCheck: str) -> bool:
    tQuotes: tuple[str, str] = ("'", '"')
    return sToCheck[0] in tQuotes and sToCheck[-1] in tQuotes


def quoted(sString: str) -> str:
    if isQuoted(sString):
        return sString
    sQuote: str = '"' if "'" in sString else "'"
    return f"{sQuote}{sString}{sQuote}"


class WorkInformation:
    saPlaylists: list[str] = list()
    saYtDltArguments: list[str] = list()
    sOutputFileName: str = "./down.sh"
    sFileMode: str = "w"
    bIsWriteShebang: bool = true
    bIsRewriteExistingFile: bool = false
    bIsNumbering: bool = false

    def __init__(self, args):
        if  "-h" in args or "--help" in args:
            print(sHelpMessage)
            sys.exit(0)
        while len(args) > 0:
            sReadedArgument = args.pop(0)
            if sReadedArgument[0] == "-":
                match sReadedArgument:
                    case "-o" if len(args) > 0:
                        self.sOutputFileName = args.pop(0)
                    case "-o" if len(args) == 0:
                        print(
                            colored(
                                f"{quoted(sReadedArgument)} argument required a file name"
                                , color=Color.RED
                            )
                        )
                        sys.exit(1)
                    case "-a" | "--append":
                        self.sFileMode = "a"
                        self.bIsWriteShebang = false
                        self.bIsRewriteExistingFile = true
                    case "-f" | "--force":
                        self.bIsRewriteExistingFile = true
                    case "--":
                        self.saYtDltArguments = args.copy()
                        args.clear()
                    case "-n" | "--numbering":
                        self.bIsNumbering = true
                    case _:
                        print(
                            colored(
                                f"{quoted(sReadedArgument)} doesn't right argument"
                                , color=Color.RED
                            )
                        )
                        sys.exit(1)
            else:
                self.saPlaylists.append(sReadedArgument)
        if len(self.saPlaylists) == 0:
            print(colored("Not any url was passed", color=Color.RED))
            print(sHelpMessage)
            sys.exit(1)


def main(workInfo: WorkInformation):

    def getStringArray(playlist):
        sArrayStirng = "urls=(\n"
        for sVideoUrl in playlist:
            sArrayStirng += f"  {quoted(sVideoUrl)}\n"
        sArrayStirng += ")\n\n"
        return sArrayStirng

    def getPlaylistAddress(sPlaylistUrl: str) -> str:
        sLeftTrimmed = sPlaylistUrl[sPlaylistUrl.index("list=") + 5:]
        nAmpersandIndex = sLeftTrimmed.find("&")
        if nAmpersandIndex == -1:
            return sLeftTrimmed
        else:
            return sLeftTrimmed[:nAmpersandIndex]

    def getCycle(sOutputDirname: str, nCount: int, saYtArgs: list[str] = None, bIsNumbering: bool = false, nDirCount: int = 0):
        nNumberLength = len(str(nCount))
        sArgsString = " ".join([quoted(arg) if not arg[0] == "-" else arg for arg in saYtArgs])
        sResultString =   "counter=1\n"
        sResultString +=  "for url in ${urls[@]}; do\n"
        sResultString +=  "  clear\n"
        sResultString += f'  num=$(printf "%0{nNumberLength}d" "$counter")\n'
        sResultString += f"  false\n"
        sResultString += f"  while [ $(echo $?) != 0 ]; do\n"
        sResultString += f'    printf "\\033[0;33mDownloading $counter of {nCount}\\033[m\\n"\n'
        sResultString += f'    yt-dlp -o "{f"{nDirCount}. " if bIsNumbering else ""}{sOutputDirName}/$num. $name" "$url" {sArgsString}\n'
        sResultString += f"  done\n"
        sResultString += f"  ((++counter))\n"
        sResultString += f"done\n"
        return sResultString


    if (os.path.isfile(workInfo.sOutputFileName) 
            and not workInfo.bIsRewriteExistingFile):
        print(f"File {quoted(workInfo.sOutputFileName)} exists. Probably you want to use '-o <file>' argument.")
        print("See 'yt-prepare --help' for more information.")
        sys.exit(1)

    saErrorUrls: list[str] = list()
    try:
        with open(workInfo.sOutputFileName, f"{workInfo.sFileMode}+") as outputFile:
            if workInfo.bIsWriteShebang:
                print("#!/usr/bin/env bash\n", file=outputFile)
                print("source ~/.bash_aliases\n", file=outputFile)

            for counter, sPlaylistUrl in enumerate(workInfo.saPlaylists, 1):
                playlist = Playlist(sPlaylistUrl)

                sResultString: str = ""
                try:
                    sPlaylistAddres = getPlaylistAddress(sPlaylistUrl)
                    sOutputDirName = f"{playlist.title} [{sPlaylistAddres}]"
                    sResultString += f"# {sOutputDirName}\n"
                    sResultString += getStringArray(playlist)
                    sResultString += getCycle(sOutputDirName, len(playlist), workInfo.saYtDltArguments, workInfo.bIsNumbering, counter)
                    print(sResultString, file=outputFile, end='\n\n')
                except:
                    saErrorUrls.append(sPlaylistUrl)

        subprocess.run(["chmod", "+x", workInfo.sOutputFileName])
    except FileNotFoundError:
        print(f"Can't open file {quoted(workInfo.sOutputFileName)}")
        sys.exit(1)

    if len(saErrorUrls) > 0:
        sUrlList = ""
        for url in saErrorUrls:
            sUrlList += f"  {quoted(url)}\n"
        print(f"These urls wasn't processed:")
        print(sUrlList, end='')
        print("Most likely this isn't playlists")
        sys.exit(1)


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    if len(args) == 0:
        print(sHelpMessage)
        sys.exit(1)
    workInfo = WorkInformation(args)
    main(workInfo)
