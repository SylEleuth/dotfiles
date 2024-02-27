-----------------------------------------------------------
-- Color schemes configuration file
-----------------------------------------------------------

local status_ok, color_scheme = pcall(require, 'gruvbox')
local colors = require("gruvbox")
if not status_ok then
  return
end

indent_highlight = {
  "IndentBlanklineIndent1",
  "IndentBlanklineIndent2",
  "IndentBlanklineIndent3",
  "IndentBlanklineIndent4",
  "IndentBlanklineIndent5",
  "IndentBlanklineIndent6",
  'IndentBlanklineContextChar',
  'IndentBlanklineContextStart',
}

color_scheme.setup({
  undercurl = true,
  underline = true,
  bold = true,
  italic = {
    strings = true,
    comments = true,
    operators = false,
    folds = true,
  },
  strikethrough = true,
  invert_selection = false,
  invert_signs = false,
  invert_tabline = false,
  invert_intend_guides = false,
  inverse = true,
  contrast = "",
  dim_inactive = false,
  transparent_mode = true,
  palette_overrides = {},
  overrides = {}
})

vim.o.background = "dark"
vim.cmd("colorscheme gruvbox")

local hl = vim.api.nvim_set_hl

hl(0, 'CursorColumn',                 { bg = '#32302f' })
hl(0, 'CursorLine',                   { bg = '#32302f' })

hl(0, 'markid1',                      { fg = '#d79921' })
hl(0, 'markid2',                      { fg = '#98971a' })
hl(0, 'markid3',                      { fg = '#458588' })
hl(0, 'markid4',                      { fg = '#83a598' })
hl(0, 'markid5',                      { fg = '#b8bb26' })
hl(0, 'markid6',                      { fg = '#fabd2f' })
hl(0, 'markid7',                      { fg = '#d3869b' })
hl(0, 'markid8',                      { fg = '#427b58' })
hl(0, 'markid9',                      { fg = '#689d6a' })
hl(0, 'markid10',                     { fg = '#8ec07c' })

hl(0, '@string',                      { fg = '#d5c4a1' })

hl(0, 'TabLineFill',                  { bg = '#282828' })

hl(0, 'NvimTreeNormal',               { bg = '#1d2021' })

hl(0, 'AerialClass',                  { fg = '#83a598' })
hl(0, 'AerialFunction',               { fg = '#b8bb26' })
hl(0, 'AerialGuide',                  { fg = '#b8bb26' })
hl(0, 'AerialLine',                   { bg = '#fe8019' })

hl(0, 'LeapLabelPrimary',             { fg = '#282828', bg = '#fe8019' })
hl(0, 'LeapLabelSecondary',           { fg = '#282828', bg = '#d65d0e' })
hl(0, 'LeapLabelSelected',            { fg = '#282828', bg = '#d3869b' })

hl(0, 'HlSearchNear',                 { fg = '#282828', bg = '#fe8019' })
hl(0, 'HlSearchLens',                 { fg = '#ebdbb2', bg = '#1d2021' })
hl(0, 'HlSearchLensNear',             { fg = '#282828', bg = '#fe8019' })

hl(0, 'CocSearch',                    { fg = '#fe8019', bg = '#282828' })
hl(0, 'CocMenuSel',                   { fg = '#282828', bg = '#fe8019' })
hl(0, 'CocFloating',                  { fg = '#ebdbb2', bg = '#1d2021' })
hl(0, 'CocCursorRange',               { fg = '#ebdbb2', bg = '#b16286' })
hl(0, 'CocExplorerNormalFloat',       { bg = '#1d2021' })
hl(0, 'CocExplorerNormalFloatBorder', { fg = '#504945' })
hl(0, 'CocHintSign',                  { fg = '#504945' })

hl(0, 'TreesitterContext',            { bg = '#32302f' })
hl(0, 'TreesitterContextBottom',      { bg = '#1d2021' })
-- hl(0, 'TSRainbowRed',                 { fg = '#cc241d' })
-- hl(0, 'TSRainbowYellow',              { fg = '#d79921' })
-- hl(0, 'TSRainbowBlue',                { fg = '#458588' })
-- hl(0, 'TSRainbowOrange',              { fg = '#fe8019' })
-- hl(0, 'TSRainbowGreen',               { fg = '#98971a' })
-- hl(0, 'TSRainbowViolet',              { fg = '#b16286' })
-- hl(0, 'TSRainbowCyan',                { fg = '#689d6a' })

hl(0, 'TelescopeMultiSelection',      { fg = '#fe8019' })

-- hl(0, 'NotifyERRORBorder',            { fg = '#cc241d' })
-- hl(0, 'NotifyWARNBorder',             { fg = '#d65d0e' })
-- hl(0, 'NotifyINFOBorder',             { fg = '#665c54' })
-- hl(0, 'NotifyDEBUGBorder',            { fg = '#928374' })
-- hl(0, 'NotifyTRACEBorder',            { fg = '#b16286' })
-- hl(0, 'NotifyERRORIcon',              { fg = '#fb4934' })
-- hl(0, 'NotifyWARNIcon',               { fg = '#d79921' })
-- hl(0, 'NotifyINFOIcon',               { fg = '#8ec07c' })
-- hl(0, 'NotifyDEBUGIcon',              { fg = '#928374' })
-- hl(0, 'NotifyTRACEIcon',              { fg = '#d3869b' })
-- hl(0, 'NotifyERRORTitle',             { fg = '#fb4934' })
-- hl(0, 'NotifyWARNTitle',              { fg = '#d79921' })
-- hl(0, 'NotifyINFOTitle',              { fg = '#8ec07c' })
-- hl(0, 'NotifyDEBUGTitle',             { fg = '#928374' })
-- hl(0, 'NotifyTRACETitle',             { fg = '#d3869b' })

hl(0, 'NoiceCmdLine',                 { bg = '#1d2021' })
hl(0, 'NoicePopupmenuMatch',          { fg = '#458588' })
hl(0, 'NoicePopupmenuSelected',       { fg = '#fe8019', bg = '#282828' })
hl(0, 'NoiceScrollbar',               { bg = '#282828' })
hl(0, 'NoiceScrollbarThumb',          { bg = '#3c3836' })

hl(0, 'IndentBlanklineIndent1',       { fg = '#8ec07c', nocombine = true })
hl(0, 'IndentBlanklineIndent2',       { fg = '#fe8019', nocombine = true })
hl(0, 'IndentBlanklineIndent3',       { fg = '#b8bb26', nocombine = true })
hl(0, 'IndentBlanklineIndent4',       { fg = '#83a598', nocombine = true })
hl(0, 'IndentBlanklineIndent5',       { fg = '#fabd2f', nocombine = true })
hl(0, 'IndentBlanklineIndent6',       { fg = '#d3869b', nocombine = true })
hl(0, 'IndentBlanklineContextChar',   { fg = '#cc241d', nocombine = true })
hl(0, 'IndentBlanklineContextStart',  { sp = '#cc241d', underline = true,  nocombine = true })

hl(0, 'WhichKey',                     { bg = '#282828' })
hl(0, 'WhichKeyGroup',                { fg = '#d3869b', bg = '#282828' })
hl(0, 'WhichKeySeparator',            { fg = '#a89984', bg = '#282828' })
hl(0, 'WhichKeyDesc',                 { fg = '#83a598', bg = '#282828' })
hl(0, 'WhichKeyFloat',                { fg = '#ebdbb2', bg = '#282828' })
hl(0, 'WhichKeyBorder',               { fg = '#1d2021', bg = '#282828' })
hl(0, 'WhichKeyValue',                { bg = '#282828' })

hl(0, 'VistaParenthesis',             { fg = '#d3869b' })
hl(0, 'VistaScope',                   { fg = '#b16286' })
hl(0, 'VistaTag',                     { fg = '#83a598' })
hl(0, 'VistaLineNr',                  { fg = '#928374' })
hl(0, 'VistaColon',                   { fg = '#d5c4a1' })
hl(0, 'VistaIcon',                    { fg = '#fabd2f' })

hl(0, 'InclineNormal',                { fg = '#ebdbb2' })
hl(0, 'InclineNormalNC',              { fg = '#928374' })


custom_gruvbox = require 'lualine.themes.gruvbox'
custom_gruvbox.normal.c.bg = '#282828'
custom_gruvbox.normal.b.bg = '#3c3836'

cockline_red = vim.g.terminal_color_1
cockline_yellow = vim.g.terminal_color_11
cockline_dark = vim.g.terminal_color_0
cockline_text = vim.g.terminal_color_15
cockline_grey = '#3c3836'
cockline_high = vim.g.terminal_color_7
cockline_mod = vim.g.terminal_color_12
