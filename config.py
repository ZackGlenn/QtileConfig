from modules.keys import keys, mod                      # pyright: ignore
from modules.groups import groups                       # pyright: ignore
from modules.layouts import layouts, floating_layout    # pyright: ignore
from modules.mouse import mouse                         # pyright: ignore
from modules.hooks import *                             # pyright: ignore
import os                                               # pyright: ignore
from modules.screens import screens                     # pyright: ignore

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
floats_kept_above = True
widget_defaults = dict(
        font='Cascadia Code',
        fontsize=13,
        padding=3
)
