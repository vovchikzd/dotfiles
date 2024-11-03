#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
export SAL_USE_VCLPLUGIN=qt6
export QT_QPA_PLATFORMTHEME=qt6ct
export PATH=$PATH:/home/vovchik/.local/bin
export PATH=$PATH:/usr/local/texlive/2024/bin/x86_64-linux
export MANPATH=$MANPATH:/usr/local/texlive/2024/texmf-dist/doc/man
export INFOPATH=$INFOPATH:/usr/local/texlive/2024/texmf-dist/doc/info
export CMAKE_GENERATOR="Ninja"
export RIPGREP_CONFIG_PATH="/home/vovchik/.config/ripgrep.conf"

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
