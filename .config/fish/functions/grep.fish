function grep --wraps grep
  command grep --color=auto -IErn --exclude-dir='lost+found' $argv
end
