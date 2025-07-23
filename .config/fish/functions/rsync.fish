function rsync
  command rsync -rPahvc --delete-delay --exclude='**/lost+found/' $argv
end
