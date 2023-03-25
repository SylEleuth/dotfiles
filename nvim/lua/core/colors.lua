-----------------------------------------------------------
-- Color schemes configuration file
-----------------------------------------------------------

local status_ok, color_scheme = pcall(require, 'gruvbox')
local colors = require("gruvbox.palette")
if not status_ok then
  return
end

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
  overrides = {
    GruvboxRedSign = { fg = colors.red, bg = colors.dark0, reverse = false },
    GruvboxGreenSign = { fg = colors.green, bg = colors.dark0, reverse = false },
    GruvboxYellowSign = { fg = colors.yellow, bg = colors.dark0, reverse = false },
    GruvboxBlueSign = { fg = colors.blue, bg = colors.dark0, reverse = false },
    GruvboxPurpleSign = { fg = colors.purple, bg = colors.dark0, reverse = false },
    GruvboxAquaSign = { fg = colors.aqua, bg = colors.dark0, reverse = false },
    GruvboxOrangeSign = { fg = colors.orange, bg = colors.dark0, reverse = false },
  }
})
vim.cmd("colorscheme gruvbox")

-- Markid config colors
vim.api.nvim_set_hl(0, 'markid1',  { fg = '#d79921' })
vim.api.nvim_set_hl(0, 'markid2',  { fg = '#98971a' })
vim.api.nvim_set_hl(0, 'markid3',  { fg = '#458588' })
vim.api.nvim_set_hl(0, 'markid4',  { fg = '#83a598' })
vim.api.nvim_set_hl(0, 'markid5',  { fg = '#b8bb26' })
vim.api.nvim_set_hl(0, 'markid6',  { fg = '#fabd2f' })
vim.api.nvim_set_hl(0, 'markid7',  { fg = '#d3869b' })
vim.api.nvim_set_hl(0, 'markid8',  { fg = '#427b58' })
vim.api.nvim_set_hl(0, 'markid9',  { fg = '#689d6a' })
vim.api.nvim_set_hl(0, 'markid10', { fg = '#8ec07c' })

vim.cmd [[highlight TabLineFill                  guibg=#282828]]

vim.cmd [[highlight NvimTreeNormal               guibg=#1d2021]]

vim.cmd [[highlight AerialClass                  guifg=#83a598]]
vim.cmd [[highlight AerialFunction               guifg=#b8bb26]]
vim.cmd [[highlight AerialGuide                  guifg=#b8bb26]]
vim.cmd [[highlight AerialLine                   guibg=#fe8019]]

vim.cmd [[highlight LeapLabelPrimary             guifg=#282828 guibg=#fe8019]]
vim.cmd [[highlight LeapLabelSecondary           guifg=#282828 guibg=#d65d0e]]
vim.cmd [[highlight LeapLabelSelected            guifg=#282828 guibg=#d3869b]]

vim.cmd [[highlight HlSearchNear                 guifg=#282828 guibg=#fe9019]]
vim.cmd [[highlight HlSearchLens                 guifg=#ebdbb2 guibg=#1d2021]]
vim.cmd [[highlight HlSearchLensNear             guifg=#282828 guibg=#fe8019]]

vim.cmd [[highlight CocSearch                    guifg=#fe8019 guibg=#282828]]
vim.cmd [[highlight CocMenuSel                   guifg=#282828 guibg=#fe8019]]
vim.cmd [[highlight CocFloating                  guifg=#ebdbb2 guibg=#1d2021]]
vim.cmd [[highlight CocExplorerNormalFloat       guibg=#1d2021]]
vim.cmd [[highlight CocExplorerNormalFloatBorder guifg=#504945]]
vim.cmd [[highlight CocCursorRange               guifg=#ebdbb2 guibg=#b16286]]
vim.cmd [[highlight CocHintSign                  guifg=#504945]]

vim.cmd [[highlight TreesitterContext            guibg=#32302f]]
vim.cmd [[highlight TreesitterContextBottom      guibg=#1d2021]]
vim.cmd [[highlight TSRainbowRed                 guifg=#cc241d]]
vim.cmd [[highlight TSRainbowYellow              guifg=#d79921]]
vim.cmd [[highlight TSRainbowBlue                guifg=#458588]]
vim.cmd [[highlight TSRainbowOrange              guifg=#fe8019]]
vim.cmd [[highlight TSRainbowGreen               guifg=#98971a]]
vim.cmd [[highlight TSRainbowViolet              guifg=#b16286]]
vim.cmd [[highlight TSRainbowCyan                guifg=#689d6a]]

vim.cmd [[highlight NotifyERRORBorder            guifg=#cc241d]]
vim.cmd [[highlight NotifyWARNBorder             guifg=#d65d0e]]
vim.cmd [[highlight NotifyINFOBorder             guifg=#665c54]]
vim.cmd [[highlight NotifyDEBUGBorder            guifg=#928374]]
vim.cmd [[highlight NotifyTRACEBorder            guifg=#b16286]]
vim.cmd [[highlight NotifyERRORIcon              guifg=#fb4934]]
vim.cmd [[highlight NotifyWARNIcon               guifg=#d79921]]
vim.cmd [[highlight NotifyINFOIcon               guifg=#8ec07c]]
vim.cmd [[highlight NotifyDEBUGIcon              guifg=#928374]]
vim.cmd [[highlight NotifyTRACEIcon              guifg=#d3869b]]
vim.cmd [[highlight NotifyERRORTitle             guifg=#fb4934]]
vim.cmd [[highlight NotifyWARNTitle              guifg=#d79921]]
vim.cmd [[highlight NotifyINFOTitle              guifg=#8ec07c]]
vim.cmd [[highlight NotifyDEBUGTitle             guifg=#8B8B8B]]
vim.cmd [[highlight NotifyTRACETitle             guifg=#d3869b]]

vim.cmd [[highlight NoiceCmdLine                 guibg=#1d2021]]
vim.cmd [[highlight NoicePopupmenuMatch          guifg=#458588]]
vim.cmd [[highlight NoicePopupmenuSelected       guifg=#fe8019 guibg=#282828]]
vim.cmd [[highlight NoiceScrollbar               guibg=#282828]]
vim.cmd [[highlight NoiceScrollbarThumb          guibg=#3c3836]]

vim.cmd [[highlight IndentBlanklineIndent1       guifg=#D65D0E gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent2       guifg=#FABD2F gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent3       guifg=#8EC07C gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent4       guifg=#83A598 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent5       guifg=#458588 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent6       guifg=#B16286 gui=nocombine]]
