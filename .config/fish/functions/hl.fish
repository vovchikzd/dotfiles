function hl --wraps rg
  command rg --passthru --no-line-number $argv
end
