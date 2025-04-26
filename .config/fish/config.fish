# Commands to run in interactive sessions can go here
if status is-interactive
  set dlt '/home/vovchik/Disks/1Tb/Видео/Delete/'
  set plt '/home/vovchik/Disks/1Tb/Видео/playlists/'
  
  set -g format "bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
  set -g lformat "bv*[height=1080]+ba / bv*+ba/b"
  set -g bformat "bv*+ba/b"
  set -g name '%(title)s [%(id)s](%(channel)s).%(ext)s'
  set -g numbering "%(playlist_index)s. $name"
  set -g playlist "%(playlist)s [%(playlist_id)s]"
  set -g playlist_numbering "$playlist/$numbering"
  set -g tor_proxy 'socks5://localhost:9150'
  # autonumber yt-dlp --autonumber-start 14 $URL -o "%(autonumber)s. %(title)s [%(id)s].%(ext)s"

  set -gx SAL_USE_VCLPLUGIN qt6
  set -gx QT_QPA_PLATFORMTHEME qt6ct
  set -gx CMAKE_GENERATOR Ninja
  set -gx MANPAGER 'nvim -c Man! -'

  set -gx XDG_DATA_HOME $HOME/.local/share
  set -gx XDG_CONFIG_HOME $HOME/.config
  set -gx XDG_STATE_HOME $HOME/.local/state
  set -gx XDG_CACHE_HOME $HOME/.cache

  set -gx RIPGREP_CONFIG_PATH $XDG_CONFIG_HOME/ripgrep.conf

  set -gx BROWSER firefox
  set fish_user_paths /home/vovchik/.cargo/bin $HOME/.local/bin


  starship init fish | source
  zoxide init --cmd cd fish | source
end
