function grep --wraps grep
  command grep --color=auto -IE --exclude-dir='lost+found' $argv
end
