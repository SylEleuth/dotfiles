set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim' " Plugin manager
Plugin 'roxma/nvim-yarp' " Remote updates of plugins

Plugin 'vim-airline/vim-airline' " Cool powerline bars
Plugin 'vim-airline/vim-airline-themes'

Plugin 'scrooloose/nerdtree' " A tree explorer plugin <F1>, <F2> for current directory
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'

Plugin 'francoiscabrol/ranger.vim' " Run Ranger in vim <F3>

Plugin 'terryma/vim-multiple-cursors' " Multiple selection <C-n>

Plugin 'mhinz/vim-startify' " Starting screen

Plugin 'https://gitlab.com/Lenovsky/nuake.git' " A Quake-style terminal panel for Neovim and Vim <F4>

" Plugin 'ncm2/ncm2' " Completion framework
" Plugin 'HansPinckaers/ncm2-jedi' " Fast python completion (use ncm2 if you want type info or snippet support)
" Plugin 'ncm2/ncm2-bufword' " Words in buffer completion
" Plugin 'ncm2/ncm2-path' " Filepath completion

" Plugin 'Shougo/neosnippet.vim' " Snippets doh!
" Plugin 'ncm2/ncm2-neosnippet'
" Plugin 'roxma/vim-hug-neovim-rpc'
" Plugin 'Shougo/neosnippet-snippets'

" Plugin 'nvie/vim-flake8' " Python linter <F7>
" Plugin 'davidhalter/jedi-vim' " jedi for python

" Plugin 'Vimjas/vim-python-pep8-indent' " Python indentations
" Plugin 'Chiel92/vim-autoformat' " code formatting <F5>

" Plugin 'kh3phr3n/python-syntax' " Python code highlight

Plugin 'tpope/vim-surround' " Surround words and phrases with parentheses, brackets, quotes, XML tags, and more
Plugin 'jiangmiao/auto-pairs' " Insert or delete brackets, parens, quotes in pair
Plugin 'Yggdroot/indentLine' " Disply the indention levels with thin vertical lines and leading spaces

Plugin 'tpope/vim-commentary' " Comment with 'gcc'

Plugin 'luochen1990/rainbow' " Colored parentheses

Plugin 'kshenoy/vim-signature' " place, toggle and display marks

Plugin 'tpope/vim-fugitive' " Git wrapper
Plugin 'airblade/vim-gitgutter' " Shows git diff

Plugin 'psliwka/vim-smoothie'

Plugin 'ryanoasis/vim-devicons'

"Plugin 'junegunn/fzf' " Fuzzy finder
"Plugin 'junegunn/fzf.vim'

"Plugin 'rbgrouleff/bclose.vim' " deleting a buffer in Vim without closing the window

"Plugin 'vim-syntastic/syntastic' " Syntax checking

"Plugin 'rstacruz/vim-closer'

" ###### COLOR SCHEMES

Plugin 'morhetz/gruvbox' 
Plugin 'sainnhe/gruvbox-material' 

" Plugin 'ajmwagar/vim-deus'
" Plugin 'altercation/vim-colors-solarized' 
" Plugin 'jnurmine/Zenburn' 
" Plugin 'ayu-theme/ayu-vim' 
" Plugin 'gilgigilgil/anderson.vim' 
" Plugin 'dracula/vim' 
" Plugin 'joshdick/onedark.vim' 
" Plugin 'zefei/cake16' 

call vundle#end()            " required
filetype plugin indent on    " required

colorscheme gruvbox
set background=dark
let g:gruvbox_contrast_dark = 'soft'
let g:gruvbox_material_background= 'soft'
let g:gruvbox_italic=1

let g:gruvbox_material_enable_italic = 1

if (has("termguicolors"))
  set termguicolors
endif

set termguicolors
let g:dracula_colorterm = 0

set cursorline
hi CursorLine   cterm=NONE ctermbg=darkred ctermfg=white
set cursorcolumn

set ignorecase " Search case insensitive:
set smartcase " .. but not when search pattern contains upper case characters
set mouse=a " Copy selected text with mouse to system clipboard
set updatetime=250 " If this many milliseconds nothing is typed the swap file will be written to disk
set lazyredraw " buffers screen updates instead of updating all the time
set linebreak " breaks lines by word rather than character
set timeoutlen=500
let g:vim_json_conceal=0
set conceallevel=0
set clipboard+=unnamedplus

" Buffers
set hidden

" Usable 'Tab'
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set infercase
set linespace=8

set showtabline=0

set laststatus=2
set encoding=UTF-8

" Persistent undo
set undofile
set undodir=$HOME/Dropbox/.vim/undo

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
nnoremap ; :
" let mapleader = \<Space>"

nnoremap <C-z> <nop>

map j gj
map k gk

" move between tabs
nnoremap <C-Down> :tabprevious<CR>
nnoremap <C-Up> :tabnext<CR>

" move between buffers
map <C-Left> <Esc>:bprev<CR>
map <C-Right> <Esc>:bnext<CR>

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

map <leader><up> <C-W>k
map <leader><down> <C-W>j
map <leader><left> <C-W>h
map <leader><right> <C-W>l

map <F3> :Ranger<CR>

nnoremap <F4> :Nuake<CR>
inoremap <F4> <C-\><C-n>:Nuake<CR>
tnoremap <F4> <C-\><C-n>:Nuake<CR>

"map <Leader>y "+y
"map <Leader>p "+p

vnoremap y "+y
vnoremap p "+p

" for the autocomplete suggest menu
inoremap <expr> <CR> pumvisible() ? "\<C-y>" : "\<CR>"
inoremap <expr> <TAB> pumvisible() ? "\<C-y>" : "\<CR>"

" disable arrow keys in normal mode and visual mode
" noremap <Up> <Nop>
" noremap <Down> <Nop>
" noremap <Left> <Nop>
" noremap <Right> <Nop>

nmap oo o<Esc>

" *** END OF KEYMAPS ***


"highlight BadWhitespace ctermbg=red guibg=red
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

highlight BadWhitespace ctermbg=red guibg=red

let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>


" Airline
let g:airline_theme='gruvbox'
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

"autocmd BufWinLeave *.* mkview
"autocmd BufWinEnter *.* silent loadview

" NERDTree settings
let g:NERDTreeLimitedSyntax = 1
let g:NERDTreeSyntaxDisableDefaultExtensions = 1
let g:NERDTreeDisableExactMatchHighlight = 1
let g:NERDTreeDisablePatternMatchHighlight = 1
let g:NERDTreeHighlightCursorline = 0
let g:NERDTreeWinSize=40
let g:indentLine_fileTypeExclude = ["nerdtree"]

let g:WebDevIconsUnicodeDecorateFolderNodes = v:true
let g:WebDevIconsNerdTreeBeforeGlyphPadding = ""
let g:webdevicons_enable_startify = 1

autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif " autoquit if only nerdtree is open
autocmd bufenter * if &filetype == "nerdtree" | silent exe substitute(mapcheck("R"), "<CR>", "", "") | endif

let g:ranger_command_override = 'ranger --cmd "set show_hidden=true"'

let g:rainbow_active = 1 "Color brackets

" autoformat settings
noremap <F5> :Autoformat<CR>
" au BufWrite * :Autoformat
let g:autoformat_autoindent = 0
let g:autoformat_retab = 0
let g:autoformat_remove_trailing_spaces = 0

" Startify settings
let g:startify_files_number = 25
let g:startify_lists = [
            \ { 'type': 'files',     'header': ['   MRU']            },
            \ { 'type': 'bookmarks', 'header': ['   Bookmarks']      },
            \ ]
let g:startify_bookmarks = [
            \ '~/.zshrc',
            \ '~/.config/compton.conf',
            \ '~/.config/nvim/init.vim',
            \ '~/.config/termite/config'
            \ ]
let g:startify_custom_header = 0

" IndentLine settings
let g:indentLine_char = '│'
let g:indentLine_enabled = 0
let g:indentLine_leadingSpaceEnabled = 1
let g:indentLine_leadingSpaceChar = "."

" Git settings (fugitive and gitguter)
set updatetime=100

" PYTHON settings
syntax on

let g:python_highlight_all=1

let g:syntastic_python_checkers=['flake8']

" Python indentations
au BufNewFile,BufRead *.py
            \ set tabstop=4 |
            \ set softtabstop=4 |
            \ set shiftwidth=4 |
            \ set textwidth=79 |
            \ set wrapmargin=0 |
            \ set formatoptions+=t |
            \ set expandtab |
            \ set autoindent |
            \ set fileformat=unix

" ncm2 settings
" autocmd BufEnter * call ncm2#enable_for_buffer()
" set completeopt=menuone,noselect,noinsert
" set shortmess+=c

" make it fast
" let ncm2#popup_delay = 5
" let ncm2#complete_length = [[1, 1]]
" " Use new fuzzy based matches
" let g:ncm2#matcher = 'substrfuzzy'

let g:jedi#auto_initialization = 1
let g:jedi#completions_enabled = 0
let g:jedi#auto_vim_configuration = 0
let g:jedi#smart_auto_mappings = 0
let g:jedi#popup_on_dot = 0
let g:jedi#completions_command = ""
let g:jedi#show_call_signatures = "1"

" inoremap <silent> <expr> <CR> ncm2_neosnippet#expand_or("\<CR>", 'n')
" inoremap <silent> <expr> <TAB> ncm2_neosnippet#expand_or("<TAB>", 'n')

"" Plugin key-mappings.
"" Note: It must be "imap" and "smap".  It uses <Plug> mappings.
"imap <C-k>     <Plug>(neosnippet_expand_or_jump)
"smap <C-k>     <Plug>(neosnippet_expand_or_jump)
"xmap <C-k>     <Plug>(neosnippet_expand_target)

"" SuperTab like snippets behavior.
"" Note: It must be "imap" and "smap".  It uses <Plug> mappings.
""imap <expr><TAB>
"" \ pumvisible() ? "\<C-n>" :
"" \ neosnippet#expandable_or_jumpable() ?
"" \    "\<Plug>(neosnippet_expand_or_jump)" : "\<TAB>"
"" smap <expr><TAB> neosnippet#expandable_or_jumpable() ?
"" \ "\<Plug>(neosnippet_expand_or_jump)" : "\<TAB>"

" For conceal markers.
if has('conceal')
  set conceallevel=2 concealcursor=niv
endif
