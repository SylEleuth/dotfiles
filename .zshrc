export ZSH="/home/eleuth/.oh-my-zsh"

POWERLEVEL9K_MODE="nerdfont-complete"
ZSH_THEME="powerlevel9k/powerlevel9k"

RANGER_LOAD_DEFAULT_RC="false"
PAGER="nvim"
VISUAL="nvim"
EDITOR="nvim"

TERM=xterm-256color

plugins+=(
	git
	zsh-autosuggestions
	zsh-completions
	k
    auto-notify
	)

autoload -U compinit && compinit

source $ZSH/oh-my-zsh.sh

compinit -d ~/.cache/zsh/zcompdump-$ZSH_VERSION

alias vi="/usr/bin/vim"
alias vim="nvim"
alias vi3="nvim ~/.config/i3/config"
alias vimconfig="nvim ~/.config/nvim/init.vim"

alias cd..='cd ..'
alias ..='cd ..'
alias ...='cd ../..'
alias ~='cd ~'
alias cls='clear'
alias s='sudo'
alias l="ls -la"
alias la="ls -AF ${colorflag}"
alias ll="ls -lFh ${colorflag}"
alias lld="ls -l | grep ^d"
alias rm="rm -i"
alias weather="curl wttr.in/Preston"
alias seriale="cd ~//Data/Videos/seriale" 
alias movies="cd ~/Data/Videos/movies" 
alias anime="cd ~/Data/Videos/anime" 
alias videos="cd ~/Data/Videos" 
alias dl="cd ~/Downloads" 
alias bl="cd ~/Data/Blender" 
alias rip="youtube-dl" 
alias ripau="youtube-dl --extract-audio --audio-format mp3" 
alias logsdel="find ~/Dropbox/.mozilla/firefox/pnlhpvgc.Eleuth/weave/logs/ -name "*.txt" -type f"


POWERLEVEL9K_PROMPT_ON_NEWLINE=true
# POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=''
POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX="%F{blue}\u2570%F{blue}\uF460%F{blue}\uF460%F{blue}\uF460%f "
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX='%F{blue}╭%F{blue}'
# POWERLEVEL9K_MULTILINE_LAST_PROMPT_PREFIX='%F{blue}╰%f '
# POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
# POWERLEVEL9K=truncate_beginning
POWERLEVEL9K_TIME_BACKGROUND=black
POWERLEVEL9K_TIME_FOREGROUND=white
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_VCS_CLEAN_FOREGROUND=black
POWERLEVEL9K_VCS_CLEAN_BACKGROUND=green
POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND=black
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND=yellow
POWERLEVEL9K_VCS_MODIFIED_FOREGROUND=white
POWERLEVEL9K_VCS_MODIFIED_BACKGROUND=black
POWERLEVEL9K_COMMAND_EXECUTION_TIME_BACKGROUND=black
POWERLEVEL9K_COMMAND_EXECUTION_TIME_FOREGROUND=blue
POWERLEVEL9K_FOLDER_ICON=
POWERLEVEL9K_STATUS_OK_IN_NON_VERBOSE=true
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD=0
POWERLEVEL9K_VCS_UNTRACKED_ICON=●
POWERLEVEL9K_VCS_UNSTAGED_ICON=±
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON=↓
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON=↑
POWERLEVEL9K_VCS_COMMIT_ICON=' '
POWERLEVEL9K_CUSTOM_OS_ICON_BACKGROUND=red
POWERLEVEL9K_CUSTOM_OS_ICON_FOREGROUND=white
POWERLEVEL9K_WHITESPACE_BETWEEN_LEFT_SEGMENTS="  "
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(ssh root_indicator dir dir_writable vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status background_jobs time)
