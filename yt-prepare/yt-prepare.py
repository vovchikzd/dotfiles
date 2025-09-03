#!/usr/bin/env python3

import os, sys, subprocess, yt_dlp
import lib.Logger as log
from lib.commondef import *
from lib.Config import Config

sHelpMessage = (
"""Simple yt-dlp wrapper to write download script for concurrent downloading

Usage: yt-prepare Url [Urls...] [Options...] [-- yt-dlp arguments]

Options:
    -f               force, allow rewriting existing download script
    -h, --help       show this help message
    --ch-num=<num>   numbering created channel folders starting from <num>,
                     any invalid number will be ignored
                     can be changed for specific channel, see '--ch'
    --ch-num         alias for '--ch-num=1'
    --pl-num=<num>   numbering created playlist folders, starting from <num>
                     any invalid number will be ignored
                     can be changed for specific playlist, see '--pl'
    --pl-num         alias for '--pl-num=1'
    --dir-num=<num>  continuous folder numbering, starting from <num>
                     any invalid number will be ignored
                     overrides '--pl-num=<num>' and '--ch-num=<num>'
                     can be changed for specific folder, see '--ch' and '--pl'
    --dir-num        alias for '--dir-num=1'
    --vd-num=<num>   numbering created video files starting from <num>
                     any invalid number will be ignored
                     can be changed for specific video, see '--vd'
    --vd-num         alias for '--vd-num=1'
    -o <file>        out file, allow specify name of ouptut script,
                     default name 'down.py'
    --yt-dlp <path>  path to yt-dlp executable
    --no-dir         doesn't create any subdirectory for channel/playlist,
                     unless otherwise set in channel/playlist settings,
                     see '--vd', '--ch', '--pl'
    --vd             allow to set some settings specific for one video
                     all arguments between this and first url will be use as
                     settings only for that video
                     Allowed settings are:
                       --num <num>    set number for a video
                                      any invalid number will be ignored
                       --name <name>  set name for the video instead of default
                                      template '%(title)s [%(id)s](%(channel)s).%(ext)s'
                                      if starts with number will overwrite '--num <num>'
                       --dir <name>   set output directory <name>
                       --force        forse the link be threated as video even if
                                      it is not recodnized as such
                       --args <args>  all between this and url will be used as yt-dlp args
                                      overwrite '--' option
    --               all after this will be used as yt-dlp args for every download
                     can by overwritten, see '--vd', '--ch', '--pl'
"""
)


def main(argv):
    conf = Config(argv)


if __name__ == "__main__":
    argv = sys.argv
    if ("-h" in argv or "--help" in argv):
        print(sHelpMessage, end='')
        exit(0)
    main(argv)
