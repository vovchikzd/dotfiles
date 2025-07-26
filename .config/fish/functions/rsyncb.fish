function rsyncb
  command rsync -rPahv --delete-before --exclude='**/lost+found/' $argv
end
