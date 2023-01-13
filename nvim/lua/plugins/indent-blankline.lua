-----------------------------------------------------------
-- Indent line configuration file
-----------------------------------------------------------

local status_ok, indent_blankline = pcall(require, 'indent_blankline')
if not status_ok then
  return
end

indent_blankline.setup {
    show_end_of_line = false,
    space_char_blankline = " ",
    show_current_context = true,
    show_current_context_start = true,
    show_first_indent_level = false,
    use_treesitter = false,
    char_highlight_list = {
        "IndentBlanklineIndent1",
        "IndentBlanklineIndent2",
        "IndentBlanklineIndent3",
        "IndentBlanklineIndent4",
        "IndentBlanklineIndent5",
        "IndentBlanklineIndent6",
        },
  filetype_exclude = {
    'lspinfo',
    'packer',
    'checkhealth',
    'help',
    'man',
    'dashboard',
    'git',
    'markdown',
    'text',
    'terminal',
    'NvimTree',
  },
  buftype_exclude = {
    'terminal',
    'nofile',
    'quickfix',
    'prompt',
  },
}

vim.opt.list = true
vim.opt.listchars:append("space:⋅")
--vim.opt.listchars:append("eol:↴")
vim.cmd [[highlight IndentBlanklineIndent1 guifg=#D65D0E gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent2 guifg=#FABD2F gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent3 guifg=#8EC07C gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent4 guifg=#83A598 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent5 guifg=#458588 gui=nocombine]]
vim.cmd [[highlight IndentBlanklineIndent6 guifg=#B16286 gui=nocombine]]
