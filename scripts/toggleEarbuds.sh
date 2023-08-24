#!/bin/bash

# Toggle connection to galaxy earbuds and capture any output
msg=$(bluetoggle -d 1 -a C4:5D:83:C5:9A:EF 2>&1)

# If there is output, there was an error which should be reported
if not [ "$msg" = "" ]; then dunstify -a "toggleEarbuds" -u low "$msg"; fi
