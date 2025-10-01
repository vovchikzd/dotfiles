function rsync --wraps rsync
  command rsync -rPSahv --preallocate --delete-delay --exclude='**/lost+found/' $argv
end
