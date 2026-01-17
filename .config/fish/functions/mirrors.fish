function mirrors --wraps refrector --description 'Update mirror list'
  sudo reflector --verbose --save '/etc/pacman.d/mirrorlist' --protocol https --sort rate --latest 50
end
