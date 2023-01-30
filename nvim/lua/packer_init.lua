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

-- Install plugins
return packer.startup(function(use)
  -- Add you plugins here:
  use 'wbthomason/packer.nvim' -- packer can manage itself

  use {'neoclide/coc.nvim', branch = 'release'}
  use 'honza/vim-snippets'

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
  use 'nvim-treesitter/nvim-treesitter-refactor'
  use 'nvim-treesitter/nvim-treesitter-textobjects'
  use 'mrjones2014/nvim-ts-rainbow'

  -- Telescope
  use { 'nvim-telescope/telescope.nvim', tag = '0.1.0' }
  use 'nvim-lua/plenary.nvim'
  use 'rcarriga/nvim-notify'
  use 'nvim-telescope/telescope-file-browser.nvim'
  use 'fannheyward/telescope-coc.nvim'
  use 'nvim-lua/popup.nvim'
  use 'natecraddock/telescope-zf-native.nvim'
  use 'debugloop/telescope-undo.nvim'
  use 'paopaol/telescope-git-diffs.nvim'
  use 'smartpde/telescope-recent-files'

  -- Markid - highlight same-name identifiers with the same color
  use 'David-Kunz/markid'

  -- Diffview
  use 'sindrets/diffview.nvim'

  -- Nvim-surround
  use({
    "kylechui/nvim-surround",
    tag = "*", -- Use for stability; omit to use `main` branch for the latest features
    config = function()
      require("nvim-surround").setup({
      })
    end
  })

  -- Yank and clipboard
  use ({
   'gbprod/yanky.nvim',
    requires = { 'kkharji/sqlite.lua' }
  })

  -- Smoooth scrolling
  use 'karb94/neoscroll.nvim'

  -- Wilder
  use 'gelguy/wilder.nvim'

  -- Comment
  use 'numToStr/Comment.nvim'

  -- HLSlens - better searching
  use 'kevinhwang91/nvim-hlslens'

  -- Indent-blankline
  use 'lukas-reineke/indent-blankline.nvim'

  -- Bufdelete
  use 'famiu/bufdelete.nvim'

  -- Window separator
  use 'nvim-zh/colorful-winsep.nvim'

  -- Color schemes
  use "ellisonleao/gruvbox.nvim"
  use 'sainnhe/gruvbox-material'

  -- Statusline
  use 'nvim-lualine/lualine.nvim'

  -- Buffers
  use 'noib3/nvim-cokeline'

  -- File explorer
  use 'nvim-tree/nvim-tree.lua'

  -- Vifm - file manager
  -- use 'vifm/vifm.vim'

  -- Murmur - automatically highlighting other uses of the word under the cursor
  use 'nyngwang/murmur.lua'

  -- Dashboard (start screen)
  use 'goolord/alpha-nvim'

  use {"shortcuts/no-neck-pain.nvim", tag = "*" }

  -- git labels
  use 'lewis6991/gitsigns.nvim'

  -- Rainbow Parentheses
  use 'luochen1990/rainbow'

  -- Vim kitty navigator for seamless navigation between kitty panes and vim splits
  use 'knubie/vim-kitty-navigator'

  -- Automatically set up your configuration after cloning packer.nvim
  -- Put this at the end after all plugins
  if packer_bootstrap then
    require('packer').sync()
  end
end)
