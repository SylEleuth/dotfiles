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
-- map('n', '<Up>', 'gkzz')
-- map('n', '<Down>', 'gjzz')
map('n', '<Tab>', 'n')
map('n', '<S-Tab>', 'N')
map('n', 'C-z', '', {})

map('n', '<C-Left>', '<C-W>h')
map('n', '<C-Down>', '<C-W>j')
map('n', '<C-Up>', '<C-W>k')
map('n', '<C-Right>', '<C-W>l')

map('n', '<S-Right>', '<Esc>:bnext<cr>')
map('n', '<S-Left>',  '<Esc>:bprevious<cr>')

map('n', '<F1>', ':NvimTreeFindFileToggle<cr>')
map('n', '<F2>', ':CocCommand explorer --root-strategies reveal<cr>')
map('n', '<F3>', ':Vista!!<CR>')

map('n', '<C-j>', ':m .+1<cr>==')
map('n', '<C-k>', ':m .-2<cr>==')
map('i', '<C-j>', '<Esc>:m .+1<cr>==gi')
map('i', '<C-k>', '<Esc>:m .-2<cr>==gi')
map('v', '<C-j>', ":m  '>+1<cr>gv=gv")
map('v', '<C-k>', ":m  '>+1<cr>gv=gv")

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
