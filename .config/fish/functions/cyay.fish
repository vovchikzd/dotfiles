function cyay
  yay -Sy &>/dev/null; and yay -Qu | sort | tee /dev/stderr | wc -l
end
