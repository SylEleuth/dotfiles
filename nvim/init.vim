set nocompatible
filetype plugin on
syntax on

call plug#begin()

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'honza/vim-snippets' " no Ultisnips required, coc-snippets is the engine
Plug 'bfrg/vim-cpp-modern'

Plug 'phaazon/hop.nvim'

Plug 'mbbill/undotree' " Undo history visualizer (F6)
Plug 'tpope/vim-commentary' " Comment with 'gcc'
Plug 'tpope/vim-surround' " Surround words and phrases with parentheses, brackets, quotes, XML tags, and more
Plug 'raimondi/delimitmate' " Automatic closing of quotes, parenthesis, brackets, etc.
Plug 'lukas-reineke/indent-blankline.nvim' " Disply the indention levels with thin vertical lines and leading spaces
Plug 'norcalli/nvim-colorizer.lua' " Color highlighter
Plug 'famiu/bufdelete.nvim' " Deleting a buffer in Vim without closing the window
Plug 'moll/vim-bbye' " Delete buffers and close files in Vim without closing your windows
Plug 'godlygeek/tabular' " Vim script for text filtering and alignment 
Plug 'ervandew/supertab'
Plug 'luochen1990/rainbow' " Colored parentheses
Plug 'terryma/vim-multiple-cursors' " Multiple selection <C-n>
Plug 'pbrisbin/vim-mkdir' " Automatically create any non-existent directories before writing the buffer
Plug 'RRethy/vim-illuminate' " Automatically highlighting other uses of the word under the cursor
Plug 'psliwka/vim-smoothie'
Plug 'lambdalisue/suda.vim'
Plug 'nacro90/numb.nvim' " Peek lines just when you intend
Plug 'rcarriga/nvim-notify'

Plug 'sudormrfbin/cheatsheet.nvim' " A searchable cheatsheet for neovim from within the editor (requirements below)
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'AckslD/nvim-neoclip.lua'
Plug 'tami5/sqlite.lua'
Plug 'liuchengxu/vista.vim'

Plug 'sidebar-nvim/sidebar.nvim'

Plug 'ryanoasis/vim-devicons'
Plug 'kyazdani42/nvim-web-devicons'

Plug 'vim-airline/vim-airline' " Cool powerline bars
Plug 'vim-airline/vim-airline-themes'

Plug 'vifm/vifm.vim'

Plug 'mhinz/vim-startify' " Starting screen

Plug 'vim-python/python-syntax'

let g:python3_host_prog = $HOME . '/.local/venv/nvim/bin/python'
Plug 'averms/black-nvim', {'do': ':UpdateRemotePlugins'}
Plug 'fisadev/vim-isort'

Plug 'peterhoeg/vim-qml'

Plug 'tpope/vim-fugitive' " Git wrapper
Plug 'rbong/vim-flog' " Git branch viewer
Plug 'airblade/vim-gitgutter' " Shows git diff
Plug 'tveskag/nvim-blame-line'
Plug 'kdheepak/lazygit.nvim'

Plug 'vimwiki/vimwiki'
Plug 'plasticboy/vim-markdown'

Plug 'rhysd/devdocs.vim'

Plug 'pechorin/any-jump.vim' " Jump to any definition and references (leader-j)

Plug 'kevinhwang91/nvim-hlslens'

Plug 'gruvbox-community/gruvbox'
" Plug 'dracula/vim'
" Plug 'drewtempelmeyer/palenight.vim' " similar to dracula

call plug#end()

" ###### COLOR SCHEMES
if has ('termguicolors')
    set termguicolors
endif

set t_Co=256

let g:gruvbox_italic             = 1
let g:gruvbox_bold               = 1
let g:gruvbox_italicize_comments = 1
let g:gruvbox_italicize_strings  = 1
let g:gruvbox_contrast_dark      = 'medium'
let g:gruvbox_contrast_light     = 'medium'

if &diff
    colorscheme gruvbox
else
    colorscheme gruvbox
endif

set cursorline
hi  CursorLine   ctermbg=236 ctermfg=0 guibg=#32302f
set cursorcolumn

set ignorecase " Search case insensitive:
set smartcase " .. but not when search pattern contains upper case characters
set mouse=a " Copy selected text with mouse to system clipboard
set updatetime=250 " If this many milliseconds nothing is typed the swap file will be written to disk
set lazyredraw " buffers screen updates instead of updating all the time
set linebreak " breaks lines by word rather than character
set timeoutlen=500
let g:vim_json_conceal=0
set clipboard=unnamedplus
set hidden " Buffers
set nobackup
set nowritebackup
set updatetime=300
set shortmess+=c
set signcolumn=auto

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

" set nofoldenable    " disable folding

" Persistent undo
set undofile
set undodir=$HOME/Dropbox/vimundo

set undolevels=1000
set undoreload=10000

" COC config

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" NOTE: There's always complete item selected by default, you may want to enable
" no select by `"suggest.noselect": true` in your configuration file.
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1):
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

" Make <CR> to accept selected completion item or notify coc.nvim to format
" <C-g>u breaks current undo, please make your own choice.
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

hi CocSearch ctermfg=0 guifg=#d65d0e
hi CocMenuSel ctermbg=0 guibg=#fe8019
hi CocFloating guibg=#32302f

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

function! ShowDocumentation()
  if CocAction('hasProvider', 'hover')
    call CocActionAsync('doHover')
  else
    call feedkeys('K', 'in')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
" autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>fs <Plug>(coc-format-selected)
nmap <leader>fs <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json,python setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a <Plug>(coc-codeaction-selected)
nmap <leader>a <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current buffer.
nmap <leader>ac <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf <Plug>(coc-fix-current)

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

" Remap <C-f> and <C-b> for scroll float windows/popups.
if has('nvim-0.4.0') || has('patch-8.2.0750')
  nnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  nnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
  inoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
  inoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"
  vnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  vnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
endif

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of language server.
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call CocActionAsync('runCommand', 'editor.action.organizeImport')

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

" END of COC config

autocmd VimResized * wincmd =

" Overwrite illuminate background color
autocmd VimEnter * hi illuminatedWord guibg=#3c3836
let g:Illuminate_highlightUnderCursor = 0

augroup numbertoggle
    autocmd!
    autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
    autocmd BufLeave,FocusLost,InsertEnter   * set number norelativenumber
augroup END

" *** KEYMAPS ***
nnoremap ; :

nmap oo o<Esc>
nmap Oo O<Esc>

map j gj
map k gk

nnoremap <C-Left>  <C-W>h
nnoremap <C-Down>  <C-W>j
nnoremap <C-Up>    <C-W>k
nnoremap <C-Right> <C-W>l

map <F2> :Vifm<CR>

nnoremap <C-z> <nop>

" move between buffers
map <S-Right> <Esc>:bnext<CR>
map <S-Left>  <Esc>:bprevious<CR>

nmap <silent> <F3> :Vista!!<CR>
nmap <silent> <leader>g :Vista finder coc<CR>

vnoremap y "+y
" vnoremap p "+p
" Don't put pasted-over content into the clipboard.
vnoremap p "_c<C-r><C-o>+<Esc>

" move lines up and down
nnoremap <C-j> :m      .+1<CR>==
nnoremap <C-k> :m      .-2<CR>==
inoremap <C-j> <Esc>:m .+1<CR>==gi
inoremap <C-k> <Esc>:m .-2<CR>==gi
vnoremap <C-j> :m      '>+1<CR>gv=gv
vnoremap <C-k> :m      '<-2<CR>gv=gv

" TAB in general mode will move to text buffer
nnoremap <silent> <TAB> :bnext<CR>
" SHIFT-TAB will go back
nnoremap <silent> <S-TAB> :bprevious<CR>

nmap <silent> <leader>] $
nmap <silent> <leader>[ 0

nmap <silent> <leader>' :Startify<CR>

" nmap <leader>e <Cmd>CocCommand explorer<CR>
nmap <F1> <Cmd>CocCommand explorer<CR>

nnoremap <Leader>q :Bdelete<CR>

nnoremap <F5> :UndotreeToggle<CR>

vmap <leader>rr :Tabularize spaces<CR>
nmap <Leader>r= :Tabularize /=<CR>
vmap <Leader>r= :Tabularize /=<CR>
nmap <Leader>r: :Tabularize /:\zs<CR>
vmap <Leader>r: :Tabularize /:\zs<CR>
nmap <Leader>r- :Tabularize /-\zs<CR>
vmap <Leader>r- :Tabularize /-\zs<CR>

nnoremap <leader>h :History<CR>

nnoremap <silent> <leader>cc :ToggleBlameLine<CR>
" Show blame info below the statusline instead of using virtual text
" let g:blameLineUseVirtualText = 0

nnoremap <silent> <leader>gg :LazyGit<CR>

" Find files using Telescope command-line sugar.
nnoremap <leader>e  <cmd>Telescope find_files<cr>
nnoremap <leader>er <cmd>Telescope live_grep<cr>
nnoremap <leader>b <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" Open, reload config
nmap <silent> <leader>v :call EditConfig()<CR>
nmap <silent> <leader>V :so $MYVIMRC<CR>

noremap <silent> n <Cmd>execute('normal! ' . v:count1 . 'n')<CR>
            \<Cmd>lua require('hlslens').start()<CR>
noremap <silent> N <Cmd>execute('normal! ' . v:count1 . 'N')<CR>
            \<Cmd>lua require('hlslens').start()<CR>

nnoremap <F4> :SidebarNvimToggle<CR>

nmap <leader>d <Plug>(devdocs-under-cursor)

nnoremap <silent> <leader>y  :<C-u>CocList -A --normal yank<cr>

" *** END OF KEYMAPS ***

" Open config file
function! EditConfig()
    for config in ['$MYGVIMRC', '$MYVIMRC']
        if exists(config)
            execute 'edit '.config
        endif
    endfor
endfunction

" Lazygit settings
let g:lazygit_floating_window_winblend = 0 " transparency of floating window
let g:lazygit_floating_window_scaling_factor = 0.9 " scaling factor for floating window
let g:lazygit_floating_window_corner_chars = ['', '', '', ''] " customize lazygit popup window corner characters
let g:lazygit_floating_window_use_plenary = 0 " use plenary.nvim to manage floating window if available
let g:lazygit_use_neovim_remote = 0 " fallback to 0 if neovim-remote is not installed

"highlight BadWhitespace ctermbg=red guibg=red
" au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" Airline
let  g:airline_theme                               = 'gruvbox'
let  g:airline#extensions#tabline#enabled          = 1
let  g:airline#extensions#tabline#formatter        = 'unique_tail'
let  g:airline_powerline_fonts                     = 1
"let g:airline#extensions#tabline#fnamemod         = ':p:.'
let  g:airline#extensions#tabline#buffer_nr_show   = 0
let  g:airline#extensions#whitespace#enabled       = 0
let  g:airline#extensions#tabline#buffer_min_count = 1
"let g:airline#extensions#tabline#fnamecollapse    = 1

" save folds and such when close file
augroup remember_folds
  autocmd!
  autocmd BufWinLeave *.* mkview
  autocmd BufWinEnter *.* silent! loadview
augroup END

let g:rainbow_active = 1 "Color brackets

" Startify settings
function! StartifyEntryFormat()
        return 'WebDevIconsGetFileTypeSymbol(absolute_path) ." ". entry_path'
endfunction

let g:startify_files_number           = 20
let g:startify_session_autoload       = 0
let g:startify_session_persistence    = 1
let g:startify_session_delete_buffers = 1
let g:startify_change_to_vcs_root     = 1
let g:startify_fortune_use_unicode    = 1

let g:startify_session_dir = '~/Dropbox/vimsession'

let g:startify_lists = [
                \ { 'type': 'files',     'header': ['   Files']                        },
                \ { 'type': 'bookmarks', 'header': ['   Bookmarks']                    },
                \ { 'type': 'dir',       'header': ['   Current Directory '. getcwd()] },
                \ { 'type': 'sessions',  'header': ['   Sessions']                     },
                \ ]

let g:startify_bookmarks = [
                \ '~/.config/nvim/init.vim',
                \ '~/.zshrc',
                \ '~/.p10k.zsh',
                \ '~/.config/kitty/kitty.conf'
                \ ]


let g:startify_custom_header = 0
" let g:startify_enable_special = 0

" PYTHON settings
let g:python_host_prog  = '/usr/bin/python'
let g:python3_host_prog = '/usr/bin/python3'

syntax on
let g:python_highlight_all = 1

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

au BufNewFile,BufRead *.cpp
            \ set shiftwidth=4

aug python
    au!
    autocmd BufWritePre *.py Isort
    autocmd BufWritePre *.py Black
aug END

" VimWiki
autocmd FileType vimwiki set ft=markdown
let g:vimwiki_list = [{'path': '~/Dropbox/vimwiki/',
                     \ 'syntax': 'markdown', 'ext': '.md'}]
let g:vimwiki_global_ext = 0
let g:vimwiki_folding = ''

" let g:floaterm_height = 0.8
" let g:floaterm_width = 0.8
" let g:floaterm_title = 0

let g:suda_smart_edit = 1

let g:vista_sidebar_width = 40
let g:vista#renderer#enable_icon = 1
let g:vista#renderer#enable_kind = 1
let g:vista#renderer#icons = {
\   "function": "\uf794",
\   "variable": "\uf71b",
\  }
let g:vista_icon_indent = ["╰─ ", "├─ "]
let g:vista#renderer#ctags = 'kind'
let g:vista_default_executive = 'ctags'
let g:vista_close_on_jump = 1

let g:undotree_SplitWidth = 35

let g:SuperTabDefaultCompletionType = "<Tab>"

" let g:vifm_exec = expand('$HOME/.config/vifm/vifmrun')

lua << EOF

local map = vim.api.nvim_set_keymap

require('colorizer').setup()

require("sidebar-nvim").setup({
    disable_default_keybindings = 0,
    bindings = nil,
    open = false,
    side = "left",
    initial_width = 35,
    hide_statusline = false,
    update_interval = 1000,
    sections = { "buffers", "symbols", "git", "diagnostics" },
    section_separator = {"", "-----", ""},
    containers = {
        attach_shell = "/bin/sh", show_all = true, interval = 5000,
    },
    datetime = { format = "%a %b %d, %H:%M", clocks = { { name = "local" } } },
    todos = { ignored_paths = { "~" } },
    disable_closing_prompt = false,
    buffers = {
        icon = "",
        ignored_buffers = {} -- ignore buffers by regex
    },
    files = {
        icon = "",
        show_hidden = false,
        ignored_paths = {"%.git$"}
    },
    symbols = {
        icon = "ƒ",
    }
})

-- Neoclip config

local function is_whitespace(line)
  return vim.fn.match(line, [[^\s*$]]) ~= -1
end

local function all(tbl, check)
  for _, entry in ipairs(tbl) do
    if not check(entry) then
      return false
    end
  end
  return true
end

require('neoclip').setup({
    history = 1000,
    enable_persistent_history = true,
    db_path = vim.fn.stdpath("data") .. "/databases/neoclip.sqlite3",
    preview = true,
    default_register = '"',
    default_register_macros = 'q',
    enable_macro_history = true,
    content_spec_column = false,
    on_paste = {
      set_reg = false,
    },
    on_replay = {
        set_reg = false,
    },
    filter = function(data)
        return not all(data.event.regcontents, is_whitespace)
    end,
})

-- Line peeker
require('numb').setup{
    show_numbers = true, -- Enable 'number' for the window while peeking
    show_cursorline = true, -- Enable 'cursorline' for the window while peeking
    number_only = false, -- Peek only when the command is only a number instead of when it starts with a number
}

require("notify").setup()
require("telescope").load_extension("notify")

require('telescope').setup {
    defaults = {
        dynamic_preview_title = true,
       }
   }
map('n', '<leader>c', '<cmd>lua require"telescope".extensions.neoclip.default()<cr>',            {noremap=true})

map('n', '<a-n>',     '<cmd>lua require"illuminate".next_reference{wrap=true}<cr>',              {noremap=true})
map('n', '<a-p>',     '<cmd>lua require"illuminate".next_reference{reverse=true,wrap=true}<cr>', {noremap=true})

-- Hop motion
require('hop').setup()
map('n', '<leader>f', "<cmd>lua require'hop'.hint_char1()<cr>", {noremap=true})
map('n', '<leader>s', "<cmd>lua require'hop'.hint_char2()<cr>", {noremap=true})
map('n', '<leader>w', "<cmd>lua require'hop'.hint_words()<cr>", {noremap=true})
map('n', '<leader>l', "<cmd>lua require'hop'.hint_lines()<cr>", {noremap=true})
vim.cmd('highlight HopNextKey guibg=none guifg=#fe8019')
vim.cmd('highlight HopNextKey1 guibg=none guifg=#fe8019')
vim.cmd('highlight HopNextKey2 guibg=none guifg=#fe8019')
vim.cmd('highlight HopUnmatched guibg=none guifg=#504945')

-- Indent blankline
require("indent_blankline").setup {
    show_end_of_line = true,
    space_char_blankline = " ",
    show_current_context_start = true,
    show_first_indent_level = false,
    char_highlight_list = {
        "IndentBlanklineIndent1",
        "IndentBlanklineIndent2",
        "IndentBlanklineIndent3",
        "IndentBlanklineIndent4",
        "IndentBlanklineIndent5",
        "IndentBlanklineIndent6",
        }
    }
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
EOF
