#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Hyprland start
# if systemctl -q is-active graphical.target && [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
if [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec Hyprland
fi
