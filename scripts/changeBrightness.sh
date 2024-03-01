#!/bin/bash
# changeBrightness

# Arbitrary but unique message tag
msgTag="mybrightness"

# Change the brightness using light
brightnessctl set "$@" >/dev/null

# Query light for the current brightness
brightness="$((100 * $(brightnessctl get) / 4285))"

# Show the brightness notification
dunstify -a "changeBrightness" -u low -h string:x-dunst-stack-tag:$msgTag \
	-h int:value:"$brightness" "Brightness: ${brightness}%"
