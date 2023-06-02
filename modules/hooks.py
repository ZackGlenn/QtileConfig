from libqtile import hook, qtile
from modules.screens import get_num_monitors
import subprocess
import os

qtile_scripts_path = os.path.expanduser('~/.config/qtile/scripts/')

@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtile_scripts_path + 'autostart_once.sh'])

@hook.subscribe.startup
def always_autostart():
    subprocess.call([qtile_scripts_path + 'autostart_always.sh'])

@hook.subscribe.startup_complete
def assign_groups_to_screens():
    if get_num_monitors() > 1:
        qtile.groups_map["2"].cmd_toscreen(1, toggle=False)
    subprocess.call([qtile_scripts_path + 'autostart_after.sh'])
