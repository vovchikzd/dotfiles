function rsync --wraps rsync
  command rsync -rPSahv --preallocate --delete-delay \
    --exclude='**/lost+found/' \
    --exclude='**/ytdl_tmp/' \
    --exclude='**/.xmake/' \
    --exclude='**/.cache/' \
    --exclude='**/.build/' \
    --exclude='**/.zig-cache/' \
    --exclude='**/zig-out/' \
    --exclude='**/zig-pkg/' \
    --exclude='**/mpv_cache/' \
    --exclude='**/*.!qB' \
    $argv
end
