#!/bin/bash
# changeVolume

# Arbitrary but unique message tag
msgTag="myvolume"

# Change the volume using alsa(might differ if you use pulseaudio)
pactl set-sink-volume @DEFAULT_SINK@ "$@"

# Query amixer for the current volume and whether or not the speaker is muted
volume="$(pactl get-sink-volume @DEFAULT_SINK@ | head -1 | awk '{print $5}')"
mute="$(pactl get-sink-mute @DEFAULT_SINK@ | awk '{print $2}')"
if [[ $volume == "0%" || "$mute" == "yes" ]]; then
	# Show the sound muted notification
	dunstify -a "changeVolume" -u low -i notification-audio-volume-muted -h string:x-dunst-stack-tag:$msgTag "Volume muted"
else
	# Show the volume notification
	dunstify -a "changeVolume" -u low -i notification-audio-volume-high -h string:x-dunst-stack-tag:$msgTag \
		-h int:value:"$volume" "Volume: ${volume}"
fi
