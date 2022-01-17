function fish_prompt
    set -l laststatus $status
    set -l now (date "+%T")
    set -l arr (printf "\UE0B0")
    set -l here (prompt_pwd)
    echo -en "\033[0;30;44m  $now\033[0;34;42m$arr"
    echo -en "\033[30m  $USER\033[0;32;46m$arr"
    echo -en "\033[30m  $here "
    if test $laststatus -ne 0
        echo -ne "\033[0;36;41m$arr\033[30m $laststatus \033[0;31m$arr"
    else
        echo -ne "\033[0;36m$arr"
    end

    echo -ne "\033[0m "
end

function mkcd
    mkdir $1
    cd $1
end

if status is-interactive
    # Commands to run in interactive sessions can go here
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

    set fish_greeting
end
