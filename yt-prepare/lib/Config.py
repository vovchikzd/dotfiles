import lib.Logger as log
from lib.commondef import *
import re, os

class Config:
    bIsRewrite = False
    sOutputFileName = "down.py"
    sYtDlpExecPath = ""
    nChannelStartNum = None
    nPlaylistStartNum = None
    bIsCommonFolderNum = False
    nCommonFolderStartNum = None
    nVideoStartNum = None
    bIsCreateSubFolders = True
    aChannels = list()
    aPlaylists = list()
    aVideos = list()
    saYtDlpCommonArgs = list()

    def parseArgs(self, args):
        while len(args) > 0:
            arg = args.pop(0)
            match arg:
                case "-f":
                    self.bIsRewrite = True
                    log.info("Allow overwrite existing script")

                case "-o":
                    if (len(args) == 0 or args[0].startswith('-')):
                        log.error("'-o' option requires argument, see '--help'")
                    sOutFile = args.pop(0)
                    if os.path.isdir(sOutFile):
                        log.error(f"{quoted(sOutFile)} is directory")
                    self.sOutputFileName = sOutFile
                    log.info(f"Set output file to {quoted(sOutFile)}")

                case "--yt-dlp":
                    if (len(args) == 0 or args[0].startswith('-')):
                        log.error("'--yt-dlp' option requires argument, see '--help'")
                    sYtExecPath = args.pop(0)
                    if not (os.path.isfile(sYtExecPath) and os.access(sYtExecPath, os.X_OK)):
                        log.error(f"{quoted} is not executable")
                    self.sYtDlpExecPath = sYtExecPath
                    log.info(f"Set yt-dlp executable to {quoted(sYtExecPath)}")

                case chNum if chNum.startswith("--ch-num"):
                    nChStNum = None
                    if chNum == "--ch-num":
                        nChStNum = 1
                    elif re.fullmatch(r"^--ch-num=-?\d+$", chNum):
                        nChStNum = getNumFromStr(chNum.split("=")[1])
                    else:
                        log.error("Channel numbering option should match pattern '--ch-num=<num>', see '--help'")
                    self.nChannelStartNum = nChStNum
                    log.info(f"Set start number for channel folders to {nChStNum}")

                case plNum if plNum.startswith("--pl-num"):
                    nPlStNum = None
                    if plNum == "--pl-num":
                        nPlStNum = 1
                    elif re.fullmatch(r"^--pl-num=-?\d+$", plNum):
                        nPlStNum = getNumFromStr(plNum.split("=")[1])
                    else:
                        log.error("Playlist numbering option should match pattern '--pl-num=<num>', see '--help'")
                    self.nPlaylistStartNum = nPlStNum
                    log.info(f"Set start number for playlist folders to {nPlStNum}")

                case dirNum if dirNum.startswith("--dir-num"):
                    self.bIsCommonFolderNum = True
                    nDrStNum = None
                    if dirNum == "--dir-num":
                        nDrStNum = 1
                    elif re.fullmatch(r"^--dir-num=-?\d+$", dirNum):
                        nDrStNum = getNumFromStr(dirNum.split("=")[1])
                    else:
                        log.error("Folder numbering option should match pattern '--dir-num=<num>', see '--help'")
                    self.nCommonFolderStartNum = nDrStNum
                    log.info(f"Set continuous folder numbering starting from {nDrStNum}")

                case vdNum if vdNum.startswith("--vd-num"):
                    nVdStNum = None
                    if vdNum == "--vd-num":
                        nVdStNum = 1
                    elif re.fullmatch(r"^--vd-num=-?\d+$", vdNum):
                        nVdStNum = getNumFromStr(vdNum.split("=")[1])
                    else:
                        log.error("Video numbering option should match pattern '--vd-num=<num>', see '--help'")
                    self.nVideoStartNum = nVdStNum
                    log.info(f"Set start number for videos to {nVdStNum}")

                case "--no-dir":
                    self.bIsCreateSubFolders = False
                    log.info("Don't create any subfolders for channels or playlists")

                case url if isUrl(url):
                    self.addLink(url)

                case _:
                    log.error(f"Unknown argument: {quoted(arg)}")

    def addLink(self, url):
        pass

    def __init__(self, argv):
        self.sStartCmd = ' '.join([quoted(arg) if (' ' in arg or '"' in arg or "'" in arg) else arg for arg in argv])
        args: list[str] = argv[1:]
        if len(args) == 0:
            log.error("Requires at least one argument, see '--help' for more information")
        if not any(isUrl(arg) for arg in args):
            log.error("Requires at least one link")
        self.parseArgs(args)
        if (self.sYtDlpExecPath is None or self.sYtDlpExecPath == ''):
            self.sYtDlpExecPath = findExecPath("yt-dlp")
            if self.sYtDlpExecPath != '':
                log.info(f"Found yt-dlp executable {quoted(self.sYtDlpExecPath)}")
