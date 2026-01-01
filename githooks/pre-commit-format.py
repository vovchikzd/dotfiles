#!/usr/bin/env python3
# git update-index --chmod=+x <path to file inside git repo>

import sys, subprocess

def main():
    gitDiffRes: subprocess.CompletedProcess[str] = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "--", "*.zig", "*.zon"]
        , capture_output=True
        , text=True
        , encoding="utf-8"
    )
    if gitDiffRes.returncode != 0:
        print(gitDiffRes.stderr, file=sys.stderr)
        sys.exit(gitDiffRes.returncode)

    saFilesToFormat: list[str] = [sFile for sFile in gitDiffRes.stdout.split("\n") if sFile.strip()]
    saFormattedFiles: list[str] = list()
    saErrorFiles: list[tuple[str, str]] = list()
    for sFile in saFilesToFormat:
        zigFmtRes: subprocess.CompletedProcess[str] = subprocess.run(["zig", "fmt", sFile], capture_output=True, text=True, encoding="utf-8")
        if zigFmtRes.returncode == 0:
            saFormattedFiles.append(sFile)
        else:
            saErrorFiles.append((sFile, zigFmtRes.stderr))

    if len(saFormattedFiles) > 0:
        gitAddRes: subprocess.CompletedProcess[str] = subprocess.run(["git", "add"] + saFormattedFiles, capture_output=True, text=True, encoding="utf-8")
        if gitAddRes.returncode != 0:
            print(gitAddRes.stderr, file=sys.stderr)
            sys.exit(gitAddRes.returncode)
            
    if len(saErrorFiles) > 0:
        for sFile, sError in saErrorFiles:
            print(f"Error formatting `{sFile}` file", file=sys.stderr)
            print(sError, file=sys.stderr)
            print()
        sys.exit(1)

if __name__ == "__main__":
    main()
