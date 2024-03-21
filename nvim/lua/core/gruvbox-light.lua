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
  palette_overrides = {
    light0 = "#ebdbb2",
  },
  overrides = {}
})

vim.o.background = "light"
vim.cmd("colorscheme gruvbox")

local hl = vim.api.nvim_set_hl

hl(0, 'CursorColumn',                 { bg = '#d5c4a1' })
hl(0, 'CursorLine',                   { bg = '#d5c4a1' })

hl(0, 'markid1',                      { fg = '#b57614' })
hl(0, 'markid2',                      { fg = '#79740e' })
hl(0, 'markid3',                      { fg = '#458588' })
hl(0, 'markid4',                      { fg = '#076678' })
hl(0, 'markid5',                      { fg = '#98971a' })
hl(0, 'markid6',                      { fg = '#d79921' })
hl(0, 'markid7',                      { fg = '#8f3f71' })
hl(0, 'markid8',                      { fg = '#427b58' })
hl(0, 'markid9',                      { fg = '#689d6a' })
hl(0, 'markid10',                     { fg = '#b16286' })

hl(0, '@string',                      { fg = '#665c54' })

hl(0, 'TabLineFill',                  { bg = '#ebdbb2' })

hl(0, 'NvimTreeNormal',               { bg = '#ebdbb2' })

hl(0, 'AerialClass',                  { fg = '#458588' })
hl(0, 'AerialFunction',               { fg = '#79740e' })
hl(0, 'AerialGuide',                  { fg = '#79740e' })
hl(0, 'AerialLine',                   { bg = '#fe8019' })

hl(0, 'LeapLabelPrimary',             { fg = '#ebdbb2', bg = '#fe8019' })
hl(0, 'LeapLabelSecondary',           { fg = '#ebdbb2', bg = '#d65d0e' })
hl(0, 'LeapLabelSelected',            { fg = '#ebdbb2', bg = '#8f3f71' })

hl(0, 'HlSearchNear',                 { fg = '#ebdbb2', bg = '#fe8019' })
hl(0, 'HlSearchLens',                 { fg = '#282828', bg = '#d5c4a1' })
hl(0, 'HlSearchLensNear',             { fg = '#ebdbb2', bg = '#fe8019' })

hl(0, 'CocSearch',                    { fg = '#d65d0e', bg = '#fbf1c7' })
hl(0, 'CocMenuSel',                   { fg = '#fbf1c7', bg = '#d65d0e' })
hl(0, 'CocFloating',                  { fg = '#282828', bg = '#fbf1c7' })
hl(0, 'CocCursorRange',               { fg = '#282828', bg = '#8f3f71' })
hl(0, 'CocExplorerNormalFloat',       { bg = '#d5c4a1' })
hl(0, 'CocExplorerNormalFloatBorder', { fg = '#bdae93' })
hl(0, 'CocHintSign',                  { fg = '#bdae93' })

hl(0, 'TreesitterContext',            { bg = '#bdae93' })
hl(0, 'TreesitterContextBottom',      { bg = '#d5c4a1' })
hl(0, 'TSRainbowRed',                 { fg = '#cc241d' })
hl(0, 'TSRainbowYellow',              { fg = '#d79921' })
hl(0, 'TSRainbowBlue',                { fg = '#458588' })
hl(0, 'TSRainbowOrange',              { fg = '#fe8019' })
hl(0, 'TSRainbowGreen',               { fg = '#98971a' })
hl(0, 'TSRainbowViolet',              { fg = '#b16286' })
hl(0, 'TSRainbowCyan',                { fg = '#689d6a' })

hl(0, 'TelescopeMultiSelection',      { fg = '#af3a03' })

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

hl(0, 'NoiceCmdLine',                 { bg = '#d5c4a1' })
hl(0, 'NoicePopupmenuMatch',          { fg = '#076678' })
hl(0, 'NoicePopupmenuSelected',       { fg = '#d65d0e', bg = '#ebdbb2' })
hl(0, 'NoiceScrollbar',               { bg = '#ebdbb2' })
hl(0, 'NoiceScrollbarThumb',          { bg = '#d5c4a1' })

hl(0, 'IndentBlanklineIndent1',       { fg = '#689d6a', nocombine = true })
hl(0, 'IndentBlanklineIndent2',       { fg = '#d65d0e', nocombine = true })
hl(0, 'IndentBlanklineIndent3',       { fg = '#98971a', nocombine = true })
hl(0, 'IndentBlanklineIndent4',       { fg = '#458588', nocombine = true })
hl(0, 'IndentBlanklineIndent5',       { fg = '#d79921', nocombine = true })
hl(0, 'IndentBlanklineIndent6',       { fg = '#b16286', nocombine = true })
hl(0, 'IndentBlanklineContextChar',   { fg = '#9d0006', nocombine = true })
hl(0, 'IndentBlanklineContextStart',  { sp = '#9d0006', underline = true,  nocombine = true })

hl(0, 'WhichKey',                     { bg = '#ebdbb2' })
hl(0, 'WhichKeyGroup',                { fg = '#b16286', bg = '#ebdbb2' })
hl(0, 'WhichKeySeparator',            { fg = '#504945', bg = '#ebdbb2' })
hl(0, 'WhichKeyDesc',                 { fg = '#458588', bg = '#ebdbb2' })
hl(0, 'WhichKeyFloat',                { fg = '#282828', bg = '#ebdbb2' })
hl(0, 'WhichKeyBorder',               { fg = '#d5c4a1', bg = '#ebdbb2' })
hl(0, 'WhichKeyValue',                { bg = '#ebdbb2' })

hl(0, 'VistaParenthesis',             { fg = '#d3869b' })
hl(0, 'VistaScope',                   { fg = '#b16286' })
hl(0, 'VistaTag',                     { fg = '#458588' })
hl(0, 'VistaLineNr',                  { fg = '#665c54' })
hl(0, 'VistaColon',                   { fg = '#504945' })
hl(0, 'VistaIcon',                    { fg = '#d79921' })

hl(0, 'InclineNormal',                { fg = '#504945' })
hl(0, 'InclineNormalNC',              { fg = '#a89984' })

colorful_winsep_bg = '#ebdbb2'
colorful_winsep_fg = '#a89984'

custom_gruvbox = require 'lualine.themes.gruvbox'
custom_gruvbox.normal.a.fg = '#ebdbb2'
custom_gruvbox.normal.a.bg = '#504945'
custom_gruvbox.normal.b.fg = '#504945'
custom_gruvbox.normal.b.bg = '#d5c4a1'
custom_gruvbox.normal.c.fg = '#504945'
custom_gruvbox.normal.c.bg = '#ebdbb2'

cockline_red = vim.g.terminal_color_1
cockline_yellow = vim.g.terminal_color_11
cockline_dark = vim.g.terminal_color_0
cockline_text = vim.g.terminal_color_15
cockline_grey = '#d5c4a1'
cockline_high = '#504945'
cockline_mod = vim.g.terminal_color_4
