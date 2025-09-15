#!/usr/bin/env bash

TARGET_DIR="~/yay_src"
CURRENT_DIR="$PWD"

if [ -d "$TARGET_DIR" ]; then
  printf 'Download directory already exists\n'
  exit 1
fi

mkdir "$TARGET_DIR" && cd "$TARGET_DIR" || exit $?

sudo pacman -S --needed git base-devel || exit $?

git clone https://aur.archlinux.org/yay.git || exit $?

cd yay || exit $?

makepkg -si || exit $?

cd "$CURRENT_DIR"

rm -r "$TARGET_DIR"
