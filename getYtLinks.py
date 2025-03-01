#!/usr/bin/env python3

import os, re, sys

sPreamble = "https://www.youtube.com/watch?v="
saTupleQuotes = ('"', "'")
def isQuoted(sToCheck):
    global saTupleQuotes
    return (len(sToCheck) > 1
            and sToCheck[0] == sToCheck[-1]
            and sToCheck[0] in saTupleQuotes)

def quoted(sToQuote):
    if len(sToQuote) == 0:
        return "''"
    if isQuoted(sToQuote):
        return sToQuote
    sQuote = '"' if "'" in sToQuote else "'"
    return f"{sQuote}{sToQuote}{sQuote}"

def fromName(sName):
    global sPreamble
    id = re.findall(r'.*\[(.*)\].*', sName)[0]
    return f"{sPreamble}{id}"

def fromFile(sFile):
    if not os.path.isfile(sFile):
        print(f"File {quoted(sFile)} doesn't exist", file=sys.stderr)
        sys.exit(1)

    saRes = list()
    try:
        with open(sFile, "r") as fFile:
            lines = [strip(line) for line in fFile.readlines() if ('[' in line and ']' in line)]
            saRes.extend([fromName(line) for line in lines])
    except FileNotFoundError:
        print(f"Can't open file {quoted(sFile)}", file=sys.stderr)
        sys.exit(1)
    return saRes

def main(args):
    global sPreamble
    saResLinks = list()
    while len(args) > 0:
        arg = args.pop(0)
        if arg == "-f":
            if len(args) > 0:
                saResLinks.extend(fromFile(args.pop(0)))
            else:
                print(f"File required for '-f' parameter", file=sys.stderr)
                sys.exit(1)
        elif ('[' in arg and ']' in arg):
            saResLinks.append(fromName(arg))
        else:
            saResLinks.append(f"{sPreamble}{arg}")
    print(*[quoted(link) for link in saResLinks], sep='\n')



if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
