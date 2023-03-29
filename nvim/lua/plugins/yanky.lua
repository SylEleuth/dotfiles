-----------------------------------------------------------
-- Yanky configuration file
-----------------------------------------------------------

local status_ok, yanky = pcall(require, 'yanky')
if not status_ok then
  return
end

local utils = require("yanky.utils")
local mapping = require("yanky.telescope.mapping")

yanky.setup({
	ring = {
		history_length = 100,
		storage = "sqlite",
		sync_with_numbered_registers = true,
		cancel_event = "update",
	},
	system_clipboard = {
		sync_with_ring = true,
	},
	highlight = {
		on_put = true,
		on_yank = true,
		timer = 500,
	},
    preserve_cursor_position = {
        enabled = true,
    },
	picker = {
		telescope = {
			mappings = {
				default = mapping.put("p"),
				i = {
					["<c-p>"] = mapping.put("p"),
					["<c-k>"] = mapping.put("P"),
					["<c-x>"] = mapping.delete(),
					["<c-r>"] = mapping.set_register(utils.get_default_register()),
					["<c-h>"]  = mapping.special_put("YankyPutAfterCharwiseJoined"),
				},
				n = {
					p = mapping.put("p"),
					P = mapping.put("P"),
					d = mapping.delete(),
					r = mapping.set_register(utils.get_default_register()),
					h = mapping.special_put("YankyPutAfterCharwiseJoined"),
				},
			}
		}
	}
})
