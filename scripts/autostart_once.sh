#!/bin/bash

# display configuration
autorandr --change >/dev/null

# background processes
picom & # compositor
disown
light-locker & # screen locker
disown
/usr/lib/deja-dup/deja-dup-monitor & # backup system
disown
warpd -f & # mouseless cursor navigation
disown
~/.config/qtile/scripts/check_battery.sh & # low battery checker
disown
/usr/bin/lxpolkit & # start polkit agent from lxde
disown

# background processes with systray entries
keepassxc & # password manager
disown
kdeconnect-indicator & # phone integration
disown
nm-applet & # network manager
disown
cbatticon & # battery indicator
disown
blueman-applet & # bluetooth manager
disown

# X configuration
setxkbmap -option "caps:escape_shifted_capslock"
