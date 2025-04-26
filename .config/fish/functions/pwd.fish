function pwd --description "I need '/' in the end of dir and don't need newline, plus append passed file/dir"
  printf "$PWD/$argv[1]"
end
