#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h \W]\$ '

if [ -f $HOME/.bash_aliases ]; then
  source $HOME/.bash_aliases
fi

if [ -f $HOME/.bash_env ]; then
  source $HOME/.bash_env
fi

if [ -f $HOME/.bash_functions ]; then
  source $HOME/.bash_functions
fi

if ! [ -L /home/vovchik/.local/bin/acp ]; then
  if [ -f '/home/vovchik/Disks/1Tb/projects/c/advcpmv/advcp' ]; then
    ln -s '/home/vovchik/Disks/1Tb/projects/c/advcpmv/advcp' /home/vovchik/.local/bin/acp
  fi
fi

if ! [ -L /home/vovchik/.local/bin/amv ]; then
  if [ -f '/home/vovchik/Disks/1Tb/projects/c/advcpmv/advmv' ]; then
    ln -s '/home/vovchik/Disks/1Tb/projects/c/advcpmv/advmv' /home/vovchik/.local/bin/amv
  fi
fi

eval "$(zoxide init --cmd cd bash)"
eval "$(starship init bash)"
