from libqtile import hook, qtile
import subprocess
import os

qtile_scripts_path = os.path.expanduser('~/.config/qtile/scripts/')

@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtile_scripts_path + 'autostart_once.sh'])

@hook.subscribe.screens_reconfigured
def send_to_second_screen():
    if len(qtile.screens) > 1:
        qtile.groups_map["2"].cmd_toscreen(1, toggle=False)
