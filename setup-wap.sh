#!/bin/bash
set -e

WIFI_IFACE="wlan0"
SSID="PillPalAP"
PASSPHRASE="raspberry123"
AP_IP="192.168.4.1"
SUBNET="192.168.4.0"
DHCP_RANGE="192.168.4.10,192.168.4.50,12h"

echo "[1/6] Installing required packages..."
apt update
apt install -y hostapd dnsmasq

echo "[2/6] Stopping services temporarily..."
systemctl stop hostapd
systemctl stop dnsmasq

echo "[3/6] Configuring systemd-networkd for static IP..."
cat >/etc/systemd/network/08-$WIFI_IFACE.network <<EOF
[Match]
Name=$WIFI_IFACE

[Network]
Address=$AP_IP/24
DHCPServer=yes
EOF

systemctl enable systemd-networkd
systemctl restart systemd-networkd

echo "[4/6] Configuring dnsmasq (DHCP)..."
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.backup
cat >/etc/dnsmasq.conf <<EOF
interface=$WIFI_IFACE
dhcp-range=$DHCP_RANGE
domain-needed
bogus-priv
EOF

echo "[5/6] Configuring hostapd (Wi-Fi AP)..."
cat >/etc/hostapd/hostapd.conf <<EOF
interface=$WIFI_IFACE
driver=nl80211
ssid=$SSID
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=$PASSPHRASE
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF

sed -i "s|#DAEMON_CONF=\"\"|DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"|" /etc/default/hostapd

echo "[6/6] Enabling services..."
systemctl unmask hostapd
systemctl enable hostapd dnsmasq
systemctl start hostapd dnsmasq

echo "Setup complete"
echo "AP SSID: $SSID"
echo "Password: $PASSPHRASE"
echo "Static IP: $AP_IP"
