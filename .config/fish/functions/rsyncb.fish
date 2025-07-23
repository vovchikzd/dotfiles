function rsyncb
  command rsync -rPahvc --delete-before --exclude='**/lost+found/' $argv
end
