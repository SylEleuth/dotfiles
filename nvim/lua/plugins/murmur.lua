-----------------------------------------------------------
-- Illuminate configuration file
-----------------------------------------------------------

local status_ok, murmur = pcall(require, 'murmur')
if not status_ok then
  return
end

murmur.setup {
  cursor_rgb = {
   guibg = '#504945',
  },
  -- cursor_rgb_always_use_config = false, -- if set to `true`, then always use `cursor_rgb`.
  max_len = 80,
  min_len = 3, -- this is recommended since I prefer no cursorword highlighting on `if`.
  exclude_filetypes = {},
  callbacks = {
    -- to trigger the close_events of vim.diagnostic.open_float.
    function ()
      -- Close floating diag. and make it triggerable again.
      vim.cmd('doautocmd InsertEnter')
      vim.w.diag_shown = false
    end,
  }
}

-- To create IDE-like no blinking diagnostic message with `cursor` scope. (should be paired with the callback above)
vim.api.nvim_create_autocmd({ 'CursorHold' }, {
  group = FOO,
  pattern = '*',
  callback = function ()
    -- skip when a float-win already exists.
    if vim.w.diag_shown then return end

    -- open float-win when hovering on a cursor-word.
    if vim.w.cursor_word ~= '' then
      vim.diagnostic.open_float()
      vim.w.diag_shown = true
    end
  end
})
