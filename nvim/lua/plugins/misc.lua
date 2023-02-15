-----------------------------------------------------------
-- Configuration file for miscelanous plugins
-----------------------------------------------------------

-- https://github.com/shortcuts/no-neck-pain.nvim

local status_ok, comment = pcall(require, "Comment")
local status_ok, hlslens = pcall(require, "hlslens")
local status_ok, no_neck_pain = pcall(require, "no-neck-pain")
local status_ok, boole = pcall(require, "boole")
local status_ok, tint = pcall(require, "tint")
local status_ok, reticle = pcall(require, "reticle")
if not status_ok then
  return
end

comment.setup({ ignore = '^$' })

hlslens.setup()

-- require("colorful-winsep").setup({
--   highlight = {
--     bg = "#282828",
--     fg = "#504945",
--   },
--   no_exec_files = { "packer", "TelescopePrompt", "mason", "CompetiTest", "NvimTree" },
-- })


no_neck_pain.setup({
  width = 100,
  toggleMapping = "<F5>",
  buffers = {
    backgroundColor = "#1d2021",
  },
  integrations = {
    NvimTree = {
      position = "left",
    },
  },
})

boole.setup({
  mappings = {
    increment = '<C-a>',
    decrement = '<C-x>'
  },
})

tint.setup({
  tint = -5,  -- Darken colors, use a positive value to brighten
  saturation = 0.6,  -- Saturation to preserve
  transforms = require("tint").transforms.SATURATE_TINT,  -- Showing default behavior, but value here can be predefined set of transforms
  tint_background_colors = true,  -- Tint background portions of highlight groups
  highlight_ignore_patterns = { "WinSeparator", "Status.*" },  -- Highlight group patterns to ignore, see `string.find`
  window_ignore_function = function(winid)
    local bufid = vim.api.nvim_win_get_buf(winid)
    local buftype = vim.api.nvim_buf_get_option(bufid, "buftype")
    local floating = vim.api.nvim_win_get_config(winid).relative ~= ""

    -- Do not tint `terminal` or floating windows, tint everything else
    return buftype == "terminal" or floating
  end
})

reticle.setup{}
