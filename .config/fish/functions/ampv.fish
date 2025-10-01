function ampv --wraps mpv
  mpv --no-resume-playback --loop-file=inf --really-quiet $argv
end
