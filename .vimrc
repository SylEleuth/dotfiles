set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

Plugin 'scrooloose/nerdtree'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'ryanoasis/vim-devicons'

Plugin 'junegunn/fzf'
Plugin 'junegunn/fzf.vim'

Plugin 'philip-karlsson/bolt.nvim', { 'do': ':UpdateRemotePlugins' }

"Plugin 'terryma/vim-multiple-cursors'

"Plugin 'tpope/vim-eunuch'

"Plugin 'vim-syntastic/syntastic'

"Plugin 'rstacruz/vim-closer'

"Plugin 'rhysd/clever-f.vim'

"Plugin 'Valloric/YouCompleteMe'

"Plugin 'ajh17/VimCompletesMe'

Plugin 'ajmwagar/vim-deus'
"Plugin 'morhetz/gruvbox'
"Plugin 'jnurmine/Zenburn'
"Plugin 'ayu-theme/ayu-vim'
"Plugin 'gilgigilgil/anderson.vim'
"Plugin 'dracula/vim'
"Plugin 'joshdick/onedark.vim'

"Plugin 'nvie/vim-flake8'

"Plugin 'Yggdroot/indentLine'

"Plugin 'tpope/vim-fugitive'
"Plugin 'airblade/vim-gitgutter'

"Plugin 'vim-scripts/indentpython.vim'

"Plugin 'sheerun/vim-polyglot'
"Plugin 'vim-python/python-syntax'

"Plugin 'numirias/semshi', {'do': ':UpdateRemotePlugins'} " Semantic highlight for Python

call vundle#end()            " required
filetype plugin indent on    " required

command W :execute ':silent w !sudo tee % > /dev/null' | :edit!
ca w!! w !sudo tee >/dev/null "%"

"colorscheme gruvbox
"set background=dark
"let g:gruvbox_contrast_dark = 'soft'

set termguicolors
colorscheme deus

set ignorecase " Search case insensitive:
set smartcase " .. but not when search pattern contains upper case characters	
set mouse=a " Copy selected text with mouse to system clipboard
set updatetime=250 " If this many milliseconds nothing is typed the swap file will be written to disk
set cursorline

" Buffers
set hidden

" Usable 'Tab'
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set infercase

" Persistent undo
set undofile
set undodir=$HOME/.vim/undo

set undolevels=1000
set undoreload=10000

autocmd VimResized * wincmd =

augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set number norelativenumber
augroup END

" *** KEYMAPS ***
map <F2> :NERDTreeToggle<CR>
map <F3> :NERDTreeFind<CR>
nnoremap <Space> :
" let mapleader = \<Space>"

map j gj
map k gk

" move between tabs
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" move between buffers
map <C-Up> <Esc>:bnext<CR>
map <C-Down> <Esc>:bprev<CR>

nnoremap <leader>l :ls<CR>:b<space>

" move lines up and down
nnoremap <C-j> :m .+1<CR>==
nnoremap <C-k> :m .-2<CR>==
inoremap <C-j> <Esc>:m .+1<CR>==gi
inoremap <C-k> <Esc>:m .-2<CR>==gi
vnoremap <C-j> :m '>+1<CR>gv=gv
vnoremap <C-k> :m '<-2<CR>gv=gv

" switch to left / right split (mostly for Nerd Tree)
map <C-h> <C-W>h
map <C-l> <C-W>l

" *** END OF KEYMAPS ***

syntax on

" Airline 
let g:airline_theme='deus'
let g:airline#extensions#tabline#enabled = 1
let g:airline_left_sep = ' ❤  '
let g:airline_right_sep = ' 🟆  '
"let g:airline#extensions#tabline#formatter = 'jsformatter'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#buffer_nr_show = 0
let g:airline#extensions#whitespace#enabled = 0

set laststatus=2
set encoding=UTF-8

let g:NERDTreeLimitedSyntax = 1
let g:NERDTreeSyntaxDisableDefaultExtensions = 1
let g:NERDTreeDisableExactMatchHighlight = 1
let g:NERDTreeDisablePatternMatchHighlight = 1
let g:NERDTreeHighlightCursorline = 0
let g:NERDTreeWinSize=40
"let g:NERDTreeSyntaxEnabledExtensions = ['py']

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif " autoquit if only nerdtree is open
autocmd bufenter * if &filetype == "nerdtree" | silent exe substitute(mapcheck("R"), "<CR>", "", "") | endif

