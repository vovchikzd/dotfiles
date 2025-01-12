alias ll='eza -lh --icons --group-directories-first --classify=always'
alias la='eza -lhaa --icons --group-directories-first --classify=always'
alias ls='eza -1 --group-directories-first --classify=always'
alias lt='eza -1 --tree --group-directories-first --classify=always'
alias lsplt='eza -1 --group-directories-first --absolute --no-quotes --classify=always'

alias srb='source $HOME/.bashrc'
alias libr='libreoffice /home/vovchik/dotfiles/list/Библиотека.ods &>/dev/null &'
alias grep='grep --color=always -E'
alias calc='cal -m'
alias atree='ouch l --tree'

dlt=/home/vovchik/Disks/1Tb/Видео/Delete/
plt=/home/vovchik/Disks/1Tb/Видео/playlists
alias list='codium "/home/vovchik/Disks/1Tb/Книги/Ближайшие планы/0. Список/list.tex"'
alias llvmup='cd /home/vovchik/Disks/1Tb/projects/cpp/llvm/llvm-project/ && \
  git fetch upstream && \
  git checkout main && \
  git merge upstream/main --ff-only && \
  git push && \
  cd -'

format="bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
lformat="bv*[height=1080]+ba / bv*+ba/b"
bformat="bv*+ba/b"
name='%(title)s [%(id)s](%(channel)s).%(ext)s'
numbering="%(playlist_index)s. $name"
playlist="%(playlist)s [%(playlist_id)s](%(playlist_channel)s)"
playlist_numbering="$playlist/$numbering"
tor_proxy='socks5://localhost:9150'
# autonumber yt-dlp --autonumber-start 14 $URL -o "%(autonumber)s. %(title)s [%(id)s].%(ext)s"

ffmpeg-sub() {
  if [ "$#" -ne 3 ]; then
    printf "\033[0;31mRequired 3 parameters: input_video input_subtitles and output_video\033[0m\n" >&2
    return 1
  elif ! [ -f "$1" ]; then
    printf "\033[0;31mFile \"$1\" doesn't exist\033[0m\n" >&2
    return 1
  elif ! [ -f "$2" ]; then
    printf "\033[0;31mFile \"$2\" doesn't exist\033[0m\n" >&2
    return 1
  elif [ -f "$3" ]; then
    printf "\033[0;31mFile \"$3\" already exist\033[0m\n" >&2
    return 1
  fi

  ffmpeg -i "$1" -i "$2" -c copy -c:s mov_text -metadata:s:s:0 language=eng "$3"
}

fmpv() {
  if [[ $1 == "" ]]; then
    printf "\033[0;31mWhere is playlist file?\033[0m\n" >&2
    return 1
  elif ! [ -f "$1" ]; then
    printf "\033[0;31mFile $1 doesn't exist\033[0m\n" >&2
    return 1
  fi
  printf "mpv --playlist=$1 &>/dev/null & "
  mpv --playlist="$1" &>/dev/null &
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
         "tealdeer"
         "bacon"
       )

  for prog in ${progs[@]}
  do
    cargo install $prog --locked || return 1
  done
}

function yy() {
  clear
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

function pwd() {
  printf "$PWD/$1"
}

function eat() {
  if [ "$#" -ne 3 ]; then
    printf "\033[0;31mRequired 3 parameters: proteins, fats and carbohydrate\033[0m\n" >&2
    return 1
  fi
  proteins=$1
  fats=$2
  carbohydrate=$3
  ccal=$(eva -f3 "4.1 * $proteins + 9.29 * $fats + 4.1 * $carbohydrate")
  joule=($(eva -f3 "17.2 * $proteins + 38.9 * $fats + 17.2 * $carbohydrate"))
  printf "${ccal} kCal\n"
  printf "${joule} kJ\n"
}

. "$HOME/.cargo/env"
eval "$(zoxide init --cmd cd bash)"
eval "$(starship init bash)"

