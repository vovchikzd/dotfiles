-- See https://wiki.hyprland.org/Configuring/Window-Rules/

local rule = hl.window_rule

local suppressMaximizeRule = rule({
    -- Ignore maximize requests from all apps. You'll probably like this.
    name  = "suppress-maximize-events",
    match = { class = ".*" },

    suppress_event = "maximize",
})

rule({
  name = "mpv-rule"
  , match = {
    class = "mpv"
  }
  , float = true
  , keep_aspect_ratio = true
  , center = true
})

rule({
  name = "picture-in-picture-from-browser"
  , match = {
    class = "(firefox|zen|Tor Browser)"
    , title = "(Picture-in-Picture)"
  }
  , pin = true
  , float = true
  , rounding = 0
  , size = { 608, 342 }
  , move = { 1300, 726 }
  , no_initial_focus = true
  , keep_aspect_ratio = true
})

rule({
  match = {
    class = "(firefox|zen)"
    , initial_title = "negative:(Mozilla Firefox( Private Browsing)?|Zen Browser)"
  }
  , float = true
  , center = true
  , persistent_size = true
})

rule({
  name = "keepass-rule"
  , match = {
    class = "(org.keepassxc.KeePassXC)"
  }
  , size = { 966, 631 }
  , center = true
  , float = true
})

rule({
  name = "pavucontrol-rule"
  , match = {
    class = "(pavucontrol-qt)"
  }
  , move = { 983, 42 }
  , size = { 466, 534 }
  , float = true
  , pin = true
})

rule({
  name = "libreoffice-popup-windows-rule"
  , match = {
    class = "(libreoffice-startcenter)"
    , title = "(Save|Export)"
  }
  , float = true
  , center = true
  , persistent_size = true
})

rule({
  name = "kdiskfree-rule"
  , match = {
    class = "(org.kde.kdf)"
    , title = "(KDiskFree)"
  }
  , size = { 960, 518 }
  , float = true
  , center = true
})

rule({
  name = "obs-rule"
  , match = {
    class = "(com.obsproject.Studio)"
    , title = "(Scripts)"
  }
  , size = { 988, 636 }
  , float = true
  , center = true
})

rule({
  name = "qbittorrent-rule"
  , match = {
    class = "org.qbittorrent.qBittorrent"
    , title = "negative:(qBittorrent v.*)"
  }
  , float = true
  , center = true
  , persistent_size = true
})

rule({
  name = "flameshot-rule"
  , match = {
    class = "flameshot"
  }
  , fullscreen_state = "0"
  , float = true
  , size = { 3840, 1080 }
  , move = { 0, 0 }
  , rounding = 0
  , no_anim = true
  , pin = true
})

rule({
  name = "xdg-desktop-portal-gtk-rule"
  , match = {
    class = "xdg-desktop-portal-gtk"
  }
  , float = true
  , center = true
  , size = { 1250, 665 }
})

rule({
  name = "dbeaver-popup-rules"
  , match = {
    class = "DBeaver"
    , title = "(Properties.*)|(Preferences.*)"
  }
  , size = { 1175, 735 }
  , center = true
})

rule({
  name = "dbeaver-no-popup-rules"
  , match = {
    class = "DBeaver"
    , title = "negative:(DBeaver \\d+.*)|(Properties.*)|(Preferences.*)"
  }
  , float = true
  , size = { 611, 188 }
  , center = true
})

rule({
  name = "steam-games-rule"
  , match = {
    class = "(steam_.*)"
  }
  , rounding = 0
  , fullscreen = true
  , pin = true
  , border_size = 0
})

rule({
  name = "steam-popups-rule"
  , match = {
    class = "steam"
    , initial_title = "negative:(Steam)"
  }
  , float = true
  , center = true
  , persistent_size = true
})

rule({
  name = "sowon-rule"
  , match = {
    title = "(.*sowon.*)"
  }
  , float = true
  , center = true
  , persistent_size = true
})
