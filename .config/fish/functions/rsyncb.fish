function rsyncb --wraps rsync
  command rsync -rPSahv --preallocate --delete-before \
    --exclude='**/lost+found/' \
    --exclude='**/ytdl_tmp/' \
    --exclude='**/.xmake/' \
    --exclude='**/.cache/' \
    --exclude='**/.build/' \
    --exclude='**/.zig-cache/' \
    --exclude='**/zig-out/' \
    $argv
end
