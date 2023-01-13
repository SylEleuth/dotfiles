-----------------------------------------------------------
-- Dashboard configuration file
-----------------------------------------------------------

local status_ok, alpha = pcall(require, 'alpha')
if not status_ok then
  return
end

local dashboard = require('alpha.themes.dashboard')

-- Footer
local function footer()
  local version = vim.version()
  local print_version = "v" .. version.major .. '.' .. version.minor .. '.' .. version.patch
  local datetime = os.date('%Y/%m/%d %H:%M:%S')

  return print_version .. ' - ' .. datetime
end

-- Banner
local banner = {}

dashboard.section.header.val = banner

-- Menu
dashboard.section.buttons.val = {
    dashboard.button('e', '  New file', ':ene <BAR> startinsert<CR>'),
    dashboard.button("r", "  Recent File  ", ":Telescope oldfiles<CR>"),
    dashboard.button("f", "  Find File  ", ":Telescope find_files<CR>"),
    dashboard.button("w", "  Find Word  ", ":Telescope live_grep<CR>"),
    dashboard.button("b", "  Bookmarks  ", ":Telescope marks<CR>"),
    dashboard.button('u', '  Update plugins', ':PackerSync<CR>'),
    dashboard.button("s", "  Settings", ":e $MYVIMRC<CR>"),
    dashboard.button('q', '  Quit', ':qa<CR>'),
}

dashboard.section.footer.val = footer()

alpha.setup(dashboard.config)
