function get_meta --wraps ffprobe
  if test (count $argv) != 2
    printf 'Error: required 2 arguments\n\tget_meta <meta name> <file>\n' >/dev/stderr
    return 69
  end
  command ffprobe -hide_banner -v error -show_entries format_tags=$argv[1] -of default=noprint_wrappers=1:nokey=1 $argv[2]
end
