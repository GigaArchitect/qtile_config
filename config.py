# -*- coding: utf-8 -*-
import os
import socket
import subprocess

from libqtile.backend.wayland.inputs import InputConfig
from libqtile.config import Screen
from libqtile import bar, hook, layout
from libqtile.dgroups import simple_key_binder
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from qtile_extras import widget

mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myBrowser = "google-chrome-stable"  # My browser of choice

keys = [
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Launches My Terminal"),
    Key(
        [],
        "Print",
        lazy.spawn(
            ["sh", "-c", 'scrot -F /home/cyberman/Pictures/Screenshots/"$(date)".png']
        ),
        desc="Launches My Terminal",
    ),
    Key(
        [mod],
        "f12",
        lazy.spawn("pamixer -i 5"),
        desc="Launches My Terminal",
    ),
    Key(
        [mod],
        "f11",
        lazy.spawn("pamixer -d 5"),
        desc="Launches My Terminal",
    ),
    Key([mod], "f10", lazy.spawn("light -A 5"), desc="Increase Brightness"),
    Key(
        [mod],
        "f9",
        lazy.spawn("light -U 5"),
        desc="Decrease Brightness",
    ),
    Key([mod], "p", lazy.spawn("i3lock -B 10")),
    ### The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launches My Terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun -show-icons"), desc="Run Launcher"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Qutebrowser"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Restart Qtile"),
    Key([mod, "shift"], "c", lazy.shutdown(), desc="Shutdown Qtile"),
    ### Switch focus to specific monitor (out of three)
    Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    Key([mod], "r", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),
    ### Switch focus of monitors
    Key([mod], "period", lazy.screen.next_group(), desc="Move focus to next group"),
    Key([mod], "comma", lazy.screen.prev_group(), desc="Move focus to prev group"),
    ### Treetab controls
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.move_left(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.move_right(),
        desc="Move down a section in treetab",
    ),
    ### Window controls
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout="treetab"),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout="treetab"),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.shrink_main().when(layout="monadtall"),
        # lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "Up",
        # lazy.layout.grow_main().when(layout="monadtall"),
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key(
        [mod],
        "Down",
        # lazy.layout.shrink_main().when(layout="monadtall"),
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.grow_main().when(layout="monadtall"),
        # lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(["mod1"], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard()),
]

groups = [
    Group("1", layout="monadtall"),
    Group("2", layout="monadtall"),
    Group("3", layout="monadtall"),
    Group("4", layout="monadtall"),
    Group("5", layout="monadtall"),
    Group("6", layout="monadtall"),
    Group("7", layout="monadtall"),
    Group("8", layout="monadtall"),
    Group("9", layout="monadtall"),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group

dgroups_key_binder = simple_key_binder(mod)

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "018ab7",
    "border_normal": "1D2330",
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=14,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=12,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
    ),
    layout.Floating(**layout_theme),
]

colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"],
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Iosevka Nerd Font Bold",
    fontsize=18,
    align="center",
    padding=0,
    background=colors[2],
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font="Iosevka Nerd Font Bold",
            fontsize=16,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            hide_unused=True,
            active="eff0f7",  # colors[2],
            inactive="77787b",  # colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="474747",
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0], padding=5),
        widget.Spacer(foreground="eff0f7", background=colors[0], padding=0),
        widget.Clock(
            foreground="92bbfc",  # colors[6],
            background=colors[0],
            format="%a, %b %d - %I:%M %p ",
        ),
        widget.Spacer(foreground="eff0f7", background=colors[0]),
        widget.Systray(background=colors[0], padding=10, icon_size = 20),  # Added padding for Systray
        widget.Sep(
            foreground=colors[2], background=colors[0], padding=25, size_percent=60
        ),
        widget.PulseVolume(
            fmt="Vol:{}",
            foreground=colors[2],
            background=colors[0],
            channel="Master",
            update_interval=0.1,
            step=0,
            scroll=False,
            scroll_step=0,
        ),
        widget.Sep(
            foreground=colors[2], background=colors[0], padding=25, size_percent=60
        ),
        widget.Backlight(
            backlight_name="intel_backlight",
            background=colors[0],
            fmt="BRIGHT:{}",
        ),
        widget.Sep(
            foreground=colors[2], background=colors[0], padding=25, size_percent=60
        ),
        widget.UPowerWidget(background=colors[0], format="{percent:2.0%}"),
        widget.Sep(
            foreground=colors[2], background=colors[0], padding=25, size_percent=60
        ),
        widget.KeyboardLayout(
            foreground="eff0f7",  # colors[8],
            margin=15,  # Increased margin for more space
            background=colors[0],
            display_map={"ara digits": "AR", "us": "EN"},
            configured_keyboards=["us", "ara digits"],
            fmt="{} ",
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # del widgets_screen1[
    #     9:10
    # ]  # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                opacity=1.0,
                size=24,
                margin=[5, 8, 0, 8],
            )
        ),
        # Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
        # Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    # widgets_screen1 = init_widgets_screen1()
    # widgets_screen2 = init_widgets_screen2()




mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),  # tastyworks exit box
        Match(title="Qalculate!"),  # qalculate-gtk
        Match(wm_class="kdenlive"),  # kdenlive
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
        Match(wm_class="goldendict"),
    ]
)

follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
floats_kept_above = True
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

@hook.subscribe.client_managed
def center_specific_windows(window):
    if window.window.get_wm_class()[0] in ["goldendict", "mpv"]:
        window.center()

def bring_floating_to_front(qtile):
    """
    Bring all floating windows of the current group to the front
    """
    for window in qtile.current_group.windows:
        if window.floating:
            window.bring_to_front()

keys.append(Key([mod], "s", lazy.function(bring_floating_to_front), desc="Bring floating windows to the front"))

wl_input_rules = {
    "type:touchpad": InputConfig(
        tap=True,                 # The settings you care most about
        natural_scroll=True,
        pointer_accel=0.5,
        dwt=True
    )
}

# wl_output_rules = {
#     "eDP-1": OutputConfig(  # Replace "eDP-1" with your display name
#         scale=1.5,         # Scaling factor (1.0 is 100%, 2.0 is 200%, etc.)
#         mode="1920x1080@60",  # Optional: Set resolution and refresh rate
#     ),
#     "*": OutputConfig(     # Default for all other outputs
#         scale=1.0,
#     ),
# }
#
wmname = "LG3D"
