import os
from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"
script_dir = os.path.expanduser('~/.config/qtile/scripts/')

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    old_screen = qtile.screens.index(qtile.current_screen)
    new_screen = (old_screen + 1) % len(qtile.screens)
    group = qtile.screens[new_screen].group.name
    qtile.current_window.togroup(group, switch_group=switch_group)
    if switch_screen:
        qtile.to_screen(new_screen)


def window_to_prev_screen(qtile, switch_group=False, switch_screen=False):
    old_screen = qtile.screens.index(qtile.current_screen)
    new_screen = (old_screen - 1) % len(qtile.screens)
    group = qtile.screens[new_screen].group.name
    qtile.current_window.togroup(group, switch_group=switch_group)
    if switch_screen:
        qtile.to_screen(new_screen)


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "tab",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next screen"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to previous screen"),
    Key([mod, "shift"], "period", lazy.function(window_to_next_screen), desc="Move window to next screen"),
    Key([mod, "shift"], "comma", lazy.function(window_to_prev_screen), desc="Move window to previous screen"),

    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"],
        "l",
        lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod, "control"], "n", lazy.layout.reset(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "tab", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Toggle floating
    Key([mod, "mod1"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),

    # Standard keyboard signals
    Key([], "XF86AudioRaiseVolume", lazy.spawn(script_dir + "changeVolume.sh +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(script_dir + "changeVolume.sh -5%")),



    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86MonBrightnessUp",lazy.spawn(script_dir + "changeBrightness.sh -A 10")),
    Key([], "XF86MonBrightnessDown",lazy.spawn(script_dir + "changeBrightness.sh -U 10")),

    # launch applications
    Key([mod], "b", lazy.spawn("qutebrowser")),
    Key([mod], "n", lazy.spawn("alacritty -e nvim")),
    Key([mod], "e", lazy.spawn("alacritty -e joshuto")),
    Key([mod], "c", lazy.spawn(script_dir + "toggleEarbuds.sh")),
    Key([mod], "x", lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu.sh"))),
    Key([mod, "shift"], "b", lazy.spawn("rofi-bluetooth")),

    # misc
    Key([mod], "d", lazy.spawn("dunstctl close-all"))
]
