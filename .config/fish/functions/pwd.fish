function pwd --description "I need '/' in the end of dir and don't need newline, plus append passed file/dir"
  printf '%s/%s' $PWD $argv[1]
end
