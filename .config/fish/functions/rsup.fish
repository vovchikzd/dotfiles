function rsup --description 'Update rust and all apps'
  command rustup update; or return $status
  set -l progs bat cpc fd-find procs ripgrep starship tokei dua-cli zoxide\
    difftastic yazi-build eza typst-cli
  for prog in $progs
    command cargo install $prog; or return $status
  end
end
