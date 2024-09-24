# eval "$(zoxide init --cmd cd bash)"
# eval "$(starship init bash)"

alias ll='eza -lh --icons --group-directories-first'
alias la='eza -lhaa --icons --group-directories-first'
alias ls='eza -1 --group-directories-first'
alias lt='eza -1 --tree --group-directories-first'
alias lsplt="eza -1 --group-directories-first --absolute --no-quotes"

alias srb='source $HOME/.bashrc'
alias libr='libreoffice /home/vovchik/dotfiles/list/Библиотека.ods &>/dev/null &'
alias cat=bat

check=/home/vovchik/Disks/1Tb/Видео/chek.py
convert=/home/vovchik/Disks/1Tb/Видео/duration.py
duration=/home/vovchik/Disks/1Tb/Видео/duration.py
alias dr=$duration
dlt=/home/vovchik/Disks/1Tb/Видео/Delete/
plt=/home/vovchik/Disks/1Tb/Видео/playlists
alias list='codium "/home/vovchik/Disks/1Tb/Книги/Ближайшие планы/0. Список/list.tex"'

# 'yt-dlp --cookies-from-browser Firefox'
# format="(mp4)[height=480]+ba / bv*[height=480]+ba / (mp4)[height=720]+ba / bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
format="bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
lformat="bv*[height=1080]+ba / bv*+ba/b"
name='%(title)s [%(id)s](%(channel)s).%(ext)s'
# ename='%(title)s_[%(id)s](%(channel)s).%(ext)s'
numbering="%(playlist_index)s. $name"
# enumbering="%(playlist_index)s._$ename"
playlist="%(playlist)s [%(playlist_id)s](%(channel)s)"
# eplaylist="%(playlist)s_[%(playlist_id)s](%(channel)s)"
playlist_numbering="$playlist/$numbering"
tor_proxy='socks5://localhost:9150'
# eplaylist_numbering="$eplaylist/$enumbering"
# no_space=--restrict-filenames
# autonumber yt-dlp --autonumber-start 14 $URL -o "%(autonumber)s. %(title)s [%(id)s].%(ext)s"


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

export CMAKE_GENERATOR="Ninja"

fmpv() {
  echo -n "mpv --playlist=$1 &>/dev/null & "
  mpv --playlist=$1 &>/dev/null &
}

rsup() {
  rustup update || return 1
  progs=("bat"
         "eva"
         "fd-find"
         "procs"
         "ripgrep"
         "sd"
         "starship"
         "tokei"
         "dua-cli"
         "zoxide"
         "difftastic"
         "bottom"
         "neocmakelsp"
         "yazi-fm"
         "yazi-cli"
         "eza"
       )

  for prog in ${progs[@]}
  do
    cargo install $prog --locked || return 1
  done
}

function yy() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

function pwd() {
  echo -n $PWD/$1
}
