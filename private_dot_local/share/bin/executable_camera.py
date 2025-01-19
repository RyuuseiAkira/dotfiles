import subprocess
import time

def check_webcam_status():
  """Checks the webcam status by reading a specific file.

  Returns:
    bool: True if webcam is on, False otherwise.
  """
  with open('/sys/devices/platform/msi-ec/webcam', 'r') as f:
    webcam_status = f.read().strip()
  return webcam_status == 'on'

def main():
  blink_script = '/home/akira/.local/share/bin/led_blink.sh'  # Replace with the actual path to your script
  while True:
    if check_webcam_status():
      subprocess.run([blink_script, 'start'])
    else:
      subprocess.run([blink_script, 'stop'])
    time.sleep(5)  # Adjust the polling interval as needed

if __name__ == '__main__':
  main()