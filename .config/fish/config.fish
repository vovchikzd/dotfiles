# Commands to run in interactive sessions can go here
if status is-interactive
  set dlt '/home/vovchik/Disks/1Tb/Видео/Delete/'
  set plt '/home/vovchik/Disks/1Tb/Видео/playlists/'
  
  set -g format 'bv*[height=720]+ba[language~="en.*"]+ba[language~="ru.*"] / bv[height=1080]+ba[language~="en.*"]+ba[language~="ru.*"] / bv+ba/b'
  set -g lformat 'bv[height=1080]+ba[language~="en.*"]+ba[language~="ru.*"] / bv+ba/b'
  set -g bformat "bv+ba/b"
  set -g name '%(title)s [%(id)s](%(channel)s).%(ext)s'
  set -g numbering "%(playlist_index)s. $name"
  set -g playlist "%(playlist)s [%(playlist_id)s]"
  set -g playlist_numbering "$playlist/$numbering"
  set -g tor_proxy 'socks5://localhost:9150'
  # autonumber yt-dlp --autonumber-start 14 $URL -o "%(autonumber)s. %(title)s [%(id)s].%(ext)s"

  set fish_user_paths /home/vovchik/.cargo/bin $HOME/.local/bin


  starship init fish | source
  zoxide init --cmd cd fish | source
end
