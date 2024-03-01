#!/bin/bash
# changeBrightness

# Arbitrary but unique message tag
msgTag="mybrightness"

# Maximum panel brightness, for computing percentage
maxBrightness="4285"

# Change the brightness using light
brightnessctl set "$@" >/dev/null

# Query light for the current brightness
brightness="$((100 * $(brightnessctl get) / maxBrightness))"

# Show the brightness notification
dunstify -a "changeBrightness" -u low -h string:x-dunst-stack-tag:$msgTag \
	-h int:value:"$brightness" "Brightness: ${brightness}%"
