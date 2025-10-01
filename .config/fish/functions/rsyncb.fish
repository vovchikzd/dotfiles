function rsyncb --wraps rsync
  command rsync -rPSahv --preallocate --delete-before --exclude='**/lost+found/' $argv
end
