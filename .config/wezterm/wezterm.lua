local wezterm = require("wezterm")
local config = wezterm.config_builder()

config.default_prog = {"/usr/bin/fish"}
config.enable_wayland = false

config.color_scheme = "Gruvbox dark, medium (base16)"
config.hide_tab_bar_if_only_one_tab = true
config.font = wezterm.font("Hack Nerd Font")
config.font_size = 11
config.window_close_confirmation = "NeverPrompt"
config.adjust_window_size_when_changing_font_size = false

return config
