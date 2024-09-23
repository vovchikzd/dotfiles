#!/usr/bin/env bash

ACTIVE_WM_CLASS=$(hyprctl activewindow | grep 'class:')
if [[ $ACTIVE_WM_CLASS == *"wezterm"* ]]
then
    # Get PID. If _NET_WM_PID isn't set, bail.
    PID=$(hyprctl activewindow | grep 'pid:' | awk '{ print $2; }')
    if [[ "$PID" == "" ]]
    then
        /usr/bin/wezterm
    fi
    CHILD_PID=$(pgrep -P $PID | head -1)
    if [[ "$CHILD_PID" == "" ]]
    then
        /usr/bin/wezterm
    fi
    # Get current directory of child. The first child should be the shell.
    pushd "/proc/${CHILD_PID}/cwd" &>/dev/null
    SHELL_CWD=$(pwd -P)
    popd &>/dev/null
    # Start alacritty with the working directory
    # /home/vovchik/.cargo/bin/alacritty --working-directory "$SHELL_CWD"
    /usr/bin/wezterm start --cwd "$SHELL_CWD"
else
    # /home/vovchik/.cargo/bin/alacritty
    /usr/bin/wezterm
fi
