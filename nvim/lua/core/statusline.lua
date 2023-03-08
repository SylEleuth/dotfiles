----------------------------------------------------------
-- Statusline configuration file
-----------------------------------------------------------

-- https://github.com/nvim-lualine/lualine.nvim
-- https://github.com/noib3/nvim-cokeline


local status_ok, lualine = pcall(require, 'lualine')
local status_ok, cokeline = pcall(require, 'cokeline')
if not status_ok then
  return
end

local function stats()
  local row = vim.api.nvim_win_get_cursor(0)[1]
  local col = vim.api.nvim_win_get_cursor(0)[2]
  local max = vim.api.nvim_buf_line_count(vim.fn.winbufnr(vim.g.statusline_winid))
  local line = "%p" .. "%% :" .. row .. "/" .. max .. "☰ ℅:" .. col + 1
  return line
end

local custom_gruvbox = require 'lualine.themes.gruvbox'

custom_gruvbox.normal.c.bg = '#282828'
custom_gruvbox.normal.b.bg = '#3c3836'

lualine.setup {
  options = {
    icons_enabled = true,
    theme = 'gruvbox',
    component_separators = { left = '', right = '' },
    section_separators = { left = '', right = '' },
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
    lualine_a = { 'mode' },
    lualine_b = { 'branch',
      { 'diff',
        symbols = { added = ' ', modified = ' ', removed = ' ' },
      },
      { 'diagnostics',
        sources = { 'nvim_diagnostic', 'coc' },
        sections = { 'error', 'warn', 'info', 'hint' },
        -- colored = false,
      },
    },
    lualine_c = {
      { 'filename',
        path = 1,
        shorting_target = 20,
      }
    },
    lualine_x = { { 'aerial' },
      {
        require("noice").api.statusline.mode.get,
        cond = require("noice").api.statusline.mode.has,
        color = { fg = "#fe8019" },
      },
    },
    lualine_y = {
      { 'filetype',
        colored = false,
      } },
    lualine_z = { stats }
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {},
    lualine_x = { 'location' },
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
    'aerial'
  }
}

-- buffer bar configuration

local is_picking_focus = require("cokeline/mappings").is_picking_focus
local is_picking_close = require("cokeline/mappings").is_picking_close
local get_hex = require("cokeline/utils").get_hex


local red = vim.g.terminal_color_1
local yellow = vim.g.terminal_color_11
local space = { text = " " }
local dark = vim.g.terminal_color_0
local text = get_hex("Comment", "fg")
local grey = "#3c3836"
local light = get_hex("Comment", "fg")
local high = vim.g.terminal_color_7
local mod = vim.g.terminal_color_12

vim.cmd [[highlight TabLineFill guibg=#282828]] -- background of the top bar

cokeline.setup(
  {
    show_if_buffers_are_at_least = 2,
    buffers = {
      new_buffers_position = "next",
    },
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

vim.keymap.set('n', '<S-Left>', '<Plug>(cokeline-focus-prev)', {})
vim.keymap.set('n', '<S-Right>', '<Plug>(cokeline-focus-next)', {})
vim.keymap.set('n', '<C-,>', '<Plug>(cokeline-switch-prev)', {})
vim.keymap.set('n', '<C-.>', '<Plug>(cokeline-switch-next)', {})
