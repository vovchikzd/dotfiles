#!/usr/bin/env python3

import os, mimetypes

def get_mime(sFilePath):
    return mimetypes.guess_type(sFilePath)[0]

def isVideo(sFilePath):
    type = get_mime(sFilePath)
    return type is not None and 'video' in type

def main():
    saDirs = ['.']
    while len(saDirs) > 0:
        sDir = saDirs.pop(0)
        for file in os.listdir(sDir):
            if "lost+found" in file:
                continue

            sFilePath = f"{sDir}/{file}"
            if os.path.isdir(sFilePath):
                saDirs.append(sFilePath)

            if os.path.isfile(sFilePath) and isVideo(sFilePath):
                sNewTitle = file
                if ':' in file:
                    sNewTitle = sNewTitle.replace(':', '')
                if "'" in file:
                    sNewTitle = sNewTitle.replace("'", '’')
                if "ё" in file:
                    sNewTitle = sNewTitle.replace("ё", "е")
                if sNewTitle != file:
                    os.rename(sFilePath, f"{sDir}/{sNewTitle}")
                    print(f"renamed '{sFilePath}' -> '{sDir}/{sNewTitle}'")

if __name__ == "__main__":
    main()
