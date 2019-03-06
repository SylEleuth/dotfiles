set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'scrooloose/nerdtree'

Plugin 'philip-karlsson/bolt.nvim', { 'do': ':UpdateRemotePlugins' }

"Plugin 'terryma/vim-multiple-cursors'

"Plugin 'airblade/vim-gitgutter'

"Plugin 'dracula/vim'
Plugin 'jnurmine/Zenburn'
"Plugin 'morhetz/gruvbox'
"Plugin 'joshdick/onedark.vim'

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

"Plugin 'tpope/vim-fugitive'

"Plugin 'vim-scripts/indentpython.vim'

"Plugin 'Valloric/YouCompleteMe'

"Plugin 'vim-syntastic/syntastic'

Plugin 'rstacruz/vim-closer'

"Plugin 'nvie/vim-flake8'

"Plugin 'Yggdroot/indentLine'

"Plugin 'numirias/semshi', {'do': ':UpdateRemotePlugins'} " Semantic highlight for Python

Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'ryanoasis/vim-devicons'

call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set number norelativenumber
augroup END

" *** KEYMAPS ***
map <C-b> :NERDTreeToggle<CR>
nnoremap <Space> :
" let mapleader = \<Space>"

" move between tabs
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" move between buffers
map <C-Up> <Esc>:bprev<CR>
map <C-Down> <Esc>:bnext<CR>

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

"syntax on
"let python_highlight_all=1

colorscheme zenburn

" set background=dark

" Python indentations                                                                                                               
"au BufNewFile,BufRead *.py
	"\ set tabstop=2 |
	"\ set softtabstop=2 |
	"\ set shiftwidth=4 |
	"\ set textwidth=79 |
	"\ set expandtab |
	"\ set autoindent |
	"\ set fileformat=unix |
	"\ set cursorline

"highlight BadWhitespace ctermbg=red guibg=red
"au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

"let g:ycm_autoclose_preview_window_after_completion=1
"map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Airline 
let g:airline_theme='bubblegum' 
let g:airline#extensions#tabline#enabled = 1
"let g:airline_left_sep = ' ❤  '
"let g:airline_right_sep = ' 🟆  '
let g:airline#extensions#tabline#formatter = 'jsformatter'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#buffer_nr_show = 1

set laststatus=2
set encoding=UTF-8

let g:NERDTreeLimitedSyntax = 1
let g:NERDTreeSyntaxDisableDefaultExtensions = 1
let g:NERDTreeDisableExactMatchHighlight = 1
let g:NERDTreeDisablePatternMatchHighlight = 1
let g:NERDTreeSyntaxEnabledExtensions = ['py']

let g:NERDTreeHighlightCursorline = 0

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif " autoquit if only nerdtree is open

