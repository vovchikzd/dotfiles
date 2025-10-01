function ls --wraps eza
  eza -1 --group-directories-first --classify=always $argv
end
