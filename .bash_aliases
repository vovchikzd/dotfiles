# eval "$(zoxide init --cmd cd bash)"
# eval "$(starship init bash)"

alias ll='eza -lh --icons --group-directories-first --classify=always'
alias la='eza -lhaa --icons --group-directories-first --classify=always'
alias ls='eza -1 --group-directories-first --classify=always'
alias lt='eza -1 --tree --group-directories-first --classify=always'
alias lsplt='eza -1 --group-directories-first --absolute --no-quotes --classify=always'

alias srb="source $HOME/.bashrc"
alias libr='libreoffice /home/vovchik/dotfiles/list/Библиотека.ods &>/dev/null &'
alias grep='grep --color=always -E'
alias calc='cal -m'
alias atree='ouch l --tree'

alias list='codium "/home/vovchik/Disks/1Tb/Книги/Ближайшие планы/0. Список/list.tex"'

alias mmpv='mpv --no-resume-playback --loop-playlist=inf'
alias ffmpeg='ffmpeg -hide_banner'

dlt=/home/vovchik/Disks/1Tb/Видео/Delete/
plt=/home/vovchik/Disks/1Tb/Видео/playlists

format="bv*[height=720]+ba / bv*[height=1080]+ba / bv*+ba/b"
lformat="bv*[height=1080]+ba / bv*+ba/b"
bformat="bv*+ba/b"
name='%(title)s [%(id)s](%(channel)s).%(ext)s'
numbering="%(playlist_index)s. $name"
playlist="%(playlist)s [%(playlist_id)s]"
playlist_numbering="$playlist/$numbering"
tor_proxy='socks5://localhost:9150'
# autonumber yt-dlp --autonumber-start 14 $URL -o "%(autonumber)s. %(title)s [%(id)s].%(ext)s"
