-----------------------------------------------------------
-- Telescope configuration file
-----------------------------------------------------------

local status_ok, telescope = pcall(require, 'telescope')
if not status_ok then
  return
end

local actions = require "telescope.actions"

local transform_mod = require("telescope.actions.mt").transform_mod

local function multiopen(prompt_bufnr, method)
    local cmd_map = {
        vertical = "vsplit",
        horizontal = "split",
        tab = "tabe",
        default = "edit"
    }
    local picker = action_state.get_current_picker(prompt_bufnr)
    local multi_selection = picker:get_multi_selection()

    if #multi_selection > 1 then
        require("telescope.pickers").on_close_prompt(prompt_bufnr)
        pcall(vim.api.nvim_set_current_win, picker.original_win_id)

        for i, entry in ipairs(multi_selection) do
            -- opinionated use-case
            local cmd = i == 1 and "edit" or cmd_map[method]
            vim.cmd(string.format("%s %s", cmd, entry.value))
        end
    else
        actions["select_" .. method](prompt_bufnr)
    end
end

local custom_actions = transform_mod({
    multi_selection_open_vertical = function(prompt_bufnr)
        multiopen(prompt_bufnr, "vertical")
    end,
    multi_selection_open_horizontal = function(prompt_bufnr)
        multiopen(prompt_bufnr, "horizontal")
    end,
    multi_selection_open_tab = function(prompt_bufnr)
        multiopen(prompt_bufnr, "tab")
    end,
    multi_selection_open = function(prompt_bufnr)
        multiopen(prompt_bufnr, "default")
    end,
})

local function stopinsert(callback)
    return function(prompt_bufnr)
        vim.cmd.stopinsert()
        vim.schedule(function()
            callback(prompt_bufnr)
        end)
    end
end


telescope.setup {
  defaults = {
    layout_strategy = "horizontal",
    layout_config = {
      horizontal = {
        prompt_position = "bottom",
        preview_width = 0.55,
        results_width = 0.8,
      },
      vertical = {
        mirror = false,
      },
      width = 0.87,
      height = 0.80,
      preview_cutoff = 120,
    },
    dynamic_preview_title = true,

    prompt_prefix = "  ",
    selection_caret = "➜ ",
    path_display = { "absolute" },

    mappings = {
      i = {
        ["<C-n>"] = actions.cycle_history_next,
        ["<C-p>"] = actions.cycle_history_prev,

        ["<C-j>"] = actions.move_selection_next,
        ["<C-k>"] = actions.move_selection_previous,

        ["<C-c>"] = actions.close,

        ["<Down>"] = actions.move_selection_next,
        ["<Up>"] = actions.move_selection_previous,

        ["<CR>"] = actions.select_default,
        ["<C-x>"] = actions.select_horizontal,
        ["<C-v>"] = actions.select_vertical,
        ["<C-t>"] = actions.select_tab,

        ["<C-u>"] = actions.preview_scrolling_up,
        ["<C-d>"] = actions.preview_scrolling_down,

        ["<PageUp>"] = actions.results_scrolling_up,
        ["<PageDown>"] = actions.results_scrolling_down,

        ["<Tab>"] = actions.toggle_selection + actions.move_selection_worse,
        ["<S-Tab>"] = actions.toggle_selection + actions.move_selection_better,
        ["<C-q>"] = actions.send_to_qflist + actions.open_qflist,
        ["<M-q>"] = actions.send_selected_to_qflist + actions.open_qflist,
        ["<C-l>"] = actions.complete_tag,
        ["<C-_>"] = actions.which_key, -- keys from pressing <C-/>
      },

      n = {
        ["<esc>"] = actions.close,
        ["<CR>"] = actions.select_default,
        ["<C-x>"] = actions.select_horizontal,
        ["<C-v>"] = actions.select_vertical,
        ["<C-t>"] = actions.select_tab,

        ["<Tab>"] = actions.toggle_selection + actions.move_selection_worse,
        ["<S-Tab>"] = actions.toggle_selection + actions.move_selection_better,
        ["<C-q>"] = actions.send_to_qflist + actions.open_qflist,
        ["<M-q>"] = actions.send_selected_to_qflist + actions.open_qflist,

        ["j"] = actions.move_selection_next,
        ["k"] = actions.move_selection_previous,
        ["H"] = actions.move_to_top,
        ["M"] = actions.move_to_middle,
        ["L"] = actions.move_to_bottom,

        ["<Down>"] = actions.move_selection_next,
        ["<Up>"] = actions.move_selection_previous,
        ["gg"] = actions.move_to_top,
        ["G"] = actions.move_to_bottom,

        ["<C-u>"] = actions.preview_scrolling_up,
        ["<C-d>"] = actions.preview_scrolling_down,

        ["<PageUp>"] = actions.results_scrolling_up,
        ["<PageDown>"] = actions.results_scrolling_down,

        ["?"] = actions.which_key,
      },
    },
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
      grep_open_files = true,
    },
    oldfiles = {
      i = {
        ["<C-v>"] = stopinsert(custom_actions.multi_selection_open_vertical),
        ["<C-s>"] = stopinsert(custom_actions.multi_selection_open_horizontal),
        ["<C-t>"] = stopinsert(custom_actions.multi_selection_open_tab),
        ["<CR>"]  = stopinsert(custom_actions.multi_selection_open)
    },
    n = {
        ["<C-v>"] = custom_actions.multi_selection_open_vertical,
        ["<C-s>"] = custom_actions.multi_selection_open_horizontal,
        ["<C-t>"] = custom_actions.multi_selection_open_tab,
        ["<CR>"] = custom_actions.multi_selection_open,
    },
    },
    find_files = {
      -- cwd = '%:p:h',
    },
  },
  extensions = {
    file_browser = {
      hidden = true,
      grouped = true,
      select_buffer = true,
      cwd = '%:p:h',
      require("telescope.themes").get_dropdown {
        previewer = false,
        -- even more opts
      },
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
        use_delta = true,
        side_by_side = true,
        diff_context_lines = vim.o.scrolloff,
        entry_format = "state #$ID, $STAT, $TIME",
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
      require("telescope.themes").get_dropdown {
        previewer = false,
      },
    },
  },
}

require("notify").setup()

require("telescope").load_extension("notify")
require("telescope").load_extension("file_browser")
require("telescope").load_extension("undo")
require('telescope').load_extension('coc')
require('telescope').load_extension('aerial')
require("telescope").load_extension("zf-native")
require('telescope').load_extension('git_diffs')
require('telescope').load_extension('recent_files')

local builtin = require('telescope.builtin')
local extension = require "telescope".extensions

vim.keymap.set('n', '<leader>ee', builtin.find_files, {})
vim.keymap.set('n', '<leader>er', builtin.live_grep, {})
vim.keymap.set('n', '<leader>b', builtin.buffers, {})
vim.keymap.set('n', '<leader>h', builtin.builtin, {})
vim.keymap.set('n', "<leader>'", builtin.oldfiles, {})
vim.keymap.set('n', '<leader>fh', builtin.commands, {})
vim.keymap.set('n', '<leader>hc', builtin.command_history, {})
vim.keymap.set('n', '<leader>hs', builtin.search_history, {})
vim.keymap.set('n', '<leader>v', builtin.treesitter, {})
vim.keymap.set('n', '<leader>e', extension.file_browser.file_browser, {})
vim.keymap.set('n', '<leader>u', extension.undo.undo, {})
vim.keymap.set('n', '<leader>c', extension.coc.coc, {})
vim.keymap.set('n', '<leader>g', extension.aerial.aerial, {})
vim.keymap.set('n', '<leader>d', extension.git_diffs.diff_commits, {})
vim.keymap.set('n', '<leader>\\', extension.recent_files.pick, {})
