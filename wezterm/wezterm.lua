local wezterm = require 'wezterm';

local mykeys = {}

for i = 1, 8 do
  -- ALT + number to activate that tab
  table.insert(mykeys, {
    key=tostring(i),
    mods="ALT",
    action=wezterm.action{ActivateTab=i-1},
  })
  -- F1 through F8 to activate that tab
  table.insert(mykeys, {
    key="F" .. tostring(i),
    action=wezterm.action{ActivateTab=i-1},
  })
end


return {

    keys = mykeys,

  -- timeout_milliseconds defaults to 1000 and can be omitted
  leader = { key="a", mods="CTRL", timeout_milliseconds=1000 },
  keys = {
    {key="LeftArrow", mods="ALT", action=wezterm.action{ActivateTabRelative=-1}},
    {key="RightArrow", mods="ALT", action=wezterm.action{ActivateTabRelative=1}},
    {key="LeftArrow", mods="SHIFT|ALT", action=wezterm.action{MoveTabRelative=-1}},
    {key="RightArrow", mods="SHIFT|ALT", action=wezterm.action{MoveTabRelative=1}},
    {key="LeftArrow", mods="CTRL|ALT", action=wezterm.action{ActivatePaneDirection="Left"}},
    {key="RightArrow", mods="CTRL|ALT", action=wezterm.action{ActivatePaneDirection="Right"}},
    {key="UpArrow", mods="CTRL|ALT", action=wezterm.action{ActivatePaneDirection="Up"}},
    {key="DownArrow", mods="CTRL|ALT", action=wezterm.action{ActivatePaneDirection="Down"}},
    {key="t", mods="ALT", action=wezterm.action{SpawnTab="CurrentPaneDomain"}},
    {key="w", mods="ALT", action=wezterm.action{CloseCurrentTab={confirm=true}}},
    {key="x", mods="ALT", action=wezterm.action{CloseCurrentPane={confirm=true}}},
    {key="h", mods="LEADER", action=wezterm.action{SplitHorizontal={domain="CurrentPaneDomain"}}},
    {key="v", mods="LEADER", action=wezterm.action{SplitVertical={domain="CurrentPaneDomain"}}},
    -- Send "CTRL-A" to the terminal when pressing CTRL-A, CTRL-A
    {key="a", mods="LEADER|CTRL", action=wezterm.action{SendString="\x01"}},
  },

  hide_tab_bar_if_only_one_tab=true,

  -- font = wezterm.font("FuraCode Nerd Font", {weight="Medium"}),
  font = wezterm.font("JetBrainsMono Nerd Font", {weight="Bold"}),
  font_size = 9.0,

  line_height = 1.0,

  front_end = "OpenGL",

  color_scheme = "Gruvbox",
	color_schemes = {
		["Gruvbox"] = {
			foreground = "#ebdbb2",
			background = "#1d2021",
			cursor_bg = "#ebdbb2",
			cursor_border = "#ebdbb2",
			cursor_fg = "#282828",
			selection_bg = "#655c54",
			selection_fg = "#ebdbb2",

			ansi = {
                "#282828",
                "#cc241d",
                "#98971a",
                "#d79921",
                "#448588",
                "#b16286",
                "#689d6a",
                "#a89984"
            },
			brights = {
                "#928374",
                "#fb4934",
                "#b8bb26",
                "#fabd2f",
                "#83a598",
                "#d3869b",
                "#8ec07c",
                "#ebdbb2"
            },
		}
	},

  colors = {
	-- foreground = "#ebdbb2",
	-- background = "#282828",
	-- cursor_bg = "#ebdbb2",
	-- cursor_border = "#ebdbb2",
	-- cursor_fg = "#282828",
	-- selection_bg = "#655b53",
	-- selection_fg = "#ebdbb2",

	-- ansi = {"#282828", "#cc231c", "#989719", "#d79920", "#448488", "#b16185", "#689d69", "#a89983"},
	-- brights = {"#928373", "#fb4833", "#b8ba25", "#fabc2e", "#83a597", "#d3859a", "#8ec07b", "#ebdbb2"},

    tab_bar = {

      background = "#282828",

      active_tab = {
        bg_color = "#1d2021",
        fg_color = "#ebdbb2",

        intensity = "Normal",
        underline = "None",
        italic = false,
        strikethrough = false,
      },

      inactive_tab = {
        bg_color = "#3c3836",
        fg_color = "#928374",
      },

      inactive_tab_hover = {
        bg_color = "#282828",
        fg_color = "#928374",
        italic = true,
      }
    }
  }
}
