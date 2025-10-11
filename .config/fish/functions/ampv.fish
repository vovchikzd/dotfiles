function ampv --wraps mpv
  mpv --no-resume-playback --loop-playlist=inf $argv
end
