from libqtile import hook
import subprocess
import os

qtile_path = os.path.expanduser('~/.config/qtile/')

@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtile_path + 'autostart_once.sh'])

@hook.subscribe.startup
def always_autostart():
    subprocess.call([qtile_path + 'autostart_always.sh'])
