#!/bin/bash

# extract temperature from output
extract_temp() {
  "$@" | jq -r '.text' | grep -oP '\d+°C' | grep -oP '\d+'
}

# send notification
send_notification() {
  notify-send -a "Power" -u critical "Temperature" "$1 temperature is $2°C! Please turn on turbo fan"
}

# Check CPU temperature
cpu_temp=$(extract_temp cpuinfo.sh --use amd)

# Check GPU temperature
gpu_temp=$(extract_temp gpuinfo.sh --use amd)

# Check if either CPU or GPU temperature
if [ -n "$cpu_temp" ] && [ "$cpu_temp" -gt 85 ]; then
  send_notification "CPU" "$cpu_temp"
elif [ -n "$gpu_temp" ] && [ "$gpu_temp" -gt 85 ]; then
  send_notification "GPU" "$gpu_temp"
fi

#waybar stuff
# Check cooler boost status
cooler_boost_status=$(cat /sys/devices/platform/msi-ec/cooler_boost)

if [ "$cooler_boost_status" = "off" ]; then
  icon="󰠝"
else
  icon="󰈐"
fi

echo " $icon"