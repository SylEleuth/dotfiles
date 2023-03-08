-----------------------------------------------------------
-- General Neovim settings and configuration
-----------------------------------------------------------

local g = vim.g       -- Global variables
local opt = vim.opt   -- Set options (global/buffer/windows-scoped)
local cmd = vim.cmd   -- For vimscript options

-----------------------------------------------------------
-- General
-----------------------------------------------------------
opt.mouse = 'a'                       -- Enable mouse support
opt.clipboard = 'unnamedplus'         -- Copy/paste to system clipboard
opt.swapfile = false                  -- Don't use swapfile
opt.completeopt = 'menuone,noinsert,noselect'  -- Autocomplete options

-----------------------------------------------------------
-- Neovim UI
-----------------------------------------------------------
opt.number = true           -- Show line number
opt.showmatch = true        -- Highlight matching parenthesis
opt.splitright = true       -- Vertical split to the right
opt.splitbelow = true       -- Horizontal split to the bottom
opt.ignorecase = true       -- Ignore case letters when search
opt.smartcase = true        -- Ignore lowercase for the whole pattern
opt.linebreak = true        -- Wrap on word boundary
opt.termguicolors = true    -- Enable 24-bit RGB colors
opt.laststatus = 2          -- Set global statusline
opt.cursorline = true
opt.cursorcolumn = true
opt.wrap = false            -- display lines as one long line
opt.sidescrolloff = 8
opt.scrolloff = 1
opt.shada = "!,'300,<50,s10,h"

-----------------------------------------------------------
-- Tabs, indent
-----------------------------------------------------------
opt.expandtab = true        -- Use spaces instead of tabs
opt.shiftwidth = 4          -- Shift 4 spaces when tab
opt.tabstop = 4             -- 1 tab == 4 spaces
opt.smartindent = true      -- Autoindent new lines

-----------------------------------------------------------
-- Memory, CPU
-----------------------------------------------------------
opt.hidden = true           -- Enable background buffers
opt.history = 100           -- Remember N lines in history
opt.lazyredraw = false      -- Faster scrolling
opt.synmaxcol = 240         -- Max column for syntax highlight
opt.updatetime = 250        -- ms to wait for trigger an event

opt.undolevels = 1000
opt.undofile = true
opt.undodir = vim.fn.expand('$HOME/Dropbox/vimundo')

-----------------------------------------------------------
-- Custom
-----------------------------------------------------------

vim.cmd [[

  " Vista
  let g:vista_sidebar_width = 40
  let g:vista#renderer#enable_icon = 1
  let g:vista#renderer#enable_kind = 1
  let g:vista#renderer#icons = {
  \   "function": "\uf794 ",
  \   "variable": "\uf71b ",
  \  }
  let g:vista_icon_indent = ["╰─ ", "├─ "]
  let g:vista#renderer#ctags = 'kind'
  let g:vista_default_executive = 'ctags'
  let g:vista_close_on_jump = 0

  highlight VistaParenthesis guifg=#d3869b
  highlight VistaScope guifg=#b16286
  highlight VistaTag guifg=#83a598
  " highlight VistaKind guifg=#cc241d
  " highlight VistaScopeKind guifg=#cc241d
  highlight VistaLineNr guifg=#928374
  highlight VistaColon guifg=#d5c4a1
  highlight VistaIcon guifg=#fabd2f
  " highlight VistaArgs guifg=#cc241d

  " Kitty navigator
  let g:kitty_navigator_no_mappings = 1

]]


-----------------------------------------------------------
-- Startup
-----------------------------------------------------------
-- Disable nvim intro
opt.shortmess:append "sI"

-- -- Disable builtin plugins
local disabled_built_ins = {
   "2html_plugin",
   "getscript",
   "getscriptPlugin",
   "gzip",
   "logipat",
   "netrw",
   "netrwPlugin",
   "netrwSettings",
   "netrwFileHandlers",
   "matchit",
   "tar",
   "tarPlugin",
   "rrhelper",
   "spellfile_plugin",
   "vimball",
   "vimballPlugin",
   "zip",
   "zipPlugin",
   "tutor",
   "rplugin",
   "synmenu",
   "optwin",
   "compiler",
   "bugreport",
   "ftplugin",
}

for _, plugin in pairs(disabled_built_ins) do
   g["loaded_" .. plugin] = 1
end
