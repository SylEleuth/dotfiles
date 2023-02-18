-----------------------------------------------------------
-- Autocommand functions
-----------------------------------------------------------

-- Define autocommands with Lua APIs
-- See: h:api-autocmd, h:augroup

local augroup = vim.api.nvim_create_augroup   -- Create/get autocommand group
local autocmd = vim.api.nvim_create_autocmd   -- Create autocommand

-- General settings:
--------------------

-- Remove whitespace on save
autocmd('BufWritePre', {
  pattern = '',
  command = ":%s/\\s\\+$//e"
})


-- Settings for filetypes:
--------------------------

-- Set python indentation to 4 spaces
augroup('setIndent', { clear = true })
autocmd('Filetype', {
  group = 'setIndent',
  pattern = { 'python' },
  command = 'setlocal shiftwidth=4 tabstop=4 softtabstop=4'
})

-- Set lua indentation
autocmd('Filetype', {
  group = 'setIndent',
  pattern = { 'lua' },
  command = 'setlocal shiftwidth=2 tabstop=2 softtabstop=2'
})


-- Format on save with coc
--------------------------

autocmd('BufWritePre', {
  group = augroup('black_on_save', { clear = true }),
	callback = function (opts)
		if vim.bo[opts.buf].filetype == 'python' then
			vim.cmd ":call CocAction('format')"
		end
	end,
})

-- autocmd('BufWritePre', {
--   pattern = '*.py',
--   command = ":call CocAction('runCommand', 'python.sortImports')"
-- })


-- Autotoggle relative numbers:
-------------------------------

local numbertogglegroup = augroup("numbertoggle", {})
autocmd(
    {"BufEnter", "FocusGained", "InsertLeave"},
    {
        pattern = '*',
        callback = function()
            vim.wo.relativenumber = true
        end,
        group = numbertogglegroup
    })
autocmd(
    {"BufLeave","FocusLost","InsertEnter"},
    {
        pattern = '*',
        callback = function()
            vim.wo.relativenumber = false
        end,
        group = numbertogglegroup
    })


-- Automatically jump to the last place you’ve visited in a file before exiting
-------------------------------------------------------------------------------

autocmd('BufReadPost', {
  callback = function()
    local mark = vim.api.nvim_buf_get_mark(0, '"')
    local lcount = vim.api.nvim_buf_line_count(0)
    if mark[1] > 0 and mark[1] <= lcount then
      pcall(vim.api.nvim_win_set_cursor, 0, mark)
    end
  end,
})

