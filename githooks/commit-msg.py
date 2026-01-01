#!/usr/bin/env python3

import sys, os, tempfile, re

def checkSkipFile() -> bool:
    sSkipFileName: str = "git_skip_msg_check.lock"
    sTmpDir: str = tempfile.gettempdir()
    sSkipFilePath: str = os.path.join(sTmpDir, sSkipFileName)
    bIsFileExists: bool = os.path.isfile(sSkipFilePath)
    if bIsFileExists:
        os.remove(sSkipFilePath)
    return bIsFileExists

def main():
    if checkSkipFile():
        exit(0)

    sMsgFilePath: str = sys.argv[1]

    sFirstLine: str = ""
    with open(sMsgFilePath, "r") as msg:
        sFirstLine = msg.readline().strip()

    sRegex: str = r"^(feat|fix|chore)\(.*\) .* #issue (\d{6}(T|D)|notask)$"
    if not re.match(sRegex, sFirstLine):
        print(f"Commit message doesn't meet the requirements", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
