#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if ! which 'clang++' &>/dev/null; then
  export CXX=g++
else
  export CXX=clang++
fi

if ! which 'clang' &>/dev/null; then
  export CC=gcc
else
  export CC=clang
fi

. "$HOME/.cargo/env"

# Hyprland start
# if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
if [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec Hyprland
fi
