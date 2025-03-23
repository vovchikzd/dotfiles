fmpv() {
  if [ "$#" -ne 1 ]; then
    printf "\033[0;31mToo many files passed\033[0m\n" >&2
    return 1
  elif [[ $1 == "" ]]; then
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
         "mdbook"
         "serie"
         "repgrep"
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
  printf "$PWD/$1"
}

function cpwd() {
  printf "$PWD/$1" | wl-copy
}

function add_favorites() {
  ~/dotfiles/add_favorite.py "$@"
}

function eread() {
  foliate "$1" &>/dev/null &
}

# function eat() {
#   if [ "$#" -ne 3 ]; then
#     printf "\033[0;31mRequired 3 parameters: proteins, fats and carbohydrate\033[0m\n" >&2
#     return 1
#   fi
#   proteins=$1
#   fats=$2
#   carbohydrate=$3
#   ccal=$(eva -f3 "4.1 * $proteins + 9.29 * $fats + 4.1 * $carbohydrate")
#   joule=($(eva -f3 "17.2 * $proteins + 38.9 * $fats + 17.2 * $carbohydrate"))
#   printf "${ccal} kCal\n"
#   printf "${joule} kJ\n"
# }

# ffmpeg-sub() {
#   if [ "$#" -ne 3 ]; then
#     printf "\033[0;31mRequired 3 parameters: input_video input_subtitles and output_video\033[0m\n" >&2
#     return 1
#   elif ! [ -f "$1" ]; then
#     printf "\033[0;31mFile \"$1\" doesn't exist\033[0m\n" >&2
#     return 1
#   elif ! [ -f "$2" ]; then
#     printf "\033[0;31mFile \"$2\" doesn't exist\033[0m\n" >&2
#     return 1
#   elif [ -f "$3" ]; then
#     printf "\033[0;31mFile \"$3\" already exist\033[0m\n" >&2
#     return 1
#   fi
#
#   ffmpeg -i "$1" -i "$2" -c copy -c:s mov_text -metadata:s:s:0 language=eng "$3"
# }
