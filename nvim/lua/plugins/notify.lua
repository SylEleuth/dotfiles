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
