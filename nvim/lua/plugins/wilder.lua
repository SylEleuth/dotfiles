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

-- ** Commands above statusline and wildmenu in statusline
wilder.set_option('renderer',  wilder.renderer_mux({
  [':'] = wilder.popupmenu_renderer({
    highlighter = wilder.basic_highlighter(),
    left = {
      ' ',
      wilder.popupmenu_devicons(),
    },
    right = {' ', wilder.popupmenu_scrollbar()},
    highlights = {
      default = wilder.make_hl('MyHighlights1', 'Pmenu', {{a = 1}, {a = 1}, {background = '#1d2021'}}),
      selected = wilder.make_hl('MyHighlights2', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#fe8019', background = '#282828'}}),
      accent = wilder.make_hl('WilderAccent1', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#83a598', background = "#1d2021"}}),
    },
  }),
  ['/'] = wilder.wildmenu_renderer({
    highlighter = wilder.pcre2_highlighter(),
    highlights = {
      default = wilder.make_hl('MyHighlights1', 'Pmenu', {{a = 1}, {a = 1}, {background = '#1d2021'}}),
      selected = wilder.make_hl('MyHighlights3', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#fe8019', background = '#1d2021'}}),
      accent = wilder.make_hl('WilderAccent2', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#83a598', background = '#1d2021'}}),
    },
    separator = ' · ',
    left = {'SEARCH', wilder.wildmenu_spinner(), ' '},
    right = {' ', wilder.wildmenu_index()},
  })
}))



-- ** Commands in the middle of the window and wildmenu in statusline
-- wilder.set_option('renderer',  wilder.renderer_mux({
--   [':'] = wilder.popupmenu_renderer(
--     wilder.popupmenu_palette_theme({
--       -- 'single', 'double', 'rounded' or 'solid'
--       -- can also be a list of 8 characters, see :h wilder#popupmenu_palette_theme() for more details
--       border = 'rounded',
--       min_height = 0,
--       max_height = '50%',
--       min_width = '20%',
--       max_width = '40%',
--       prompt_position = 'bottom',
--       reverse = 0,
--     highlighter = wilder.basic_highlighter(),
--     highlights = {
--       accent = wilder.make_hl('WilderAccent', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#83a598'}}),
--       selected = wilder.make_hl('MyHighlights1', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#fe8019', background = '#282828'}}),
--       -- default = wilder.make_hl('MyHighlights', 'Pmenu', {{a = 1}, {a = 1}, {background = '282828'}}),
--     },
--       left = {
--         ' ',
--         wilder.popupmenu_devicons(),
--         wilder.popupmenu_buffer_flags({
--           flags = ' a + ',
--           icons = {['+'] = '', a = '', h = ''},
--         }),
--       },
--       right = {' ', wilder.popupmenu_scrollbar()},
--     })
--   ),
--   ['/'] = wilder.wildmenu_renderer({
--     highlighter = wilder.pcre2_highlighter(),
--     highlights = {
--       default = wilder.make_hl('MyHighlights', 'Pmenu', {{a = 1}, {a = 1}, {background = '#282828'}}),
--       accent = wilder.make_hl('WilderAccent1', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#83a598', background = '#282828'}}),
--       selected = wilder.make_hl('MyHighlights2', 'Pmenu', {{a = 1}, {a = 1}, {foreground = '#fe8019', background = '#282828'}}),
--     },
--     separator = ' · ',
--     left = {'SEARCH', wilder.wildmenu_spinner(), ' '},
--     right = {' ', wilder.wildmenu_index()},
--   })
-- }))

