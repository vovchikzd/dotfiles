-----------------------------
--- ENVIRONMENT VARIABLES ---
-----------------------------

-- https://wiki.hypr.land/Configuring/Advanced-and-Cool/Environment-variables/

local env = hl.env
local home = os.getenv("HOME") or "/home/vovchik"
local xdg_config_home = home .. "/.config"
local env_pairs = {
  XCURSOR_SIZE = "24"
  , HYPRCURSOR_SIZE = "24"
  , GDK_BACKEND = "wayland,x11,*"
  , QT_QPA_PLATFORM = "wayland;xcb"
  , QT_AUTO_SCREEN_SCALE_FACTOR = "1"
  , QT_WAYLAND_DISABLE_WINDOWDECORATION = "1"
  , QT_QPA_PLATFORMTHEME = "qt6ct"
  , SDL_VIDEODRIVER = "wayland"
  , CLUTTER_BACKEND = "wayland"
  , XDG_CURRENT_DESKTOP = "Hyprland"
  , XDG_SESSION_TYPE = "wayland"
  , XDG_SESSION_DESKTOP = "Hyprland"
  , GTK_USE_PORTAL = "1"
  , MOZ_ENABLE_WAYLAND = "1"
  , SAL_USE_VCLPLUGIN = "qt6"
  , CMAKE_GENERATOR = "Ninja"
  , CMAKE_EXPORT_COMPILE_COMMANDS = "On"
  , MANPAGER = "nvim -c Man! -c 'set nomodifiable' -"
  , GTK_CSD = "0"
  , GTK_USE_CSD = "0"
  , GTK_THEME = "Adwaita:dark"
  , LIBADWAITA_FORCE_DARK = "1"
  , XDG_CONFIG_HOME = xdg_config_home
  , XDG_DATA_HOME = home .. "/.local/share"
  , XDG_STATE_HOME = home .. "/.local/state"
  , XDG_CACHE_HOME = home .. "/.cache"
  , RIPGREP_CONFIG_PATH = xdg_config_home .. "/ripgrep.conf"
  , BROWSER = "firefox"
  , EDITOR = "nvim"
  , CROC_SECRET = "yt-dlp-to-phone"
}

for key, value in pairs(env_pairs) do
  env(key, value)
end
