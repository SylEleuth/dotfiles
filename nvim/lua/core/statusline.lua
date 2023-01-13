----------------------------------------------------------
-- Statusline configuration file
-----------------------------------------------------------

-- https://github.com/nvim-lualine/lualine.nvim
-- https://github.com/noib3/nvim-cokeline


local status_ok, lualine = pcall(require, 'lualine')
if not status_ok then
  return
end

function stats()
  row = vim.api.nvim_win_get_cursor(0)[1]
  col = vim.api.nvim_win_get_cursor(0)[2]
  max = vim.api.nvim_buf_line_count(vim.fn.winbufnr(vim.g.statusline_winid))
  line = "%p" .. "%% :" .. row .. "/" .. max .. "☰ ℅:" .. col
  return line
end

local custom_gruvbox = require'lualine.themes.gruvbox'

custom_gruvbox.normal.c.bg = '#32302f'

lualine.setup {
  options = {
    icons_enabled = true,
    theme = 'gruvbox',
    component_separators = { left = '', right = ''},
    section_separators = { left = '', right = ''},
    disabled_filetypes = {
      statusline = {},
      winbar = {},
    },
    ignore_focus = {},
    always_divide_middle = true,
    globalstatus = false,
    refresh = {
      statusline = 1000,
      tabline = 1000,
      winbar = 1000,
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch',
      {'diff',
        -- colored = false,
      }},
    lualine_c = {
      {'diagnostics',
        sources = { 'nvim_diagnostic', 'coc' },
        sections = { 'error', 'warn', 'info', 'hint' },
        -- colored = false,
      },
      {'filename',
        path = 2,
      }
    },
    lualine_x = {},
    lualine_y = {
      {'filetype',
        colored = false,
      }},
    lualine_z = {stats}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  },
  -- tabline = {
  --   lualine_a = {'buffers'}
  -- },
  winbar = {},
  inactive_winbar = {},
  extensions = {
    'nvim-tree',
    'aerial',
  }
}

-- buffer bar configuration

local is_picking_focus = require("cokeline/mappings").is_picking_focus
local is_picking_close = require("cokeline/mappings").is_picking_close
local get_hex = require("cokeline/utils").get_hex


local red = "#cc241d"
local yellow = "#fabd2f"
local space = {text = " "}
local dark = "#282828"
local text = get_hex("Comment", "fg")
local grey = "#32302f"
local light = get_hex("Comment", "fg")
local high = "#a89984"
local mod = "#83a598"

vim.cmd [[highlight TabLineFill guibg=dark]] -- background of the top bar

require("cokeline").setup(
  {
    default_hl = {
      fg = function(buffer)
        if buffer.is_focused then
          return dark
        end

        if buffer.is_modified then
          return mod
        else
          return light
        end

        return text
      end,
      bg = function(buffer)
        if buffer.is_focused and buffer.is_modified then
          return mod
        elseif buffer.is_focused then
          return high
        end
        return grey
      end
    },
    components = {
      {
        text = function(buffer)
          if buffer.index ~= 1 then
            return ""
          end
          return ""
        end,
        bg = function(buffer)
          if buffer.is_focused and buffer.is_modified then
            return mod
          elseif buffer.is_focused then
            return high
          end
          return grey
        end,
        fg = dark
      },
      space,
      {
        text = function(buffer)
          if is_picking_focus() or is_picking_close() then
            return buffer.pick_letter .. " - "
          end
          return buffer.devicon.icon
        end,
        fg = function(buffer)
          if is_picking_focus() then
            return yellow
          end
          if is_picking_close() then
            return red
          end

          if buffer.is_focused then
            return dark
          else
            return light
          end
        end,
        style = function(_)
          return (is_picking_focus() or is_picking_close()) and "italic,bold" or nil
        end
      },
      {
        text = function(buffer)
          return buffer.unique_prefix .. buffer.filename .. "⠀"
        end,
        style = function(buffer)
          return buffer.is_focused and "bold" or nil
        end
      },
      {
        text = "",
        fg = function(buffer)
          if buffer.is_focused and buffer.is_modified then
            return mod
          elseif buffer.is_focused then
            return high
          end
          return grey
        end,
        bg = dark
      }
    }
  }
)
