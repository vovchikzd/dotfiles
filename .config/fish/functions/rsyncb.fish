function rsyncb --wraps rsync
  command rsync -rPSahv --preallocate --delete-before --exclude='**/lost+found/' --exclude='**/ytdl_tmp/' $argv
end
