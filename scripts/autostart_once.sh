#!/bin/bash
autorandr --change &
picom &
disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed
kdeconnect-indicator &
disown
keepassxc &
disown
nm-applet &
disown
cbatticon &
disown
blueman-applet &
disown
light-locker &
disown
/usr/lib/deja-dup/deja-dup-monitor &
disown
warpd -f &
disown

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh &
disown

/usr/bin/lxpolkit &
disown # start polkit agent from lxde

setxkbmap -option "caps:escape_shifted_capslock"
