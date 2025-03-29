#!/usr/bin/env bash

TMP_DIR="${PWD}/NERD_FONTS_TMP"
CUR_DIR="$PWD"

if [ -d "$TMP_DIR" ]; then
  printf '\033[0;31mDirectory already exists\033[0m\n'
  exit 1
fi

install_fonts() {
  mkdir -p "$TMP_DIR" && cd "$TMP_DIR" || return 1

  git clone --depth=1 'https://github.com/ryanoasis/nerd-fonts.git' || return 1

  cd nerd-fonts/patched-fonts || return 1

  if ! [ -d /usr/local/share/fonts/ ]; then
    printf 'password here' | sudo -S mkdir /usr/local/share/fonts || return 1
  fi

  printf 'password here' | sudo -S find . -type f -regextype posix-egrep -iregex '.*\.(otf|ttf)$' -exec bash -c 'mv "$0" "$@" /usr/local/share/fonts/' {} + || return 1

  cd "$CUR_DIR" && rm -fr "$TMP_DIR" || return 1

  fc-cache -fv
}

install_fonts
unset -f install_fonts

if ! [ "$PWD" == "$CUR_DIR" ]; then
  cd "$CUR_DIR"
fi

if [ -d "$TMP_DIR" ]; then
  rm -fr "$TMP_DIR"
fi
