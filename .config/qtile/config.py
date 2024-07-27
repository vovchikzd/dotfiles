from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

terminal: str = "/home/vovchik/dotfiles/.config/qtile/script.sh"

alt = "mod1"
# caps = "mod2" # num lock ????
super = "mod4"
control = "control"
shift = "shift"
caps = "lock"
enter = "Return"
space = "space"
period = "period"
tab = "Tab"

wallpaper = "/home/vovchik/dotfiles/wallpaper.jpg"

browser = "/usr/bin/firefox"
telegram = "/usr/bin/telegram-desktop"

keys = [
    # Layout manipulation
    Key([super], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([super], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([super], "j", lazy.layout.down(), desc="Move focus down"),
    Key([super], "k", lazy.layout.up(), desc="Move focus up"),
    Key([super], space, lazy.layout.next(), desc="Move window focus to next window"),
    Key([super, alt], space, lazy.layout.previous(), desc="Move window focus to previous window"),

    Key([super, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([super, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([super, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([super, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([super], "i", lazy.layout.grow(), desc="Grow window"),
    Key([super], "m", lazy.layout.shrink(), desc="Shrink window"),
    Key([super], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    Key([super, shift], "space", lazy.layout.flip(), desc="Flip windows"),

    Key([super], tab, lazy.next_layout(), desc="Toggle between layouts"),
    Key([super], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [super]
        , "f"
        , lazy.window.toggle_fullscreen() , desc="Toggle fullscreen on the focused window"
    ),
    Key(
        [super, shift]
        , "f"
        , lazy.window.toggle_floating()
        , desc="Toggle floating on the focused window"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [super, shift],
        enter,
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # App Launch
    Key([super], enter, lazy.spawn(terminal), desc="Launch terminal"),
    Key([super], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([super], "t", lazy.spawn(telegram), desc="Launch telegram"),
    Key([alt], space, lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([shift, alt], "b", lazy.spawn("/usr/bin/obs"), desc="Launch obs-studio"),
    Key([super], "v", lazy.spawn("/usr/bin/librewolf"), desc="Launch LibreWorl"),

    # Config manipulation
    Key([super, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([super, control, shift], "r", lazy.restart(), desc="Restart Qtile"),

    Key([super, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [

            Key(
                [super],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),

            Key(
                [super, shift],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),

            Key(
                [super, control],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"Move focused window to group {i.name}",
            ),
        ]
    )

layouts = [
    layout.MonadTall(
        margin = 7
        , border_width = 2
    ),

    layout.Max(
        margin = 7
        , border_width = 2
    ),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

keyboard_layouts = widget.KeyboardLayout(
                    configured_keyboards = ['us', 'ru']
                    , display_map = {'us': 'en', 'ru': 'ru'}
)

keys.extend([
    Key([super], period, lazy.next_screen(), desc="Switch to next screen"),
    Key([alt, shift], space, lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
])


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                widget.CurrentScreen(),
                keyboard_layouts,
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowTabs(),
                widget.Bluetooth(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Memory(),
                widget.StatusNotifier(),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper = wallpaper,
        wallpaper_mode = "fill"
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                widget.CurrentScreen(),
                keyboard_layouts,
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowTabs(),
                widget.Bluetooth(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.Memory(),
                widget.StatusNotifier(),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper = wallpaper,
        wallpaper_mode = "fill"
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([super], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="mpv"),
        Match(wm_class="dolphin")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
