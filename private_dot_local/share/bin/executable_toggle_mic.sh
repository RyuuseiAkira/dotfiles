#!/bin/bash

led_device="platform::micmute"  # LED device

# Function to check microphone mute status
is_mic_muted() {
  pamixer --default-source --get-mute | grep -q "false"
}

# Toggle LED based on microphone mute status
if is_mic_muted; then
  brightnessctl -d "$led_device" s 0
else
  brightnessctl -d "$led_device" s 1
fi
