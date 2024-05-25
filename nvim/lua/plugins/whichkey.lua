-----------------------------------------------------------
-- Whickkey configuration file
-----------------------------------------------------------
-- https://github.com/folke/which-key.nvim

local status_ok, whichkey = pcall(require, "which-key")
if not status_ok then
  return
end

whichkey.setup({
  plugins = {
    marks = true, -- shows a list of your marks on ' and `
    registers = true, -- shows your registers on " in NORMAL or <C-r> in INSERT mode
    -- the presets plugin, adds help for a bunch of default keybindings in Neovim
    -- No actual key bindings are created
    spelling = {
      enabled = true, -- enabling this will show WhichKey when pressing z= to select spelling suggestions
      suggestions = 20, -- how many suggestions should be shown in the list?
    },
    presets = {
      operators = true, -- adds help for operators like d, y, ...
      motions = true, -- adds help for motions
      text_objects = true, -- help for text objects triggered after entering an operator
      windows = true, -- default bindings on <c-w>
      nav = true, -- misc bindings to work with windows
      z = true, -- bindings for folds, spelling and others prefixed with z
      g = true, -- bindings for prefixed with g
    },
  },
  -- add operators that will trigger motion and text object completion
  -- to enable all native operators, set the preset / operators plugin above
  operators = { gc = "Comments" },
  key_labels = {
    -- override the label used to display some keys. It doesn't effect WK in any other way.
    -- For example:
    -- ["<space>"] = "SPC",
    -- ["<cr>"] = "RET",
    -- ["<tab>"] = "TAB",
  },
  motions = {
    count = true,
  },
  icons = {
    breadcrumb = "»", -- symbol used in the command line area that shows your active key combo
    separator = "➜", -- symbol used between a key and it's label
    group = "+", -- symbol prepended to a group
  },
  popup_mappings = {
    scroll_down = "<c-d>", -- binding to scroll down inside the popup
    scroll_up = "<c-u>", -- binding to scroll up inside the popup
  },
  window = {
    border = "single", -- none, single, double, shadow
    position = "bottom", -- bottom, top
    margin = { 1, 0, 1, 0 }, -- extra window margin [top, right, bottom, left]
    padding = { 0, 0, 0, 0 }, -- extra window padding [top, right, bottom, left]
    winblend = 0, -- value between 0-100 0 for fully opaque and 100 for fully transparent
  },
  layout = {
    height = { min = 5, max = 20 }, -- min and max height of the columns
    width = { min = 20, max = 30 }, -- min and max width of the columns
    spacing = 2, -- spacing between columns
    align = "left", -- align columns left, center or right
  },
  ignore_missing = false, -- enable this to hide mappings for which you didn't specify a label
  hidden = { "<silent>", "<cmd>", "<Cmd>", "<CR>", "^:", "^ ", "^call ", "^lua " }, -- hide mapping boilerplate
  show_help = true, -- show a help message in the command line for using WhichKey
  show_keys = true, -- show the currently pressed key and its label as a message in the command line
  triggers = "auto", -- automatically setup triggers
  -- triggers = {"<leader>"} -- or specifiy a list manually
  -- list of triggers, where WhichKey should not wait for timeoutlen and show immediately
  triggers_nowait = {
    -- marks
    "`",
    "'",
    "g`",
    "g'",
    -- registers
    '"',
    "<c-r>",
    -- spelling
    "z=",
  },
  triggers_blacklist = {
    -- list of mode / prefixes that should never be hooked by WhichKey
    -- this is mostly relevant for keymaps that start with a native binding
    i = { "j", "k" },
    v = { "j", "k" },
  },
  -- disable the WhichKey popup for certain buf types and file types.
  -- Disabled by deafult for Telescope
  disable = {
    buftypes = {},
    filetypes = {},
  },
})

-- local keyset = vim.keymap.set

require("telescope").load_extension("notify")
require("telescope").load_extension("file_browser")
require("telescope").load_extension("undo")
require('telescope').load_extension('coc')
require('telescope').load_extension('aerial')
require("telescope").load_extension("zf-native")
require('telescope').load_extension('recent_files')
require('telescope').load_extension('smart_open')
require('telescope').load_extension('ui-select')
require('telescope').load_extension('notify')
require("telescope").load_extension("yank_history")

local builtin = require('telescope.builtin')
local extension = require "telescope".extensions

whichkey.register({
  ["<Space>"] = { "<cmd>WhichKey<cr>", "" },
  ["<leader>"] = {
    a = {
      name = "Aerial",
      a = { "<cmd>AerialToggle<cr>", "Aerial panel" },
      t = { extension.aerial.aerial, "Aerial telescope " },
    },
    b = { builtin.buffers, "Buffers fuzzy finder" },
    e = {
      name = "Telescope files",
      e = { extension.file_browser.file_browser, "File browser" },
      f = { builtin.find_files, "Find files" },
      n = { "<cmd>enew<cr>", "New file" },
    },
    g = {
      name = "Telescope grep",
      g = { builtin.grep_string, "Grep string" },
      r = { builtin.live_grep, "Live grep" },
    },
    h = {
      name = "Telescope history",
      b = { builtin.builtin, "Telescope builtin" },
      c = { builtin.command, "Command history" },
      h = { builtin.search_history, "Search history" },
      n = { extension.notify.notify, "Notify history" },
      u = { extension.undo.undo, "Undo history" },
      y = { extension.yank_history.yank_history, "Yank history" },
    },
    m = { "<Cmd>MarkdownPreview<cr>", "Markdown preview"},
    q = { "<Cmd>Bwipeout<cr>", "Close buffer"},
    -- s = {
    --   name = "Telescope spell",
    --   s = { builtin.spell_suggest, "Spell suggest" },
    -- },
    v = {
      name = "Telescope treesitter",
      c = { extension.coc.coc, "Coc" },
      t = { builtin.treesitter, "Treesitter" },
    },
    u = {
      name = "Updated",
      u = { "<cmd>PackerUpdate<cr>", "Packer update" },
      r = { "<cmd>UrlView packer<cr>", "Packers URL" },
      c = { "<cmd>CocUpdate<cr>", "Coc update" },
      t = { "<cmd>TSUpdate<cr>", "Treesitter update" },
    },
    z = {
      name = "Telekasten",
      a = { "<cmd>lua require('telekasten').show_tags()<cr>", "Show tags" },
      b = { "<cmd>lua require('telekasten').show_backlinks()<cr>", "Show backlinks" },
      c = { "<cmd>lua require('telekasten').show_calendar()<cr>", "Show calendar" },
      C = { "<cmd>CalendarT<cr>", "Full window Calendar" },
      d = { "<cmd>lua require('telekasten').find_daily_notes()<cr>", "Find daily notes" },
      f = { "<cmd>lua require('telekasten').find_notes()<cr>", "Find notes" },
      F = { "<cmd>lua require('telekasten').find_friends()<cr>", "Find friends" },
      g = { "<cmd>lua require('telekasten').search_notes()<cr>", "Search notes" },
      i = { "<cmd>lua require('telekasten').paste_img_and_link()<cr>", "Pate img and link" },
      I = { "<cmd>lua require('telekasten').insert_img_link({ i=true })<cr>", "Insert img link" },
      l = { "<cmd>lua require('telekasten').follow_link()<cr>", "Follow link" },
      m = { "<cmd>lua require('telekasten').browse_media()<cr>", "Browse media" },
      n = { "<cmd>lua require('telekasten').new_note()<cr>", "New note" },
      N = { "<cmd>lua require('telekasten').new_templated_note()<cr>", "New templated note" },
      p = { "<cmd>lua require('telekasten').preview_img()<cr>", "Preview img " },
      r = { "<cmd>lua require('telekasten').rename_note()<cr>", "Rename note" },
      t = { "<cmd>lua require('telekasten').toggle_todo()<cr>", "Toggle todo" },
      T = { "<cmd>lua require('telekasten').goto_today()<cr>", "Goto today" },
      w = { "<cmd>lua require('telekasten').find_weekly_notes()<cr>", "Find weekly notes" },
      W = { "<cmd>lua require('telekasten').goto_thisweek()<cr>", "Goto this week" },
      y = { "<cmd>lua require('telekasten').yank_notelink()<cr>", "Yank notelink" },
      z = { "<cmd>lua require('telekasten').panel()<cr>", "Panel" },
    },
    ["/"] = {
      name = "Urlview",
      ["/"] = { "<cmd>UrlView<cr>", "View file URLs"},
    },
    ["\\"] = { extension.recent_files.pick, "Recent files"},
    ["'"] = { extension.smart_open.smart_open, "Smart open"},
  },
})

