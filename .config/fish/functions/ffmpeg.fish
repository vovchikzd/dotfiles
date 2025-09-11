function ffmpeg
  printf '\x1b[?25l'; command ffmpeg -hide_banner $argv; printf '\x1b[?25h'
end
