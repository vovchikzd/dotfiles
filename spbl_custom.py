#!/usr/bin/env python3

import os, sponsorblock as sb, sys
from subprocess import run

CATEGORIES = ["sponsor", "interaction", "intro", "preview", "outro", "selfpromo", "hook"]

def cleanRanges(ranges):
    result = list()
    for start, end in sorted(ranges):
        if len(result) > 0 and start <= result[-1][1]:
            result[-1] = (result[-1][0], end)
        else:
            result.append((start, end))
    return result

def getSaveRanges(ranges, nDuration):
    result = list()
    nLclStart = 0.0
    for start, end in sorted(ranges):
        if start == nLclStart:
            nLclStart = end
        elif nLclStart >= nDuration:
            return result
        else:
            result.append((nLclStart, start))
            nLclStart = end
    if nLclStart < nDuration:
        result.append((nLclStart, nDuration))
    return result

def main(sFilePath, sWebUrl, sDuration):
    if not os.path.isfile(sFilePath):
        exit(0)

    spnbl_segments: list[sb.Segment] = list()
    try:
        spnbl_segments = sb.Client(no_env=True, default_categories=CATEGORIES).get_skip_segments(sWebUrl)
    except (ValueError, sb.errors.NotFoundException):
        pass
    except:
        print(f"Some unhandled exception occured", file=sys.stderr)
        exit(2)

    print(f"Found {len(spnbl_segments)} segments in sponsorblock database")
    if len(spnbl_segments) == 0:
        exit(0)

    nDuration = float(sDuration)
    if round(spnbl_segments[-1].end) == nDuration:
        spnbl_segments[-1].end = nDuration

    if any([seg.end > nDuration for seg in spnbl_segments]):
        print("Looks like file is ulready trimmed")
        exit(0)

    naCleanSkipRanges = cleanRanges([(s.start, s.end) for s in spnbl_segments])
    naSaveRanges = getSaveRanges(naCleanSkipRanges, nDuration)

    saTmpFiles = list()
    def delTmp():
        for sTmpFile in saTmpFiles:
            if os.path.isfile(sTmpFile):
                os.remove(sTmpFile)

    sNamePath, sExt = os.path.splitext(sFilePath)
    sCoverFile = f"{sNamePath}.png"
    saTmpFiles.append(sCoverFile)
    print(f"Extracting thumbnail to '{sCoverFile}'")
    try:
        getCoverRes = run([
            "ffmpeg", "-y", "-i", sFilePath
            , "-map", "0:v", "-map", "-0:V"
            , "-c", "copy"
            , sCoverFile
        ], capture_output=True)
        if getCoverRes.returncode != 0:
            print("Error while extracting thumbnail. Continue without cover.", file=sys.stderr)
            delTmp()
    except:
        print("Error while extracting thumbnail. Continue without cover.", file=sys.stderr)
        delTmp()

    sNoMetaFile = f"{sNamePath}.no_meta.tmp{sExt}"
    saTmpFiles.append(sNoMetaFile)
    sOrigFile = f"{sNamePath}.orig.uncut{sExt}"
    os.rename(sFilePath, sOrigFile)
    print(f"Renamed '{sFilePath}' -> '{sOrigFile}'")

    saFilters = list()
    sConcatFlt = ""
    for cnt, (start, end) in enumerate(naSaveRanges, 1):
        print(f"{start} -> {end}")
        sVidOut = f"[v{cnt:03}]"
        sAudOut = f"[a{cnt:03}]"
        if start == 0.0:
            saFilters.append(f"[0:v]trim=end={end},setpts=PTS-STARTPTS{sVidOut}")
            saFilters.append(f"[0:a]atrim=end={end},asetpts=PTS-STARTPTS{sAudOut}")
        elif end == nDuration:
            saFilters.append(f"[0:v]trim=start={start},setpts=PTS-STARTPTS{sVidOut}")
            saFilters.append(f"[0:a]atrim=start={start},asetpts=PTS-STARTPTS{sAudOut}")
        else:
            saFilters.append(f"[0:v]trim=start={start}:end={end},setpts=PTS-STARTPTS{sVidOut}")
            saFilters.append(f"[0:a]atrim=start={start}:end={end},asetpts=PTS-STARTPTS{sAudOut}")
        sConcatFlt += f"{sVidOut}{sAudOut}"
    saFilters.append(f"{sConcatFlt}concat=n={len(naSaveRanges)}:v=1:a=1[v][a]")

    print("Modifying chapters")
    try:
        sConvRes = run([
            "ffmpeg", "-i", sOrigFile
            , "-filter_complex", ';'.join(saFilters)
            , "-map", "[v]", "-map", "[a]"
            , sNoMetaFile
        ], capture_output=True)
        if sConvRes.returncode != 0:
            os.rename(sOrigFile, sFilePath)
            delTmp()
            print("Error while modifying chapters. Exiting.")
            exit(1)
    except:
        os.rename(sOrigFile, sFilePath)
        delTmp()
        print("Error while modifying chapters. Exiting.")
        exit(1)

    print("Adding metadata")
    try:
        addMetaRes = run([
            "ffmpeg", "-i", sNoMetaFile, "-i", sOrigFile
            , "-map", "0", "-map_metadata", "1", "-map_chapters", "-1"
            , "-c", "copy"
            , "-attach", sCoverFile
            , "-metadata:s:t", "mimetype=image/png"
            , "-metadata:s:t", "filename=cover.png"
            , sFilePath
        ], capture_output=True)
        if addMetaRes.returncode != 0:
            if os.path.isfile(sFilePath):
                os.remove(sFilePath)
            os.rename(sOrigFile, sFilePath)
            delTmp()
            print("Error adding metadata. Exiting.")
            exit(1)
    except:
        if os.path.isfile(sFilePath):
            os.remove(sFilePath)
        os.rename(sOrigFile, sFilePath)
        delTmp()
        print("Error adding metadata. Exiting.")
        exit(1)

    delTmp()
    if os.path.isfile(sOrigFile):
        os.remove(sOrigFile)

if __name__ == "__main__":
    main(*sys.argv[1:])
