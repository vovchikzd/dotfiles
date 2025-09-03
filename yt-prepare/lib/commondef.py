import validators, yt_dlp, os, sys, lib.Logger as log

def quoted(msg: str | None):
    if (msg is None or msg == ''):
        return "''"
    
    if (msg[0] == msg[-1] and msg[0] in ("'", '"', '`')):
        return msg

    bIsHasSingle = "'" in msg
    bIsHasDouble = '"' in msg

    if (bIsHasSingle and bIsHasDouble):
        return f"`{msg}`"
    if bIsHasSingle:
        return f'"{msg}"'
    return f"'{msg}'"


def isUrl(sUrl):
    return validators.url(sUrl)


def getLinkType(sUrl):
    saChannelPatterns = ["/channel/", "/c/", "/user/", "/@"]
    if any(pattern in sUrl.lower() for pattern in saChannelPatterns):
        return "channel"

    if "list=" in sUrl.lower():
        return "playlist"

    ydl_opts = {
        "extract_flat": True
        , "quiet": True
        , "no_warnings": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(sUrl, download=False)

            if info.get("_type") == "playlist":
                sWebpadeUrl = info.get("webpage_url", "").lower()

                if any(pattern in sWebpadeUrl for pattern in saChannelPatterns):
                    return "channel"
                return "playlist"
            else:
                if info.get("channel_id") and not info.get("duration"):
                    return "channel"
                return "video"
    except:
        return None


def getNumFromStr(sNum: str):
    def isDigit(sCheck):
        for ch in sCheck:
            if not 48 <= ord(ch) <= 57:
                return False
        return True

    nMultiplier = -1 if sNum.startswith('-') else 1
    sToProc = sNum[1:] if nMultiplier == -1 else sNum
    if (isDigit(sToProc)):
        return int(sToProc) * nMultiplier
    else:
        return None

def findExecPath(sName):
    saPathDirs = os.environ.get("PATH", '').split(os.pathsep)
    saPathDirs.extend(sys.path)
    saFoundedPaths = list()
    for sPathDir in saPathDirs:
        sFilePath = os.path.join(sPathDir, sName)
        if (os.path.isfile(sFilePath) and os.access(sFilePath, os.X_OK)):
            saFoundedPaths.append(sFilePath)

    if len(saFoundedPaths) == 0:
        log.warn(f"Not found {quoted(sName)} executable")
        return ''
    if len(saFoundedPaths) > 1:
        log.warn(f"Found more than one {quoted(sName)} executables")
        return ''
    return saFoundedPaths[0]
