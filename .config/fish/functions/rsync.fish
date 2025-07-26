function rsync
  command rsync -rPahv --delete-delay --exclude='**/lost+found/' $argv
end
