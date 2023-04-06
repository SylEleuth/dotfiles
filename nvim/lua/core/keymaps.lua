-----------------------------------------------------------
-- Define keymaps of Neovim and installed plugins.
-----------------------------------------------------------

local function map(mode, lhs, rhs, opts)
  local options = { noremap=true, silent=true }
  if opts then
    options = vim.tbl_extend('force', options, opts)
  end
  vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

-- map('n', '<Space>', '')
-- vim.g.mapleader = ' '

map('n', ';', ':')
map('n', 'o', 'o')
map('n', 'O', 'O')
map('n', 'oo', 'o<Esc>')
map('n', 'OO', 'O<Esc>')
-- map('n', 'k', 'gkzz')
-- map('n', 'j', 'gjzz')
-- map('v', 'k', 'gkzz')
-- map('v', 'j', 'gjzz')
map('n', 'E', 'ge')
map('v', 'E', 'ge')
map('n', '<Del>', ':nohlsearch<cr>')

map('n', '<F1>', ':NvimTreeFindFileToggle<cr>')
map('n', '<F2>', ':CocCommand explorer --root-strategies reveal<cr>')
map('n', '<F3>', ':Vista!!<CR>')

-- map('n', '<leader>]', '$')
-- map('n', '<leader>[', '0')

-- don't lose selection when shifting
map("x", "<", "<gv")
map("x", ">", ">gv")

-- disable ex mode
map("n", "Q", "<nop>")
map("n", "q", "<nop>")

-- map('v', 'y', '"+y')
-- map('v', 'p', '"_c<C-r><C-o>+<Esc>')

map('n', '<C-Left>',  ':KittyNavigateLeft<cr>')
map('n', '<C-Down>',  ':KittyNavigateDown<cr>')
map('n', '<C-Up>',    ':KittyNavigateUp<cr>')
map('n', '<C-Right>', ':KittyNavigateRight<cr>')

map('n', '<C-j>', ':MoveLine(1)<CR>')
map('v', '<C-j>', ':MoveBlock(1)<CR>')
map('n', '<C-k>', ':MoveLine(-1)<CR>')
map('v', '<C-k>', ':MoveBlock(-1)<CR>')
map('n', '<C-h>', ':MoveHChar(-1)<CR>')
map('v', '<C-h>', ':MoveHBlock(-1)<CR>')
map('n', '<C-l>', ':MoveHChar(1)<CR>')
map('v', '<C-l>', ':MoveHBlock(1)<CR>')

map('n', '<S-Left>', '<Plug>(cokeline-focus-prev)')
map('n', '<S-Right>', '<Plug>(cokeline-focus-next)')
map('n', '<C-,>', '<Plug>(cokeline-switch-prev)')
map('n', '<C-.>', '<Plug>(cokeline-switch-next)')

map("n", "p", '"+<Plug>(YankyPutAfter)')
map("x", "p", '"+<Plug>(YankyPutAfter)')
map("n", "P", "<Plug>(YankyPutBefore)")
map("x", "P", "<Plug>(YankyPutBefore)")
map("n", "gp", "<Plug>(YankyGPutAfter)")
map("x", "gp", "<Plug>(YankyGPutAfter)")
map("n", "gP", "<Plug>(YankyGPutBefore)")
map("x", "gP", "<Plug>(YankyGPutBefore)")
map("n", "<c-n>", "<Plug>(YankyCycleForward)")
map("n", "<c-p>", "<Plug>(YankyCycleBackward)")

map('n', 'n', "<Cmd>execute('normal! ' . v:count1 . 'n')<CR><Cmd>lua require('hlslens').start()<CR>")
map('n', '<Tab>', "<Cmd>execute('normal! ' . v:count1 . 'n')<CR><Cmd>lua require('hlslens').start()<CR>")
map('n', 'N', "<Cmd>execute('normal! ' . v:count1 . 'N')<CR><Cmd>lua require('hlslens').start()<CR>")
map('n', '<S-Tab>', "<Cmd>execute('normal! ' . v:count1 . 'N')<CR><Cmd>lua require('hlslens').start()<CR>")
map('n', '*', "*<Cmd>lua require('hlslens').start()<CR>")
map('n', '#', "#<Cmd>lua require('hlslens').start()<CR>")
map('n', 'g*', "g*<Cmd>lua require('hlslens').start()<CR>")
map('n', 'g#', "g#<Cmd>lua require('hlslens').start()<CR>")
