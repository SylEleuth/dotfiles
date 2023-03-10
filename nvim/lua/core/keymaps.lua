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

-- map('n', '<Space>', '', {})
-- vim.g.mapleader = ' '

map('n', ';', ':')
map('n', 'oo', 'o<Esc>')
map('n', 'OO', 'O<Esc>')
map('n', 'k', 'gkzz')
map('n', 'j', 'gjzz')
map('v', 'k', 'gkzz')
map('v', 'j', 'gjzz')
map('n', 'E', 'ge')
map('v', 'E', 'ge')
map('n', '<Tab>', 'n')
map('n', '<S-Tab>', 'N')
map('n', '<Del>', ':nohlsearch<cr>')

map('n', '<F1>', ':NvimTreeFindFileToggle<cr>')
map('n', '<F2>', ':CocCommand explorer --root-strategies reveal<cr>')
map('n', '<F3>', ':Vista!!<CR>')
map('n', '<leader>aa', ':AerialToggle<CR>')
map('n', '<leader>m', '<Cmd>CocCommand markdown-preview-enhanced.openPreview<cr>')

map('n', '<leader>]', '$')
map('n', '<leader>[', '0')

-- don't lose selection when shifting
map("x", "<", "<gv")
map("x", ">", ">gv")

-- disable ex mode
map("n", "Q", "<nop>")
map("n", "q:", "<nop>")

map('n', '<leader>uu', ':PackerUpdate<cr>')

map('n', '<leader>q', ':Bwipeout<cr>')
-- map('n', '<leader>q', ':bp<bar>sp<bar>bn<bar>bd<CR>')

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
