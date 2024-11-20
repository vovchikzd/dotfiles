#!/usr/bin/env bash

confd='/home/vovchik/dotfiles/.config/hypr/'
dir='/home/vovchik/dotfiles/images/wallpapers/'

cd "$dir"
papers=("${dir}"*)
cd "$confd"

length=${#papers[@]}

rand=$((1 + $RANDOM % $length - 1))

wallp=${papers[$rand]}

cat << EOF > ./hyprpaper.conf
preload = $wallp
wallpaper = , $wallp
EOF

/usr/bin/hyprpaper &
