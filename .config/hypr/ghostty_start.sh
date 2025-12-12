#!/usr/bin/env bash

ACTIVE_WM_CLASS=$(hyprctl activewindow | grep 'class:')
if [[ $ACTIVE_WM_CLASS == *"ghostty"* ]]; then
  PID=$(hyprctl activewindow | grep 'pid:' | awk '{ print $2; }')
  if [[ "$PID" == "" ]]; then
    ghostty &
  else
    CHILD_PID=$(pgrep -P $PID)
    if [[ "$CHILD_PID" == "" ]]; then
      ghostty &
    else
      pushd "/proc/${CHILD_PID}/cwd" &>/dev/null
      SHELL_CWD=$(/usr/bin/pwd -P)
      popd &>/dev/null
      ghostty --working-directory="$SHELL_CWD" &
    fi
  fi
else
  ghostty &
fi
