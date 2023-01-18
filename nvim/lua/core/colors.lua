-----------------------------------------------------------
-- Color schemes configuration file
-----------------------------------------------------------

local status_ok, color_scheme = pcall(require, 'gruvbox')
local colors = require("gruvbox.palette")
if not status_ok then
  return
end


color_scheme.setup({
  undercurl = true,
  underline = true,
  bold = true,
  italic = true,
  strikethrough = true,
  invert_selection = false,
  invert_signs = false,
  invert_tabline = false,
  invert_intend_guides = false,
  inverse = true,
  contrast = "",
  palette_overrides = {},
  overrides = {},
  dim_inactive = false,
  transparent_mode = true,
  overrides = {
    GruvboxRedSign = { fg = colors.red, bg = colors.dark0, reverse = false },
    GruvboxGreenSign = { fg = colors.green, bg = colors.dark0, reverse = false },
    GruvboxYellowSign = { fg = colors.yellow, bg = colors.dark0, reverse = false },
    GruvboxBlueSign = { fg = colors.blue, bg = colors.dark0, reverse = false },
    GruvboxPurpleSign = { fg = colors.purple, bg = colors.dark0, reverse = false },
    GruvboxAquaSign = { fg = colors.aqua, bg = colors.dark0, reverse = false },
    GruvboxOrangeSign = { fg = colors.orange, bg = colors.dark0, reverse = false },
  }
})
vim.cmd("colorscheme gruvbox")


-- Markid config colors
vim.api.nvim_set_hl(0, 'markid1', { fg = '#d79921'})
vim.api.nvim_set_hl(0, 'markid2', { fg = '#98971a'})
vim.api.nvim_set_hl(0, 'markid3', { fg = '#458588'})
vim.api.nvim_set_hl(0, 'markid4', { fg = '#83a598'})
vim.api.nvim_set_hl(0, 'markid5', { fg = '#b8bb26'})
vim.api.nvim_set_hl(0, 'markid6', { fg = '#fabd2f'})
vim.api.nvim_set_hl(0, 'markid7', { fg = '#d3869b'})
vim.api.nvim_set_hl(0, 'markid8', { fg = '#ebdbb2'})
vim.api.nvim_set_hl(0, 'markid9', { fg = '#8ec07c'})
vim.api.nvim_set_hl(0, 'markid10', { fg = '#689d6a'})
