#!/usr/bin/env python3

import os, sys, subprocess, re, yt_dlp

true = True
false = False


sHelpMessage: str = (
"""
Usage: yt-prepare [Arguments...] playlist... [-- yt-dlp argument...]

Arguments:
    -a, --append     append result to an existing file
    -d, --dynamic    add dynamicly numbering progress
    -f, --force      allow rewriting existing file
    -h, --help       show this help message
    -n, --numbering  numbering created directories by passed order
    -o <file>        print result to <file>, default name is 'down.sh'
    -t, --template   create empty template file (always dynamic numbering)

    --               all after this will go as arguments to yt-dlp
"""
)


class Color:
    NEUTRAL: str = "\033[0m"
    RED: str = "\033[0;31m"
    GREEN: str = "\033[0;32m"
    YELLOW: str = "\033[0;33m"
    BLUE: str = "\033[0;34m"


def get_playlist_title(playlist_url):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,       
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        return result.get('title') if result else None


def get_playlist_videos(playlist_url):
    ydl_opts = {
        'extract_flat': True,
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        
        if 'entries' in result:
            return [entry['url'] for entry in result['entries']]
        return []


def colored(sToColor: str, color: Color = Color.NEUTRAL):
    return f"{color}{sToColor}{Color.NEUTRAL}"


def isQuoted(sToCheck: str) -> bool:
    tQuotes: tuple[str, str] = ("'", '"')
    return len(sToCheck) > 1 and sToCheck[0] == sToCheck[-1] and sToCheck[0] in tQuotes


def quoted(sString: str = "") -> str:
    if len(sString) == 0:
        return "''"
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
    bIsDynamicNumbering: bool = false
    bIsCreateTemplate: bool = false

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
                    case "-p" if len(args) > 0:
                        self.saPlaylists.append(f"https://youtube.com/playlist?list={args.pop(0)}")
                    case "-d" | "--dynamic":
                        self.bIsDynamicNumbering = true
                    case "-t" | "--template":
                        self.bIsCreateTemplate = true
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
        if len(self.saPlaylists) == 0 and not self.bIsCreateTemplate:
            print(colored("Not any url was passed", color=Color.RED))
            print(sHelpMessage)
            sys.exit(1)


def main(workInfo: WorkInformation):
    nVideosInsidePlaylist = {}

    def getStringArray(sPlaylistUrl):
        videoUrls = get_playlist_videos(sPlaylistUrl)
        nVideosInsidePlaylist[sPlaylistUrl] = len(videoUrls)
        nAlign = len(str(len(videoUrls)))
        sArrayStirng = "urls=(\n"
        for counter, sVideoUrl in enumerate(videoUrls, 1):
            sArrayStirng += f"  {quoted(sVideoUrl)} # {counter:0{nAlign}}\n"
        sArrayStirng += ")\n\n"
        return sArrayStirng

    def getPlaylistAddress(sPlaylistUrl: str) -> str:
        sLeftTrimmed = sPlaylistUrl[sPlaylistUrl.index("list=") + 5:]
        nAmpersandIndex = sLeftTrimmed.find("&")
        if nAmpersandIndex == -1:
            return sLeftTrimmed
        else:
            return sLeftTrimmed[:nAmpersandIndex]

    def getCycle(sOutputDirName: str, nCount: int, saYtArgs: list[str] = None, bIsNumbering: bool = false, nDirCount: int = 0, bIsDynNum: bool = false):
        nNumberLength = len(str(nCount))
        sArgsString = " ".join([quoted(arg) if (len(arg) == 0 or not arg[0] == "-") else arg for arg in saYtArgs])
        sResultString = ""
        if bIsDynNum:
            sResultString += "array_length=${#urls[*]}\n"
            sResultString += "char_length=${#array_length}\n"
            sResultString += "\n"
            sResultString += "if [ $char_length -lt 2 ]; then\n"
            sResultString += "  char_length=2\n"
            sResultString += "fi\n"
            sResultString += "\n"
        sResultString +=  "counter=1\n"
        sResultString +=  "clear\n"
        sResultString +=  "for url in ${urls[@]}; do\n"
        if bIsDynNum:
            sResultString += f'  num=$(printf "%0${{char_length}}d" "$counter")\n'
        else:
            sResultString += f'  num=$(printf "%0{max(nNumberLength, 2)}d" "$counter")\n'
        sResultString += f"  false\n"
        sResultString += f"  while [ $(echo $?) != 0 ]; do\n"
        if bIsDynNum:
            sResultString += f'    printf "\\033[0;33mDownloading $counter of ${{array_length}} ({re.sub(' \\[.*\\]', '', sOutputDirName)})\\033[0m\\n"\n'
        else:
            sResultString += f'    printf "\\033[0;33mDownloading $counter of {nCount} ({re.sub(' \\[.*\\]', '', sOutputDirName)})\\033[0m\\n"\n'
        sResultString += f'    yt-dlp -o "{f"{nDirCount:02}. " if bIsNumbering else ""}{sOutputDirName}/$num. $name" "$url" {sArgsString}\n'
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
                print("pip install -U yt-dlp\n", file=outputFile)

            for counter, sPlaylistUrl in enumerate(workInfo.saPlaylists, 1):

                sResultString: str = ""
                try:
                    sPlaylistAddres = getPlaylistAddress(sPlaylistUrl)
                    sOutputDirName = f"{get_playlist_title(sPlaylistUrl)} [{sPlaylistAddres}]".replace('"', r'\"').replace("/", "_")
                    sResultString += f"# {sOutputDirName}\n"
                    sResultString += f"# {sPlaylistUrl}\n"
                    sResultString += getStringArray(sPlaylistUrl)
                    sResultString += getCycle(sOutputDirName, nVideosInsidePlaylist[sPlaylistUrl], workInfo.saYtDltArguments, workInfo.bIsNumbering, counter, workInfo.bIsDynamicNumbering)
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


def createTemplate(workInfo):
    if (os.path.isfile(workInfo.sOutputFileName)
            and not workInfo.bIsRewriteExistingFile):
        print(f"File {quoted(workInfo.sOutputFileName)} exists. Probably you want to use '-o <file>' argument.")
        print("See 'yt-prepare --help' for more information.")
        sys.exit(1)

    with open(workInfo.sOutputFileName, f"{workInfo.sFileMode}+") as outputFile:
        if workInfo.bIsWriteShebang:
            print("#!/usr/bin/env bash\n", file=outputFile)
            print("source ~/.bash_aliases\n", file=outputFile)
            print("pip install -U yt-dlp\n", file=outputFile)

        sArgsString = " ".join([quoted(arg) if (len(arg) == 0 or not arg[0] == "-") else arg for arg in workInfo.saYtDltArguments])
        sResultString = """urls=(\n\n)\n\n"""
        sResultString += "array_length=${#urls[*]}\n"
        if workInfo.bIsNumbering:
            sResultString += "char_length=${#array_length}\n\n"
            sResultString += "if [ $char_length -lt 2 ]; then\n"
            sResultString += "  char_length=2\n"
            sResultString += "fi\n"
        sResultString += "\n"
        sResultString += "counter=1\n"
        sResultString += "clear\n"
        sResultString += "for url in ${urls[@]}; do\n"
        if workInfo.bIsNumbering:
            sResultString += '  num=$(printf "%0${char_length}d" "$counter")\n'
        sResultString += '  false\n'
        sResultString += "  while [ $(echo $?) != 0 ]; do\n"
        sResultString += r'    printf "\033[0;33mDownloading $counter of ${array_length}\033[0m\n"'
        sResultString += "\n"
        if workInfo.bIsNumbering:
            sResultString += f'    yt-dlp -o "$num. $name" "$url" {sArgsString}\n'
        else:
            sResultString += f'    yt-dlp "$url" {sArgsString}\n'
        sResultString += "  done\n"
        sResultString += "  ((++counter))\n"
        sResultString += "done\n\n"
        print(sResultString, file=outputFile)
        
    subprocess.run(["chmod", "+x", workInfo.sOutputFileName])


if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    if len(args) == 0:
        print(sHelpMessage)
        sys.exit(1)
    workInfo = WorkInformation(args)
    if workInfo.bIsCreateTemplate:
        createTemplate(workInfo)
    else:
        main(workInfo)
