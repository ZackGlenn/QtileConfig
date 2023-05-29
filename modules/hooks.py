from libqtile import hook, qtile
import subprocess
import os

qtile_path = os.path.expanduser('~/.config/qtile/')

@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtile_path + 'autostart_once.sh'])

@hook.subscribe.startup
def always_autostart():
    subprocess.call([qtile_path + 'autostart_always.sh'])

@hook.subscribe.startup_complete
def assign_groups_to_screens():
    qtile.groups_map["2"].cmd_toscreen(1, toggle=False)
