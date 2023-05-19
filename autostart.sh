#!/bin/bash
xrandr --output HDMI1 --right-of eDP1
nitrogen --restore
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
picom &
disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh &
disown

# Start welcome
eos-welcome &
disown

/usr/lib/polkit-kde-authentication-agent-1 &
disown # start polkit agent from kde
