hook global BufSetOption filetype=c %{
    set-option buffer formatcmd 'clang-format --style=file:/home/vovchik/dotfiles/clang-format'
}
hook global BufSetOption filetype=cpp %{
    set-option buffer formatcmd 'clang-format --style=file:/home/vovchik/dotfiles/clang-format'
}
hook global BufSetOption filetype=zig %{
    set-option buffer formatcmd 'zig fmt --stdin'
}
