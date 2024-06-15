alias lg='eza -lh --icons --git --group-directories-first'
alias ll='eza -lh --icons --group-directories-first'
alias lgt='eza -lh --icons --git --tree --group-directories-first'
alias llt='eza -lh --icons --tree --group-directories-first'

alias lga='eza -lhaa --icons --git --group-directories-first'
alias la='eza -lhaa --icons --group-directories-first'
alias lgat='eza -lha --icons --git --tree --group-directories-first'
alias lat='eza -lha --icons --tree --group-directories-first'

alias ls='eza -1 --group-directories-first'
alias lt='eza -1 --tree --group-directories-first'

alias rsup='cargo install bat eva eza fd-find procs ripgrep sd starship tokei alacritty dirstat-rs zoxide difftastic bottom gitui --locked'
alias du='du -sh'
alias srb='source $HOME/.bashrc'
alias list='codium /home/vovchik/External_Drives/1Tb/Книги/Ближайшие\ планы/0.\ Список/list.tex'
alias libr='libreoffice /home/vovchik/External_Drives/1Tb/Библиотека.ods &>/dev/null &'
alias cat=bat
alias pwd='echo -n $PWD/'
alias xclip='xclip -selection c'
alias xclip_get='xclip -selection c -o'
alias bpr="cd '/home/vovchik/External_Drives/1Tb/Книги/compiler_and_operating_system/'"
alias push='git push origin master'

check=/home/vovchik/External_Drives/1Tb/Видео/chek.py
convert=/home/vovchik/External_Drives/1Tb/Видео/convert.py
duration=/home/vovchik/External_Drives/1Tb/Видео/duration.py
alias dr=$duration
delete=/home/vovchik/External_Drives/1Tb/Видео/Delete
plt=/home/vovchik/External_Drives/1Tb/Видео/playlists/

alias umpv='mpv --ytdl-format="(mp4)[height=1080]+ba / bv*[height=1080]+ba / bv*+ba/b"'
alias byt-dlp='yt-dlp --cookies-from-browser Firefox'
# format="(mp4)[height=480]+ba / bv*[height=480]+ba / (mp4)[height=720]+ba / bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
format="bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
lformat="bv*[height=1080]+ba / bv*+ba/b"
name='%(title)s [%(id)s](%(channel)s).%(ext)s'
ename='%(title)s_[%(id)s](%(channel)s).%(ext)s'
numbering="%(playlist_index)s. $name"
enumbering="%(playlist_index)s._$ename"
playlist="%(playlist)s [%(playlist_id)s](%(channel)s)"
eplaylist="%(playlist)s_[%(playlist_id)s](%(channel)s)"
playlist_numbering="$playlist/$numbering"
eplaylist_numbering="$eplaylist/$enumbering"
no_space=--restrict-filenames
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

# eval "$(zoxide init --cmd cd bash)"
# eval "$(starship init bash)"

# alias pipup="pip --disable-pip-version-check list --outdated --format=json | python -c \"import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))\" | xargs -n1 pip install -U"

pipup() {
  GREEN='\033[0;32m'
  RED='\033[0;31m'
  NC='\033[0m' # no color
  list=$(pip --disable-pip-version-check list --outdated --format=json | python -c 'import json, sys; print(" ".join([x["name"] for x in json.load(sys.stdin)]))')
  if [ ! -z "$list" ]
  then
    pip install -U $list || echo -e "${RED}Failed${NC}"
  else
    echo -e "${GREEN}Nothing to upgrade${NC}"
  fi
}

eval $(ssh-agent) &>/dev/null && ssh-add ~/.ssh/id_ed25519 &>/dev/null
