-----------------------------------------------------------
-- Dashboard configuration file
-----------------------------------------------------------

local status_ok, alpha = pcall(require, 'alpha')
if not status_ok then
  return
end

local dashboard = require('alpha.themes.dashboard')

-- Banner
local banner = {}

dashboard.section.header.val = banner

-- Menu
dashboard.section.buttons.val = {
  dashboard.button("e", "  New file", ":ene <BAR> startinsert <CR>"),
  dashboard.button("r", "ﭯ  Recently opened files", ":Telescope oldfiles<CR>"),
  dashboard.button("f", "  Find File  ", ":Telescope find_files<CR>"),
  -- dashboard.button("p", "  Find project", ":Telescope repo list<CR>"),
  dashboard.button("w", "  Find Word  ", ":Telescope live_grep<CR>"),
  -- dashboard.button("g", "  Find modified file", ":lua require('config.plugins.telescope').my_git_status()<CR>"),
  dashboard.button("m", "  Bookmarks", ":Telescope marks<CR>"),
  -- dashboard.button("t", "  Show todo", ":TodoTelescope<CR>"),
  dashboard.button("s", "  Plugins", ":e ~/.config/nvim/lua/packer_init.lua<CR>"),
  dashboard.button("h", "  Neovim Check health", ":checkhealth<CR>"),
  dashboard.button('u', '  Update plugins', ':PackerSync<CR>'),
  -- dashboard.button("s", "  Settings", ":e $MYVIMRC<CR>"),
  dashboard.button('q', '  Quit', ':qa<CR>'),
}

local function footer()
  local version = vim.version()
  local print_version = "v" .. version.major .. '.' .. version.minor .. '.' .. version.patch
  local datetime = os.date('%A, %e %B %Y  %H:%M:%S')

  return print_version .. ' - ' .. datetime
end

dashboard.section.footer.val = footer()

alpha.setup(dashboard.config)
