#!/bin/bash
# Disable screen blanking
xset s off
xset -dpms
xset s noblank

# Hide mouse cursor after inactivity
unclutter -idle 0.5 -root &

# Launch Chromium in kiosk mode
chromium-browser --noerrdialogs --disable-infobars --kiosk http://127.0.0.1:5001
