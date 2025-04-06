#!/usr/bin/env python3

import subprocess, sys

true = True
false = False

class Config:
    bIsSilent: bool = true
    bIsPrintOut: bool = false
    nWorkspace: int = None
    saToDispatch: list[str] = None

    def isdigit(sCheck: str) -> bool:
        for ch in sCheck:
            if not 48 <= ord(ch) <= 57:
                return false
        return true

    def validateWorkspaceNumber(sPassedNumber: str) -> int:
        if not Config.isdigit(sPassedNumber):
            print("'-w' required non-negative integer argument", file=sys.stderr)
            sys.exit(1)
        nPassedWorkspace: int = None
        try:
            nPassedWorkspace = int(sPassedNumber)
        except:
            print(f"Can't convert `{sPassedNumber}` to int", file=sys.stderr)
            sys.exit(1)
        if nPassedWorkspace <= 0 or nPassedWorkspace > 20:
            print("Number of workspace should be between 1 and 20", file=sys.stderr)
            sys.exit(1)
        return nPassedWorkspace


    def __init__(self, args: list[str]):
        while len(args) > 0:
            arg = args.pop(0)
            match arg:
                case "--no-silent":
                    self.bIsSilent = false
                case "-w" if len(args) > 0:
                    self.nWorkspace = Config.validateWorkspaceNumber(args.pop(0))
                case "-w" if len(args) == 0:
                    print("'-w' required passing number of workspace", file=sys.stderr)
                    sys.exit(1)
                case "--":
                    self.saToDispatch = args.copy()
                    args.clear()
                case "--print":
                    self.bIsPrintOut = true
                case _:
                    print(f"Can't understand what this `{arg}` is mean")
                    sys.exit(1)


def main():
    conf = Config(sys.argv[1:])
    if conf.saToDispatch is None or len(conf.saToDispatch) == 0:
        print("Nothing to dispatch", file=sys.stderr)
        sys.exit(1)
    saToExec: list[str] = ["hyprctl", "dispatch", "--", "exec"]
    if conf.nWorkspace is not None:
        saToAppend: list[str] = ["[workspace", f"{conf.nWorkspace}"]
        if conf.bIsSilent:
            saToAppend.append("silent")
        saToAppend[-1] += ']'
        saToExec.extend(saToAppend)
    saToExec.extend(conf.saToDispatch)
    if conf.bIsPrintOut:
        print(' '.join(saToExec))
    else:
        subprocess.run(saToExec)

if __name__ == "__main__":
    main()
