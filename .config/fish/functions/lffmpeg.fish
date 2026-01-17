function lffmpeg --wraps ffmpeg
  printf '\x1b[?25l'
  command lffmpeg -nostdin -hide_banner $argv
  set -l lffmpeg_exit_status $status
  printf '\x1b[?25h'
  return $lffmpeg_exit_status
end
