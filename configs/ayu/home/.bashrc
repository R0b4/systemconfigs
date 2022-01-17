#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='exa -la --icons --group-directories-first --no-user --no-time --no-filesize'
alias .='ls'
alias ..='cd ..;.'
alias mkdir='mkdir -p'
alias rmr='rm -r '

alias c='clear'

alias yays='yay -Sv --needed --sudoloop'
alias yayr='yay -Rcns --sudoloop'
alias yayu='yay -Syu --sudoloop'
alias yayc='yay -c --sudoloop'

function mkcd() {
	mkdir $1
	cd $1
}

function nonzero_return() {
	RETVAL=$?
	[ $RETVAL -ne 0 ] && echo " $RETVAL "
}

BashErrorPrompt="\`nonzero_return\`"
BashPromptStart=$'\[\e[30;44m\]  \A\[\e[m\]\[\e[34;42m\]\ue0b0\[\e[m\]\[\e[30;42m\]  \u\[\e[m\]\[\e[32;46m\]\ue0b0\[\e[m\]\[\e[30;46m\]  \w \[\e[m\]\[\e[36;41m\]\ue0b0\[\e[m\]\[\e[30;41m\]'
BashPromptEnd=$'\[\e[m\]\[\e[31m\]\ue0b0\[\e[m\] '
export PS1="$BashPromptStart$BashErrorPrompt$BashPromptEnd"
