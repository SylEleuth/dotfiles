-----------------------------------------------------------
-- Configuration file for miscelanous plugins
-----------------------------------------------------------
-- https://github.com/shortcuts/no-neck-pain.nvim

local status_ok, comment = pcall(require, "Comment")
local status_ok, hlslens = pcall(require, "hlslens")
local status_ok, no_neck_pain = pcall(require, "no-neck-pain")
local status_ok, boole = pcall(require, "boole")
-- local status_ok, tint = pcall(require, "tint")
local status_ok, reticle = pcall(require, "reticle")
local status_ok, leap = pcall(require, "leap")
local status_ok, bufresize = pcall(require, "bufresize")
local status_ok, incline = pcall(require, "incline")
local status_ok, move = pcall(require, "move")
local status_ok, colorful_winsep = pcall(require, "colorful-winsep")
local status_ok, sibling_swap = pcall(require, "sibling-swap")
if not status_ok then
  return
end

comment.setup({ ignore = '^$' })

move.setup()

hlslens.setup()

colorful_winsep.setup({
  -- highlight for Window separator
  hi = {
    bg = colorful_winsep_bg,
    fg = colorful_winsep_fg,
  },
  -- This plugin will not be activated for filetype in the following table.
  no_exec_files = { "packer", "TelescopePrompt", "mason", "CompetiTest", "NvimTree" },
  anchor = {
    left = { height = 1, x = -1, y = -1 },
    right = { height = 1, x = -1, y = 0 },
    up = { width = 0, x = -1, y = 0 },
    bottom = { width = 0, x = 1, y = 0 },
  },
})

-- no_neck_pain.setup({
--   width = 100,
--   mappings = {
--     enabled = true,
--   },
--   integrations = {
--     NvimTree = {
--       position = "left",
--       reopen = true,
--     },
--   },
--   -- buffers = {
--   --   colors = {
--   --     background = "#1d2021",
--   --   },
--   -- },
-- })

boole.setup({
  mappings = {
    increment = '<C-a>',
    decrement = '<C-x>'
  },
})

bufresize.setup()

incline.setup()

-- tint.setup({
--   tint = -5, -- Darken colors, use a positive value to brighten
--   saturation = 0.6, -- Saturation to preserve
--   transforms = require("tint").transforms.SATURATE_TINT, -- Showing default behavior, but value here can be predefined set of transforms
--   tint_background_colors = true, -- Tint background portions of highlight groups
--   highlight_ignore_patterns = { "WinSeparator", "Status.*" }, -- Highlight group patterns to ignore, see `string.find`
--   window_ignore_function = function(winid)
--     local bufid = vim.api.nvim_win_get_buf(winid)
--     local buftype = vim.api.nvim_buf_get_option(bufid, "buftype")
--     local floating = vim.api.nvim_win_get_config(winid).relative ~= ""

--     -- Do not tint `terminal` or floating windows, tint everything else
--     return buftype == "terminal" or floating
--   end
-- })

reticle.setup {}

leap.add_default_mappings()

sibling_swap.setup()
