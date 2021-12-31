set nocompatible
filetype plugin on
syntax on

call plug#begin()

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'honza/vim-snippets'
Plug 'neovim/nvim-lsp' " nvim-lsp
Plug 'jackguo380/vim-lsp-cxx-highlight'

Plug 'tpope/vim-commentary' " Comment with 'gcc'

Plug 'easymotion/vim-easymotion'

Plug 'mbbill/undotree' " Undo history visualizer (F6)

Plug 'tpope/vim-surround' " Surround words and phrases with parentheses, brackets, quotes, XML tags, and more
" Plug 'jiangmiao/auto-pairs' " Insert or delete brackets, parens, quotes in pair
Plug 'raimondi/delimitmate' " Insert or delete brackets, parens, quotes in pair
Plug 'lukas-reineke/indent-blankline.nvim' " Disply the indention levels with thin vertical lines and leading spaces
" Plug 'yamatsum/nvim-cursorline' " Highlight words and lines on the cursor for Neovim
Plug 'norcalli/nvim-colorizer.lua' " Color highlighter
Plug 'preservim/tagbar' " Displays tags in a window, ordered by scope
Plug 'jeetsukumaran/vim-buffergator' " List, select and switch between buffers
Plug 'famiu/bufdelete.nvim' " Deleting a buffer in Vim without closing the window
Plug 'moll/vim-bbye' " Delete buffers and close files in Vim without closing your windows
Plug 'godlygeek/tabular' " Vim script for text filtering and alignment 
Plug 'luochen1990/rainbow' " Colored parentheses
Plug 'terryma/vim-multiple-cursors' " Multiple selection <C-n>
Plug 'pbrisbin/vim-mkdir' " Automatically create any non-existent directories before writing the buffer

Plug 'ryanoasis/vim-devicons'
Plug 'kyazdani42/nvim-web-devicons'

Plug 'vim-airline/vim-airline' " Cool powerline bars
Plug 'vim-airline/vim-airline-themes'
" Plug 'glepnir/galaxyline.nvim' , {'branch': 'main'}

Plug 'vifm/vifm.vim'
Plug 'kevinhwang91/rnvimr' " Ranger in floating window

Plug 'mhinz/vim-startify' " Starting screen

Plug 'Lenovsky/nuake' " A Quake-style terminal panel for Neovim and Vim <F4>

Plug 'nvie/vim-flake8' " Python linter <F7>
Plug 'davidhalter/jedi-vim' " jedi for python

Plug 'Chiel92/vim-autoformat' " Code formatting <F5>

Plug 'kh3phr3n/python-syntax' " Python code highlight
Plug 'numirias/semshi', { 'do': ':UpdateRemotePlugins' }

Plug 'kshenoy/vim-signature' " place, toggle and display marks

Plug 'tpope/vim-fugitive' " Git wrapper
Plug 'rbong/vim-flog' " Git branch viewer
Plug 'airblade/vim-gitgutter' " Shows git diff
Plug 'ruanyl/vim-gh-line' " Opens a link to the current line on GitHub

Plug 'psliwka/vim-smoothie'

Plug 'junegunn/fzf' " Fuzzy finder
Plug 'junegunn/fzf.vim'

Plug 'vimwiki/vimwiki'
Plug 'plasticboy/vim-markdown'

Plug 'pechorin/any-jump.vim' " Jump to any definition and references (leader-j)

" Plug 'vim-syntastic/syntastic' " Syntax checking
" Plug 'roxma/nvim-yarp' " Remote updates of plugins

Plug 'sainnhe/gruvbox-material'
" Plug 'morhetz/gruvbox'
" Plug 'dracula/vim'
" Plug 'drewtempelmeyer/palenight.vim' " similar to dracula

call plug#end()

" ###### COLOR SCHEMES
if has ('termguicolors')
    set termguicolors
endif

set t_Co=256

let g:gruvbox_material_background = 'medium'
set background=dark
let g:gruvbox_contrast_dark = 'soft'
let g:gruvbox_italic=1

let g:gruvbox_material_enable_italic = 1
let g:gruvbox_material_enable_bold = 1
let g:gruvbox_material_diagnostic_text_highlight = 1
let g:gruvbox_material_diagnostic_line_highlight = 1
let g:gruvbox_material_diagnostic_virtual_text = 'colored'
let g:gruvbox_material_current_word = 'bold'

colorscheme gruvbox-material

if &diff
    colorscheme gruvbox-material
endif

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
set clipboard+=unnamedplus

" Buffers
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
" set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("nvim-0.5.0") || has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

" COC config

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction
" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()
" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
" position. Coc only does snippet and additional edit on confirm.
if exists('*complete_info')
  inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
else
  imap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current buffer.
nmap <leader>ac  <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf  <Plug>(coc-fix-current)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server.
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Use <TAB> for selections ranges.
" NOTE: Requires 'textDocument/selectionRange' support from the language server.
" coc-tsserver, coc-python are the examples of servers that support it.
nmap <silent> <TAB> <Plug>(coc-range-select)
xmap <silent> <TAB> <Plug>(coc-range-select)

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of language server.
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocActionAsync('runCommand', 'editor.action.organizeImport')

" Use <C-l> for trigger snippet expand.
imap <C-l> <Plug>(coc-snippets-expand)

" Use <C-h> for select text for visual placeholder of snippet.
vmap <C-j> <Plug>(coc-snippets-select)

" Use <C-h> for jump to next placeholder, it's default of coc.nvim
let g:coc_snippet_next = '<c-l>'

" Use <C-l> for jump to previous placeholder, it's default of coc.nvim
let g:coc_snippet_prev = '<c-h>'

" Use <C-h> for both expand and jump (make expand higher priority.)
imap <C-h> <Plug>(coc-snippets-expand-jump)

" Use <leader>x for convert visual selected code to snippet
xmap <leader>x  <Plug>(coc-convert-snippet)

let g:lsp_cxx_hl_use_text_props = 1

" END of COC config

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

set nofoldenable    " disable folding

" Persistent undo
set undofile
set undodir=$HOME/Dropbox/vimundo

set undolevels=1000
set undoreload=10000

autocmd VimResized * wincmd =

augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set number norelativenumber
augroup END

" *** KEYMAPS ***
nnoremap <Space> :
nnoremap ; :
" let mapleader = "\<Space>"
" let g:maplocalleader = ','
" nnoremap <Space> <Nop>

nmap oo o<Esc>

map j gj
map k gk

nnoremap <C-Left> <C-W>h
nnoremap <C-Down> <C-W>j
nnoremap <C-Up> <C-W>k
nnoremap <C-Right> <C-W>l

" map <F1> :NERDTreeToggle<CR>
" map <F2> :NERDTreeFind<CR>
map <F2> :Vifm<CR>

nnoremap <C-z> <nop>

" move between tabs
" nnoremap <C-Down> :tabprevious<CR>
" nnoremap <C-Up> :tabnext<CR>

" move between buffers
map <S-Right> <Esc>:bnext<CR>
map <S-Left> <Esc>:bprevious<CR>

" nnoremap <leader>l :ls<CR>:b<space>

" switch to left / right split (mostly for Nerd Tree)
" map <C-h> <C-W>h
" map <C-l> <C-W>l

" map <leader><up> <C-W>k
" map <leader><down> <C-W>j
" map <leader><left> <C-W>h
" map <leader><right> <C-W>l

nnoremap <F4> :Nuake<CR>
inoremap <F4> <C-\><C-n>:Nuake<CR>
tnoremap <F4> <C-\><C-n>:Nuake<CR>

nmap <F8> :TagbarToggle<CR>

"map <Leader>y "+y
"map <Leader>p "+p

vnoremap y "+y
vnoremap p "+p

" move lines up and down
nnoremap <C-j> :m .+1<CR>==
nnoremap <C-k> :m .-2<CR>==
inoremap <C-j> <Esc>:m .+1<CR>==gi
inoremap <C-k> <Esc>:m .-2<CR>==gi
vnoremap <C-j> :m '>+1<CR>gv=gv
vnoremap <C-k> :m '<-2<CR>gv=gv

" for the autocomplete suggest menu
inoremap <expr> <CR> pumvisible() ? "\<C-y>" : "\<CR>"
inoremap <expr> <TAB> pumvisible() ? "\<C-y>" : "\<CR>"

" disable arrow keys in normal mode and visual mode
" noremap <Up> <Nop>
" noremap <Down> <Nop>
" noremap <Left> <Nop>
" noremap <Right> <Nop>

" TAB in general mode will move to text buffer
nnoremap <silent> <TAB> :bnext<CR>
" SHIFT-TAB will go back
nnoremap <silent> <S-TAB> :bprevious<CR>

nmap <silent> <leader>] $
nmap <silent> <leader>[ 0

nmap <silent> <leader>' :Startify<CR>

nmap <leader>e <Cmd>CocCommand explorer<CR>
nmap <F1> <Cmd>CocCommand explorer<CR>

:nnoremap <Leader>q :Bdelete<CR>

nnoremap <F6> :UndotreeToggle<CR>

vmap <leader>r :Tabularize spaces<CR>

" *** END OF KEYMAPS ***

" Open config file
nmap <silent> <leader>V :so $MYVIMRC<CR>
nmap <silent> <leader>v :call EditConfig()<CR>

function! EditConfig()
    for config in ['$MYGVIMRC', '$MYVIMRC']
        if exists(config)
            execute 'edit '.config
        endif
    endfor
endfunction

" Rnvimr
map <F3> :RnvimrToggle<CR>

let g:rnvimr_draw_border = 1

" Make Ranger to be hidden after picking a file
let g:rnvimr_pick_enable = 1

" Make Neovim to wipe the buffers corresponding to the files deleted by Ranger
let g:rnvimr_bw_enable = 1

" Make Neovim wipe the buffers corresponding to the files deleted by Ranger
let g:rnvimr_enable_bw = 1

let g:rnvimr_ranger_cmd = 'ranger --cmd="set column_ratios 1,1"'
            " \ --cmd="set draw_borders separators"'

let g:rnvimr_presets = [
            \ {'width': 0.900, 'height': 0.900}]

"highlight BadWhitespace ctermbg=red guibg=red
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

highlight BadWhitespace ctermbg=red guibg=red

" easymotion
let g:EasyMotion_smartcase = 1
let g:EasyMotion_verbose = 0
let g:EasyMotion_do_shade = 0
let g:EasyMotion_prompt = ' => '

" s{char}{char} to move to {char}{char}
nmap s <Plug>(easymotion-overwin-f2)

" Move to line
map <Leader>l <Plug>(easymotion-bd-jk)
nmap <Leader>l <Plug>(easymotion-overwin-line)

" <Leader>f{char} to move to {char}
map  <Leader>f <Plug>(easymotion-bd-f)
nmap <Leader>f <Plug>(easymotion-overwin-f)

" Move to word
map  <Leader>w <Plug>(easymotion-bd-w)
nmap <Leader>w <Plug>(easymotion-overwin-w)

" Airline
let g:airline_theme='gruvbox_material'
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

" save folds and such when close file
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent! loadview

" Tagbar
let g:tagbar_width = max([40, winwidth(0) / 5])
let g:tagbar_autofocus = 1
let g:rainbow_active = 1 "Color brackets

" autoformat settings
noremap <F5> :Autoformat<CR>
" au BufWrite * :Autoformat
let g:autoformat_autoindent = 1
let g:autoformat_retab = 0
let g:autoformat_remove_trailing_spaces = 0

" Startify settings
function! StartifyEntryFormat()
        return 'WebDevIconsGetFileTypeSymbol(absolute_path) ." ". entry_path'
endfunction

let g:startify_files_number = 20
let g:startify_session_autoload = 1
let g:startify_session_delete_buffers = 1
let g:startify_change_to_vcs_root = 1
let g:startify_fortune_use_unicode = 1
let g:startify_session_persistence = 1

let g:startify_session_dir = '~/.config/nvim/session'

let g:startify_lists = [
          \ { 'type': 'files',     'header': ['   Files']                        },
          \ { 'type': 'dir',       'header': ['   Current Directory '. getcwd()] },
          \ { 'type': 'sessions',  'header': ['   Sessions']                     },
          \ { 'type': 'bookmarks', 'header': ['   Bookmarks']                    },
          \ ]

let g:startify_lists = [
            \ { 'type': 'files',     'header': ['   MRU']            },
            \ { 'type': 'bookmarks', 'header': ['   Bookmarks']      },
            \ ]

let g:startify_bookmarks = [
            \ '~/.config/nvim/init.vim',
            \ '~/.zshrc',
            \ '~/.p10k.zsh',
            \ '~/.config/kitty/kitty.conf'
            \ ]

let g:startify_custom_header = 0
" let g:startify_enable_special = 0

" IndentLine settings
let g:indentLine_char = '│'
let g:indentLine_enabled = 1
let g:indentLine_leadingSpaceChar = "."
let g:indentLine_leadingSpaceEnabled = 1

" PYTHON settings
syntax on

let g:python_highlight_all = 1

" let g:syntastic_python_checkers=['flake8']

" Python indentations
au BufNewFile,BufRead *.py
            \ set tabstop=4 |
            \ set softtabstop=4 |
            \ set shiftwidth=4 |
            \ set textwidth=79 |
            \ set wrapmargin=0 |
            \ set formatoptions+=t |
            \ set expandtab |
            " \ set autoindent |
            \ set fileformat=unix |
            \ set foldmethod=indent |
            \ set foldnestmax=10 |
            \ set nofoldenable |
            \ set foldlevel=2 |

let g:jedi#auto_initialization = 1
let g:jedi#completions_enabled = 0
let g:jedi#auto_vim_configuration = 0
let g:jedi#smart_auto_mappings = 0
let g:jedi#popup_on_dot = 0
let g:jedi#completions_command = ""
let g:jedi#show_call_signatures = "1"

" VimWiki
autocmd FileType vimwiki set ft=markdown
let g:vimwiki_list = [{'path': '~/Dropbox/vimwiki/',
                     \ 'syntax': 'markdown', 'ext': '.md'}]
let g:vimwiki_global_ext = 0
let g:vimwiki_folding = ''

lua << EOF
require'colorizer'.setup()

-- Indent blankline
vim.opt.list = true
--vim.opt.listchars:append("space:⋅")
--vim.opt.listchars:append("eol:↴")
vim.opt.termguicolors = true
vim.cmd [[highlight IndentBlanklineIndent1 guifg=#D65D0E gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent2 guifg=#FABD2F gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent3 guifg=#8EC07C gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent4 guifg=#83A598 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent5 guifg=#458588 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent6 guifg=#B16286 gui=nocombine]]

require("indent_blankline").setup {
    show_end_of_line = true,
    space_char_blankline = " ",
    show_current_context_start = true,
    char_highlight_list = {
        "IndentBlanklineIndent1",
        "IndentBlanklineIndent2",
        "IndentBlanklineIndent3",
        "IndentBlanklineIndent4",
        "IndentBlanklineIndent5",
        "IndentBlanklineIndent6",
    },
}
EOF
