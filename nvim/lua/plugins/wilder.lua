local status_ok, wilder = pcall(require, 'wilder')
if not status_ok then
  return
end


wilder.setup({modes = {':', '/', '?'}})

wilder.set_option('pipeline', {
  wilder.branch(
  wilder.python_file_finder_pipeline({
      file_command = {'find', '.', '-type', 'f', '-printf', '%P\n'}, 
      dir_command = {'find', '.', '-type', 'd', '-printf', '%P\n'},
      filters = {'fuzzy_filter', 'difflib_sorter'},
    }),
    wilder.cmdline_pipeline(),
    wilder.python_search_pipeline(),
    wilder.cmdline_pipeline({
      language = 'python',
      fuzzy = 1,
    }),
    wilder.python_search_pipeline({
      pattern = wilder.python_fuzzy_pattern(),
      sorter = wilder.python_difflib_sorter(),
      engine = 're',
    })
  ),
})

local highlighters = {
  wilder.pcre2_highlighter(),
  wilder.basic_highlighter(),
}

wilder.set_option('renderer', wilder.popupmenu_renderer({
  highlighter = wilder.basic_highlighter(),
  highlights = {
    accent = wilder.make_hl('WilderAccent', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#fe8019'}}),
  },
  left = {' ', wilder.popupmenu_devicons()},
  right = {' ', wilder.popupmenu_scrollbar()},
  pumblend = 20,
}))

vim.keymap.set('n', '<leader>wd', ':call wilder#toggle()<cr>')
