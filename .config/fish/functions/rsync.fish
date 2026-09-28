function rsync --wraps rsync
  command rsync -rPSahv --preallocate --delete-delay --delete-excluded \
    --exclude='**/lost+found/' \
    --exclude='**/ytdl_tmp/' \
    --exclude='**/qbit_tmp/' \
    --exclude='**/.xmake/' \
    --exclude='**/.cache/' \
    --exclude='**/.build/' \
    --exclude='**/.zig-cache/' \
    --exclude='**/zig-out/' \
    --exclude='**/zig-pkg/' \
    --exclude='**/mpv_cache/' \
    --exclude='**/*.!qB' \
    --exclude='**/*.zip.part' \
    --exclude='**/*.tmp.mkv' \
    $argv
end
