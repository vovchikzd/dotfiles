#!/usr/bin/env bash

ACTIVE_WM_CLASS=$(hyprctl activewindow | grep 'class:')
if [[ $ACTIVE_WM_CLASS == *"wezterm"* ]]
then
    PID=$(hyprctl activewindow | grep 'pid:' | awk '{ print $2; }')
    if [[ "$PID" == "" ]]
    then
        /usr/bin/wezterm start --always-new-process &
    fi
    CHILD_PID=$(pgrep -P $PID)
    if [[ "$CHILD_PID" == "" ]]
    then
        /usr/bin/wezterm start --always-new-process &
    fi
    # Get current directory of child. The first child should be the shell.
    pushd "/proc/${CHILD_PID}/cwd" &>/dev/null
    SHELL_CWD=$(pwd -P)
    popd &>/dev/null
    /usr/bin/wezterm start --cwd "$SHELL_CWD" --always-new-process &
else
    /usr/bin/wezterm start --always-new-process &
fi
