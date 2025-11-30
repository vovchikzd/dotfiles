# Commands to run in interactive sessions can go here
if status is-interactive
  set dlt '/home/vovchik/Disks/1Tb/Видео/Delete/'
  set plt '/home/vovchik/Disks/1Tb/Видео/playlists/'
  
  set -gx format "bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba / b"
  set -gx lformat "bv*[height=1080]+ba / bv*+ba / b"
  set -gx bformat "bv*+ba / b"
  set -gx name '%(title)s [%(id)s](%(channel)s).%(ext)s'
  set -gx name_orig '%(title)s [%(id)s](%(channel)s).orig.%(ext)s'
  set -gx channel_folder_name "%(channel)s/$name"
  set -gx numbering "%(playlist_index)s. $name"
  set -gx playlist "%(playlist)s"
  set -gx playlist_numbering "$playlist/$numbering"
  set -gx tor_proxy 'socks5://localhost:9150'

  set fish_user_paths /home/vovchik/.cargo/bin $HOME/.local/bin


  starship init fish | source
  zoxide init --cmd cd fish | source
end
