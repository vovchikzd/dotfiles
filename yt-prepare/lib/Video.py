import lib.Logger as log
from lib.commondef import *

class Video:
    bIsSilent = False

    sVideoUrl = None
    nVideoNumber = None
    sVideoName = None
    sOutputDir = None
    saYtDlpArgs = list()

    def parseArgs(self, args):
        while len(args) > 0:
            arg = args.pop(0)
            match arg:
                case "--force":
                    pass

                case "--num":
                    if (len(args) == 0 or args[0].startswith('--')):
                        log.error("'--num' requires followed number")
                    self.nVideoNumber = getNumFromStr(args.pop(0))
                    if self.nVideoNumber is not None and not self.bIsSilent:
                        log.info(f"Set number {self.nVideoNumber} for video {quoted(self.sVideoUrl)}")


    def __init__(self, args, bIsSilent = False):
        self.bIsSilent = bIsSilent
        if (len(args) == 0 or not isUrl(args[-1])):
            log.error("Can't find any video link in args")
        if (getLinkType(args[-1]) != 'video' and not "--force" in args):
            log.error("Provided link is not a video link")

        self.sVideoUrl, args = args[-1], args[:-1]
        if not self.bIsSilent:
            log.info(f"Added video link {quoted(self.sVideoUrl)}")
        self.parseArgs(args)
