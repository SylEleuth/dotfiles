-----------------------------------------------------------
-- Plugin manager configuration file
-----------------------------------------------------------

-- Automatically install packer

local fn = vim.fn
local install_path = fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'

if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({
    'git',
    'clone',
    '--depth',
    '1',
    'https://github.com/wbthomason/packer.nvim',
    install_path
  })
  vim.o.runtimepath = vim.fn.stdpath('data') .. '/site/pack/*/start/*,' .. vim.o.runtimepath
end

-- Autocommand that reloads neovim whenever you save the packer_init.lua file
vim.cmd [[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost packer_init.lua source <afile> | PackerSync
  augroup end
]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, 'packer')
if not status_ok then
  return
end

-- Packer in flaoting window
packer.init {
  display = {
    open_fn = function()
      return require("packer.util").float { border = "rounded" }
    end,
  },
  git = {
    clone_timeout = 300, -- Timeout, in seconds, for git clones
  },
}

-- Install plugins
return packer.startup(function(use)
  -- Add you plugins here:
  use 'wbthomason/packer.nvim' -- packer can manage itself

  -- Lsp
  use { 'neoclide/coc.nvim', branch = 'release' }

  -- Icons
  use 'nvim-tree/nvim-web-devicons'

  -- Tag viewer
  use 'liuchengxu/vista.vim'
  use 'stevearc/aerial.nvim'

  -- Treesitter interface
  use {
    'nvim-treesitter/nvim-treesitter',
    run = function() require('nvim-treesitter.install').update({ with_sync = true }) end,
  }
  use 'nvim-treesitter/nvim-treesitter-context'
  use 'nvim-treesitter/nvim-treesitter-textobjects'
  use 'HiPhish/rainbow-delimiters.nvim'

  -- Telescope
  use { 'nvim-telescope/telescope.nvim', tag = '0.1.4' }
  use 'nvim-lua/plenary.nvim'
  use 'rcarriga/nvim-notify'
  use 'nvim-telescope/telescope-file-browser.nvim'
  use 'fannheyward/telescope-coc.nvim'
  use 'nvim-lua/popup.nvim'
  use 'natecraddock/telescope-zf-native.nvim'
  use 'debugloop/telescope-undo.nvim'
  use 'smartpde/telescope-recent-files'
  use 'danielfalk/smart-open.nvim'
  use 'nvim-telescope/telescope-ui-select.nvim'
  use 'nvim-telescope/telescope-symbols.nvim'
  use 'nvim-telescope/telescope-media-files.nvim'

  -- Note making
  use 'renerocksai/telekasten.nvim'
  use 'renerocksai/calendar-vim'

  -- Viewing all the URLs in a buffer
  -- use 'axieax/urlview.nvim'

  -- Highlight same-name identifiers with the same color
  use 'David-Kunz/markid'

  -- Diffview
  use 'sindrets/diffview.nvim'

  -- Add/change/delete surrounding delimiter pairs
  use({
    "kylechui/nvim-surround",
    tag = "*", -- Use for stability; omit to use `main` branch for the latest features
    config = function()
      require("nvim-surround").setup({
      })
    end
  })

  -- Yank and clipboard
  use({
    'gbprod/yanky.nvim',
    requires = { 'kkharji/sqlite.lua' }
  })

  -- Smoooth scrolling
  use 'karb94/neoscroll.nvim'

  -- A more adventurous wildmenu
  -- use 'gelguy/wilder.nvim'

  -- Replacement for the UI for messages, cmdline and the popupmenu
  use({
    "folke/noice.nvim",
    "MunifTanjim/nui.nvim",
  })

  -- Comment
  use {
    'numToStr/Comment.nvim',
    config = function()
        require('Comment').setup()
    end
}

  -- Better searching
  use 'kevinhwang91/nvim-hlslens'

  -- Indent guides
  use{ "lukas-reineke/indent-blankline.nvim", main = "ibl", opts = {} }

  -- Delete Neovim buffers without losing window layout
  use 'famiu/bufdelete.nvim'

  -- Keep buffer dimensions in proportion when terminal window is resized
  use 'kwkarlwang/bufresize.nvim'

  -- Window separator
  use 'nvim-zh/colorful-winsep.nvim'

  -- Color schemes
  use "ellisonleao/gruvbox.nvim"
  -- use 'sainnhe/gruvbox-material'
  -- use 'Mofiqul/dracula.nvim'

  -- Statusline
  use 'nvim-lualine/lualine.nvim'

  -- Bufferline
  use 'willothy/nvim-cokeline'

  -- Floating statuslines
  use 'b0o/incline.nvim'

  -- File explorer
  use 'nvim-tree/nvim-tree.lua'

  -- Vifm - file manager
  -- use 'vifm/vifm.vim'

  -- Dashboard (start screen)
  use 'goolord/alpha-nvim'

  -- Center the currently focused buffer to the middle of the screen
  use { "shortcuts/no-neck-pain.nvim", tag = "*" }

  -- Git labels
  use 'lewis6991/gitsigns.nvim'

  -- Vim kitty navigator for seamless navigation between kitty panes and vim splits
  use 'knubie/vim-kitty-navigator'

  -- Toggling booleans and more
  use 'nat-418/boole.nvim'

  -- Move lines and blocks and auto-indent them
  use 'fedepujol/move.nvim'

  -- Dim inactive windows
  -- use "levouh/tint.nvim"

  -- Highlight only the screen line of the cursor in the currently active window
  use 'tummetott/reticle.nvim'

  -- Motion plugin for moving around in the visible area
  use 'ggandor/leap.nvim'

  -- Displays a popup with possible keybindings of the command you started typing
  use 'folke/which-key.nvim'

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end
end)
