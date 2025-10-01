function lsblk --wraps lsblk
  command lsblk $argv | bat -pl conf
end
