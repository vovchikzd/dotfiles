function vsub --wraps whisper
  whisper -f srt --verbose True --model large-v3 --max_line_count 2 --max_line_width 25 --word_timestamps True $argv
end
