#!/usr/bin/env python3
# git update-index --chmod=+x <path to file inside git repo>

import os, sys, tempfile
from pathlib import Path
from subprocess import CompletedProcess, run

# https://git-scm.com/docs/githooks#_prepare_commit_msg
saCheckMessageTypes: list[str] = ["message", "template"]
saNotCheckMessageTypes: list[str] = ["merge", "squash", "commit"]
saSkipMessageTypes: list[str] = saCheckMessageTypes + saNotCheckMessageTypes

saChangeTypes: list[str] = ["feat", "fix", "chore"]

def createSkipLockFile():
    sSkipFileName: str = "git_skip_msg_check.lock"
    sTmpDir: str = tempfile.gettempdir()
    sSkipFilePath: str = os.path.join(sTmpDir, sSkipFileName)
    Path(sSkipFilePath).touch()

def getCommentStr() -> str:
    sCommentStr: str = "#"
    saGetCommentCharCmd: list[str] = ["git", "config", "core.commentChar"]
    try:
        getCommentCharRes: CompletedProcess[str] = run(saGetCommentCharCmd, capture_output=True, text=True, encoding="utf-8")
        if getCommentCharRes.returncode == 0 and getCommentCharRes.stdout.strip():
            sCommentStr = getCommentCharRes.stdout.strip()
        else:
            saGetCommentStrCmd: list[str] = ["git", "config", "core.commentString"]
            getCommentStrRes: CompletedProcess[str] = run(saGetCommentStrCmd, capture_output=True, text=True, encoding="utf-8")
            if getCommentStrRes.returncode == 0 and getCommentStrRes.stdout.strip():
                sCommentStr = getCommentStrRes.stdout.strip()
    except:
        pass
    return sCommentStr

def getDirName() -> str:
    sDirStub: str = "<directory name>"
    sGetRootCmd: list[str] = ["git", "rev-parse", "--show-toplevel"]
    try:
        getRootRes: CompletedProcess[str] = run(sGetRootCmd, capture_output=True, text=True, encoding="utf-8")
        if getRootRes.returncode == 0 and getRootRes.stdout.strip():
            sDirStub = os.path.basename(getRootRes.stdout.strip())
    except:
        pass
    return sDirStub

def main():
    args: list[str] = sys.argv[1:]
    sMsgFilePath: str = args[0]
    sMsgType: str = args[1] if len(args) >= 2 else ""

    if sMsgType in saSkipMessageTypes:
        if sMsgType in saNotCheckMessageTypes:
            createSkipLockFile()
        exit(0)

    sCommentStr: str = getCommentStr()
    sDirName: str = getDirName()
    with open(sMsgFilePath, "w") as msg:
        for sChangeType in saChangeTypes:
            print(f"{sCommentStr} {sChangeType}({sDirName}):  #issue <issue number>", file=msg)


if __name__ == "__main__":
    main()
