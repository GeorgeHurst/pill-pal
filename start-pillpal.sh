#!/bin/bash
# Wait a few seconds for networking / X
sleep 10

# 1. Run the AP setup
/bin/bash /home/pi/pill-pal/setup-wap.sh

# 2. Activate venv and run threader.py in background
source /home/pi/venv/bin/activate
nohup python3 /home/pi/threader.py >/home/pi/threader.log 2>&1 &

# 3. Wait until server responds
until curl -s http://127.0.0.1:5001 >/dev/null; do sleep 1; done

# 4. Start kiosk
/bin/bash /home/pi/pill-pal/start.sh
