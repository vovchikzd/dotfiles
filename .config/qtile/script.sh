#!/usr/bin/env bash

ACTIVE_WINDOW=$(xdotool getactivewindow)
ACTIVE_WM_CLASS=$(xprop -id $ACTIVE_WINDOW | grep WM_CLASS)
#if [[ $ACTIVE_WM_CLASS == *"Alacritty"* ]]
if [[ $ACTIVE_WM_CLASS == *"wezterm"* ]]
then
    # Get PID. If _NET_WM_PID isn't set, bail.
    PID=$(xprop -id $ACTIVE_WINDOW | grep _NET_WM_PID | grep -oP "\d+")
    if [[ "$PID" == "" ]]
    then
        # /home/vovchik/.cargo/bin/alacritty
        prime-run /usr/bin/wezterm
    fi
    # Get first child of terminal
    CHILD_PID=$(pgrep -P $PID)
    if [[ "$CHILD_PID" == "" ]]
    then
        # /home/vovchik/.cargo/bin/alacritty
        prime-run /usr/bin/wezterm
    fi
    # Get current directory of child. The first child should be the shell.
    pushd "/proc/${CHILD_PID}/cwd" &>/dev/null
    SHELL_CWD=$(pwd -P)
    popd &>/dev/null
    # Start alacritty with the working directory
    # /home/vovchik/.cargo/bin/alacritty --working-directory "$SHELL_CWD"
    prime-run /usr/bin/wezterm start --cwd "$SHELL_CWD"
else
    # /home/vovchik/.cargo/bin/alacritty
    prime-run /usr/bin/wezterm
fi
