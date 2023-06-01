#!/bin/bash

xidlehook \
	--not-when-fullscreen \
	--not-when-audio \
	--timer 300 \
	'light -S 10' \
	'light -S 100' \
	--timer 60 \
	'light -S 100; slock' \
	'' \
	--timer 3600 \
	'systemctl suspend' \
	''
