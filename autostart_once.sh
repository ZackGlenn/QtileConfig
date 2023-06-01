#!/bin/bash
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
~/.config/qtile/scripts/auto_lock.sh &
disown

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh &
disown

/usr/lib/polkit-kde-authentication-agent-1 &
disown # start polkit agent from kde
