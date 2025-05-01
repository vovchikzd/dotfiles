#!/usr/bin/env bash

ACTIVE_WM_CLASS=$(hyprctl activewindow | grep 'class:')
if [[ "$ACTIVE_WM_CLASS" == *"wezterm"* ]]; then
  PID=$(hyprctl activewindow | grep 'pid:' | cut -d' ' -f2)
  if [[ "$PID" == "" ]]; then
    /usr/bin/wezterm start --always-new-process --class yazi -e /home/vovchik/.cargo/bin/yazi &
  else
    CHILD_PID=$(pgrep -P $PID)
    if [[ "$CHILD_PID" == "" ]]; then
      /usr/bin/wezterm start --always-new-process --class yazi -e /home/vovchik/.cargo/bin/yazi &
    else
      pushd "/proc/${CHILD_PID}/cwd" &>/dev/null
      SHELL_CWD=$(/usr/bin/pwd -P)
      popd &>/dev/null
      /usr/bin/wezterm start --always-new-process --class yazi -e /home/vovchik/.cargo/bin/yazi "$SHELL_CWD" &
    fi
  fi
else
  /usr/bin/wezterm start --always-new-process --class yazi -e /home/vovchik/.cargo/bin/yazi &
fi
