function ffmpeg --wraps ffmpeg
  printf '\x1b[?25l'
  command ffmpeg -nostdin -hide_banner $argv
  set -l ffmpeg_exit_status $status
  printf '\x1b[?25h'
  return $ffmpeg_exit_status
end
