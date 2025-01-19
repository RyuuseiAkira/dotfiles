#!/bin/bash

cooler_boost_status=$(cat /sys/devices/platform/msi-ec/cooler_boost)

if [ "$cooler_boost_status" = "off" ]; then
  icon="󰠝"  # Replace with your desired "off" icon
else
  icon="󰈐"  # Replace with your desired "on" icon
fi

echo " $icon"