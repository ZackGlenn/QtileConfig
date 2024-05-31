from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import keys, mod

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"],
        #     i.name,
        #     lazy.window.togroup(i.name, switch_group=True),
        #     desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

keys.extend([
    Key([mod], "y", lazy.group["1"].toscreen(), desc = "Switch to group 1"),
    Key([mod], "u", lazy.group["2"].toscreen(), desc = "Switch to group 2"),
    Key([mod], "i", lazy.group["3"].toscreen(), desc = "Switch to group 3"),
    Key([mod], "o", lazy.group["4"].toscreen(), desc = "Switch to group 4"),
    Key([mod], "p", lazy.group["5"].toscreen(), desc = "Switch to group 5"),

    Key([mod, "shift"], "y", lazy.window.togroup("1"), desc = "Move focused window to group 1"),
    Key([mod, "shift"], "u", lazy.window.togroup("2"), desc = "Move focused window to group 2"),
    Key([mod, "shift"], "i", lazy.window.togroup("3"), desc = "Move focused window to group 3"),
    Key([mod, "shift"], "o", lazy.window.togroup("4"), desc = "Move focused window to group 4"),
    Key([mod, "shift"], "p", lazy.window.togroup("5"), desc = "Move focused window to group 5"),

    Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
])
