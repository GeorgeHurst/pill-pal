#!/bin/bash
set -e

USER="pi"
URL="http://127.0.0.1:5001"

echo "[1/3] Installing Chromium..."
apt update
apt install -y chromium-browser xserver-xorg x11-xserver-utils xinit openbox unclutter

echo "[2/3] Creating kiosk start script..."
mkdir -p /home/$USER/.config/kiosk
cat >/home/$USER/.config/kiosk/start.sh <<EOF
#!/bin/bash
# Disable screen blanking
xset s off
xset -dpms
xset s noblank

# Hide mouse cursor after inactivity
unclutter -idle 0.5 -root &

# Launch Chromium in kiosk mode
chromium-browser --noerrdialogs --disable-infobars --kiosk $URL
EOF

chmod +x /home/$USER/.config/kiosk/start.sh
chown -R $USER:$USER /home/$USER/.config/kiosk

echo "[3/3] Creating systemd service (manual start only)..."
cat >/etc/systemd/system/kiosk.service <<EOF
[Unit]
Description=Chromium Kiosk (manual start)
After=systemd-user-sessions.service network.target

[Service]
User=$USER
Environment=XAUTHORITY=/home/$USER/.Xauthority
Environment=DISPLAY=:0
ExecStart=/home/$USER/.config/kiosk/start.sh
Restart=always
RestartSec=5

[Install]
WantedBy=graphical.target
EOF

systemctl daemon-reload

echo "Kiosk mode installed."
echo "Start with:   sudo systemctl start kiosk"
echo "Stop with:    sudo systemctl stop kiosk"
echo "If you ever want it to auto-start at boot, run: sudo systemctl enable kiosk"
