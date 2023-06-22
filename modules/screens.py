from libqtile import qtile, bar
from Xlib import display as xdisplay # this import requires python-xlib to be installed
from modules.widgets import widget, volume
from libqtile.config import Screen
from modules.keys import terminal
import os

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

def make_widgets():
    return [   
        widget.Sep(padding=3, linewidth=0, background="#2f343f"),
            widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
            widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
            widget.GroupBox(
                            highlight_method='line',
                            this_screen_border="#5294e2",
                            this_current_screen_border="#5294e2",
                            active="#ffffff",
                            inactive="#848e96",
                            background="#2f343f"),
            widget.TextBox(
                   text = '',
                   padding = 0,
                   fontsize = 28,
                   foreground='#2f343f'
                   ),    
            widget.Prompt(),
            widget.Spacer(length=5),
            widget.WindowName(foreground='#99c0de',fmt='{}'),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.CurrentLayoutIcon(scale=0.75),
            widget.Systray(icon_size = 20),
            widget.TextBox(
                   text = '',
                   padding = 0,
                   fontsize = 28,
                   foreground='#2f343f'
                   ), 
            volume,
            widget.TextBox(                                                                    
                   text = '',
                   padding = 0,
                   fontsize = 28,
                   foreground='#2f343f',
                   ),   
            widget.TextBox(
                   text = '',
                   padding = 0,
                   fontsize = 28,
                   foreground='#2f343f'
                   ),    
            widget.Clock(format='󰥔 %Y-%m-%d %a %I:%M %p',
                         background="#2f343f",
                         foreground='#9bd689'),
                                            widget.TextBox(                                                
                                            
                   text = '',
                   padding = 0,
                   fontsize = 28,
                   foreground='#2f343f',
                   ),   
            widget.TextBox(
                text=' ',
                mouse_callbacks= {
                    'Button1':
                    lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                },
                foreground='#e39378'
                )
    ]

widgets1 = make_widgets()
widgets2 = [w for w in make_widgets() if not isinstance(w, widget.Systray)]

screens = [
    Screen(
        top=bar.Bar(
            widgets1,
            30,  # height in px
            background="#404552",  # background color
        ),
        wallpaper = "~/Pictures/wallpapers/The Way of Kings.jpg",
        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets2,
            30,  # height in px
            background="#404552",  # background color
        ),
        wallpaper = "~/Pictures/wallpapers/RoW Bulgarian.jpg",
        wallpaper_mode="fill"
    ),
]
