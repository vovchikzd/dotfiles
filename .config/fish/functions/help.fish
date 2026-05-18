function help
  command $argv --help | nvim -R -c "set nomodifiable" -
end
