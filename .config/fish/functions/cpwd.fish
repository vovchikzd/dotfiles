function cpwd
  printf "$PWD/$(string replace -a '%' '%%' $argv[1])" | wl-copy
end
