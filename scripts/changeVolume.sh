#!/bin/bash
# changeVolume

# Arbitrary but unique message tag
msgTag="myvolume"

# Change the volume using alsa(might differ if you use pulseaudio)
amixer -M -D pulse set Master "$@" >/dev/null

# Query amixer for the current volume and whether or not the speaker is muted
volume="$(amixer -M -D pulse get Master | tail -1 | awk '{print $5}' | sed 's/[^0-9]*//g')"
mute="$(amixer -M -D pulse get Master | tail -1 | awk '{print $7}' | sed 's/[^a-z]*//g')"
if [[ $volume == 0 || "$mute" == "off" ]]; then
	# Show the sound muted notification
	dunstify -a "changeVolume" -u low -i notification-audio-volume-muted -h string:x-dunst-stack-tag:$msgTag "Volume muted"
else
	# Show the volume notification
	dunstify -a "changeVolume" -u low -i notification-audio-volume-high -h string:x-dunst-stack-tag:$msgTag \
		-h int:value:"$volume" "Volume: ${volume}%"
fi

# Play the volume changed sound
canberra-gtk-play -i audio-volume-change -d "changeVolume"
