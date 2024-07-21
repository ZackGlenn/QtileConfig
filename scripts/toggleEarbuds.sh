#!/bin/bash

# Toggle connection to galaxy earbuds and capture any output
msg=$(bluetoggle -d 1 -a DC:69:E2:23:CA:6F 2>&1)

# If there is output, there was an error which should be reported
if not [ "$msg" = "" ]; then dunstify -a "toggleEarbuds" -u low "$msg"; fi
