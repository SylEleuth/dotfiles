-----------------------------------------------------------
-- Indent line configuration file
-----------------------------------------------------------

local status_ok, indent_blankline = pcall(require, 'ibl')
if not status_ok then
  return
end

local highlight = {
  "RainbowOlive",
  "RainbowOrange",
  "RainbowGreen",
  "RainbowBlue",
  "RainbowYellow",
  "RainbowPurple",
  "RainbowRed",
}

local hooks = require "ibl.hooks"

hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
  vim.api.nvim_set_hl(0, 'RainbowOlive',  { fg = '#8ec07c', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowOrange', { fg = '#fe8019', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowGreen',  { fg = '#b8bb26', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowBlue',   { fg = '#83a598', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowYellow', { fg = '#fabd2f', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowPurple', { fg = '#d3869b', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowRed',    { fg = '#cc241d', nocombine = true })
  vim.api.nvim_set_hl(0, 'RainbowRed',    { sp = '#cc241d', underline = true,  nocombine = true })
end)

indent_blankline.setup {
  scope = {
    show_start = true,
    show_end = false,
    highlight = highlight,
  },
    indent = {
      char = "▎",
      highlight = highlight,
    },
  exclude = {
    filetypes = {
      'lspinfo',
      'packer',
      'checkhealth',
      'help',
      'man',
      'dashboard',
      'git',
      'markdown',
      'text',
      'terminal',
      'NvimTree',
    },
    buftypes = {
      'terminal',
      'nofile',
      'quickfix',
      'prompt',
    },
  },
}

local hooks = require "ibl.hooks"
hooks.register(
  hooks.type.WHITESPACE,
  hooks.builtin.hide_first_space_indent_level
)

vim.opt.list = true
vim.opt.listchars:append("space:⋅")
--vim.opt.listchars:append("eol:↴")
