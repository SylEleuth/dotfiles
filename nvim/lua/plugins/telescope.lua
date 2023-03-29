-----------------------------------------------------------
-- Telescope configuration file
-----------------------------------------------------------

local status_ok, telescope = pcall(require, 'telescope')
if not status_ok then
  return
end

local actions = require "telescope.actions"
local action_state = require("telescope.actions.state")

local multiopen = {
  ["<CR>"] = function(pb)
    local picker = action_state.get_current_picker(pb)
    local multi = picker:get_multi_selection()
    actions.select_default(pb)
    for _, j in pairs(multi) do
      if j.path ~= nil then
        vim.cmd(string.format("%s %s", "edit", j.path))
      end
    end
  end,
}

local dropdown_configs = {
  layout_strategy = "center",
  -- layout_config = {
  --   prompt_position = "top",
  --   vertical = {
  --     width = 0.6,
  --     height = 20,
  --   },
  -- },
}

telescope.setup {
  defaults = {
    layout_strategy = "flex",
    sorting_strategy = 'ascending',
    layout_config = {
      horizontal = {
        prompt_position = "top",
        preview_width = 0.55,
        width = 0.87,
        height = 0.80,
        preview_cutoff = 140,
      },
      vertical = {
        prompt_position = "top",
        -- preview_height = 0.7,
        width = 0.9,
        preview_height = 0.5,
        mirror = true,
        preview_cutoff = 20,
      },
      flex = {
        flip_columns = 120,
      },
    },
    dynamic_preview_title = true,
    prompt_prefix = "  ",
    selection_caret = "➜ ",
    path_display = { "absolute" },
    mappings = { i = multiopen, n = multiopen },
    -- mappings = {
    --   i = {
    --     ["<C-n>"] = actions.cycle_history_next,
    --     ["<C-p>"] = actions.cycle_history_prev,
    --
    --     ["<C-j>"] = actions.move_selection_next,
    --     ["<C-k>"] = actions.move_selection_previous,
    --
    --     ["<C-c>"] = actions.close,
    --
    --     ["<Down>"] = actions.move_selection_next,
    --     ["<Up>"] = actions.move_selection_previous,
    --
    --     ["<CR>"] = actions.select_default,
    --     ["<C-x>"] = actions.select_horizontal,
    --     ["<C-v>"] = actions.select_vertical,
    --     ["<C-t>"] = actions.select_tab,
    --
    --     ["<C-u>"] = actions.preview_scrolling_up,
    --     ["<C-d>"] = actions.preview_scrolling_down,
    --
    --     ["<PageUp>"] = actions.results_scrolling_up,
    --     ["<PageDown>"] = actions.results_scrolling_down,
    --
    --     ["<Tab>"] = actions.toggle_selection + actions.move_selection_worse,
    --     ["<S-Tab>"] = actions.toggle_selection + actions.move_selection_better,
    --     ["<C-q>"] = actions.send_to_qflist + actions.open_qflist,
    --     ["<M-q>"] = actions.send_selected_to_qflist + actions.open_qflist,
    --     ["<C-l>"] = actions.complete_tag,
    --     ["<C-_>"] = actions.which_key, -- keys from pressing <C-/>
    --   },
    --
    --   n = {
    --     ["<esc>"] = actions.close,
    --     ["<CR>"] = actions.select_default,
    --     ["<C-x>"] = actions.select_horizontal,
    --     ["<C-v>"] = actions.select_vertical,
    --     ["<C-t>"] = actions.select_tab,
    --
    --     ["<Tab>"] = actions.toggle_selection + actions.move_selection_worse,
    --     ["<S-Tab>"] = actions.toggle_selection + actions.move_selection_better,
    --     ["<C-q>"] = actions.send_to_qflist + actions.open_qflist,
    --     ["<M-q>"] = actions.send_selected_to_qflist + actions.open_qflist,
    --
    --     ["j"] = actions.move_selection_next,
    --     ["k"] = actions.move_selection_previous,
    --     ["H"] = actions.move_to_top,
    --     ["M"] = actions.move_to_middle,
    --     ["L"] = actions.move_to_bottom,
    --
    --     ["<Down>"] = actions.move_selection_next,
    --     ["<Up>"] = actions.move_selection_previous,
    --     ["gg"] = actions.move_to_top,
    --     ["G"] = actions.move_to_bottom,
    --
    --     ["<C-u>"] = actions.preview_scrolling_up,
    --     ["<C-d>"] = actions.preview_scrolling_down,
    --
    --     ["<PageUp>"] = actions.results_scrolling_up,
    --     ["<PageDown>"] = actions.results_scrolling_down,
    --
    --     ["?"] = actions.which_key,
    --   },
    -- },
  },
  pickers = {
    select = {
      action = nil, -- nil to use default put action
    },
    telescope = {
      mappings = nil, -- nil to use default mappings
    },
    buffers = {
      include_curret_session = true,
      ignore_current_buffer = true,
      sort_lastused = true,
      sort_mru = true,
    },
    live_grep = {
      cwd = '%:p:h',
    },
    grep_string = {
      cwd = '%:p:h',
    },
    find_files = {
      cwd = '%:p:h',
    },
  },
  extensions = {
    file_browser = {
      hidden = true,
      grouped = true,
      select_buffer = true,
      cwd = '%:p:h',
      mappings = {
        ["i"] = {
          -- your custom insert mode mappings
        },
        ["n"] = {
          -- your custom normal mode mappings
        },
      },
    },
    undo = {
      use_delta = false,
      side_by_side = false,
      diff_context_lines = vim.o.scrolloff,
      entry_format = "state #$ID, $STAT, $TIME",
      layout_strategy = "flex",
      mappings = {
        i = {
          ["<cr>"] = require("telescope-undo.actions").yank_additions,
          ["<S-cr>"] = require("telescope-undo.actions").yank_deletions,
          ["<C-cr>"] = require("telescope-undo.actions").restore,
        },
      },
    },
    coc = {
      prefer_locations = true,
    },
    aerial = {
      show_nesting = {
        ['_'] = false,
        json = true,
        yaml = true,
      }
    },
    ["zf-native"] = {
      file = {
        enable = true,
        highlight_results = true,
        match_filename = true,
      },
      generic = {
        enable = true,
        highlight_results = true,
        match_filename = false,
      },
    },
    ["ui-select"] = {
      require("telescope.themes").get_dropdown(dropdown_configs),
    },
    media_files = {
      filetypes = {"png", "webp", "jpg", "jpeg", "pdf", "gif"},
      find_cmd = "rg"
    },
  },
}

require("notify").setup()
require("urlview").setup()

-- require("telescope").load_extension("notify")
-- require("telescope").load_extension("file_browser")
-- require("telescope").load_extension("undo")
-- require('telescope').load_extension('coc')
-- require('telescope').load_extension('aerial')
-- require("telescope").load_extension("zf-native")
-- require('telescope').load_extension('recent_files')
-- require('telescope').load_extension('smart_open')
-- require('telescope').load_extension('ui-select')
-- require('telescope').load_extension('notify')

-- local builtin = require('telescope.builtin')
-- local extension = require "telescope".extensions

-- keyset('n', '<leader>gg', builtin.grep_string, { noremap = true, silent = true })
-- keyset('n', '<leader>gr', builtin.live_grep, { noremap = true, silent = true })
-- keyset('n', '<leader>ee', builtin.find_files, { noremap = true, silent = true })
-- keyset('n', '<leader>bb', builtin.buffers, { noremap = true, silent = true })
-- keyset('n', '<leader>b', builtin.current_buffer_fuzzy_find, { noremap = true, silent = true })
-- keyset('n', '<leader>s', builtin.spell_suggest, { noremap = true, silent = true })
-- keyset('n', '<leader>hh', builtin.builtin, { noremap = true, silent = true })
-- keyset('n', '<leader>t', builtin.colorscheme, { noremap = true, silent = true })
-- keyset('n', '<leader>fh', builtin.commands, { noremap = true, silent = true })
-- keyset('n', '<leader>hc', builtin.command_history, { noremap = true, silent = true })
-- keyset('n', '<leader>hs', builtin.search_history, { noremap = true, silent = true })
-- keyset('n', '<leader>v', builtin.treesitter, { noremap = true, silent = true })
-- keyset('n', '<leader>e', extension.file_browser.file_browser, { noremap = true, silent = true })
-- keyset('n', '<leader>u', extension.undo.undo, { noremap = true, silent = true })
-- keyset('n', '<leader>c', extension.coc.coc, { noremap = true, silent = true })
-- keyset('n', '<leader>a', extension.aerial.aerial, { noremap = true, silent = true })
-- keyset('n', '<leader>nn', extension.notify.notify, { noremap = true, silent = true })
-- keyset('n', '<leader>\\', extension.recent_files.pick, { noremap = true, silent = true })
-- keyset('n', "<leader>'", extension.smart_open.smart_open, { noremap = true, silent = true })

-- keyset("n", "<leader>/", "<Cmd>UrlView<CR>", { desc = "view buffer URLs" })
-- keyset("n", "<leader>//", "<Cmd>UrlView packer<CR>", { desc = "view plugin URLs" })
