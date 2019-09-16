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

Plugin 'terryma/vim-multiple-cursors'

Plugin 'tpope/vim-eunuch'

Plugin 'rstacruz/vim-closer'

Plugin 'rhysd/clever-f.vim'

Plugin 'Valloric/YouCompleteMe'

Plugin 'ajh17/VimCompletesMe'

Plugin 'mhinz/vim-startify'

Plugin 'https://gitlab.com/Lenovsky/nuake.git'

Plugin 'ajmwagar/vim-deus'

Plugin 'vim-syntastic/syntastic'

Plugin 'nvie/vim-flake8'

Plugin 'vim-python/python-syntax'

"Plugin 'morhetz/gruvbox'
"Plugin 'jnurmine/Zenburn'
"Plugin 'ayu-theme/ayu-vim'
"Plugin 'gilgigilgil/anderson.vim'
"Plugin 'dracula/vim'
"Plugin 'joshdick/onedark.vim'

"Plugin 'Yggdroot/indentLine'

"Plugin 'tpope/vim-fugitive'
"Plugin 'airblade/vim-gitgutter'

"Plugin 'vim-scripts/indentpython.vim'

"Plugin 'sheerun/vim-polyglot'

"Plugin 'numirias/semshi', {'do': ':UpdateRemotePlugins'} " Semantic highlight for Python

call vundle#end()            " required
filetype plugin indent on    " required

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
set lazyredraw

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
map <F1> :NERDTreeToggle<CR>
map <F2> :NERDTreeFind<CR>
nnoremap <Space> :
" let mapleader = \<Space>"

map j gj
map k gk

" move between tabs
nnoremap <C-Down> :tabprevious<CR>
nnoremap <C-Up> :tabnext<CR>

" move between buffers
map <C-Right> <Esc>:bnext<CR>
map <C-Left> <Esc>:bprev<CR>

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

nnoremap <F4> :Nuake<CR>
inoremap <F4> <C-\><C-n>:Nuake<CR>
tnoremap <F4> <C-\><C-n>:Nuake<CR>

" *** END OF KEYMAPS ***

syntax on

let g:python_highlight_all=1

" Python indentations
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

"highlight BadWhitespace ctermbg=red guibg=red
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

highlight BadWhitespace ctermbg=red guibg=red

let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Airline 
let g:airline_theme='deus'
let g:airline#extensions#tabline#enabled = 1
"let g:airline_left_sep = ' ❤  '
"let g:airline_right_sep = ' 🟆  '
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline_powerline_fonts = 1
"let g:airline#extensions#tabline#fnamemod = ':p:.'
let g:airline#extensions#tabline#buffer_nr_show = 0
let g:airline#extensions#whitespace#enabled = 0
let g:airline#extensions#tabline#buffer_min_count = 1
"let g:airline#extensions#tabline#fnamecollapse = 1

set showtabline=0

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
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif " autoquit if only nerdtree is open
autocmd bufenter * if &filetype == "nerdtree" | silent exe substitute(mapcheck("R"), "<CR>", "", "") | endif

