function rsyncb
  command rsync -rPSahv --preallocate --delete-before --exclude='**/lost+found/' $argv
end
