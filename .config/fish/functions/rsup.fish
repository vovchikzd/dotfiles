function rsup --description 'Update rust and all apps'
  command rustup update; or return 1
  set progs bat cpc fd-find procs ripgrep sd starship tokei dua-cli zoxide\
    difftastic neocmakelsp yazi-fm yazi-cli eza tealdeer bacon mdbook\
    serie repgrep typst-cli
  # bottom 
  for prog in $progs
    command cargo install $prog --locked; or return 1
  end
end
