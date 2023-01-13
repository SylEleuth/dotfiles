-----------------------------------------------------------
-- Configuration file for miscelanous plugins
-----------------------------------------------------------

-- https://github.com/shortcuts/no-neck-pain.nvim

local status_ok, comment = pcall(require, "Comment")
local status_ok, hlslens = pcall(require, "hlslens")
local status_ok, no_neck_pain = pcall(require, "no-neck-pain")
if not status_ok then
  return
end

comment.setup()
hlslens.setup()

require("colorful-winsep").setup({
  highlight = {
    bg = "#282828",
    fg = "#504945",
  },
  no_exec_files = { "packer", "TelescopePrompt", "mason", "CompetiTest", "NvimTree" },
})


no_neck_pain.setup({
  width = 100,
  toggleMapping = "<Leader>np",
  buffers = {
    backgroundColor = "#1d2021",
  },
  integrations = {
    NvimTree = {
      position = "left",
    },
  },
})
