-----------------------------------------------------------
-- Configuration file for notify plugin
-----------------------------------------------------------

-- https://github.com/rcarriga/nvim-notify

local status_ok, notify = pcall(require, "notify")
if not status_ok then
  return
end

notify.setup({
  background_colour = "#282828",
  stages = "slide",
  render = "compact",
  minimum_width = 50,
  timeout = 1000,
  top_down = false,
})


vim.cmd [[highlight NotifyERRORBorder guifg=#cc241d]]
vim.cmd [[highlight NotifyWARNBorder guifg=#d65d0e]]
vim.cmd [[highlight NotifyINFOBorder guifg=#665c54]]
vim.cmd [[highlight NotifyDEBUGBorder guifg=#928374]]
vim.cmd [[highlight NotifyTRACEBorder guifg=#b16286]]
vim.cmd [[highlight NotifyERRORIcon guifg=#fb4934]]
vim.cmd [[highlight NotifyWARNIcon guifg=#d79921]]
vim.cmd [[highlight NotifyINFOIcon guifg=#8ec07c]]
vim.cmd [[highlight NotifyDEBUGIcon guifg=#928374]]
vim.cmd [[highlight NotifyTRACEIcon guifg=#d3869b]]
vim.cmd [[highlight NotifyERRORTitle  guifg=#fb4934]]
vim.cmd [[highlight NotifyWARNTitle guifg=#d79921]]
vim.cmd [[highlight NotifyINFOTitle guifg=#8ec07c]]
vim.cmd [[highlight NotifyDEBUGTitle  guifg=#8B8B8B]]
vim.cmd [[highlight NotifyTRACETitle  guifg=#d3869b]]
