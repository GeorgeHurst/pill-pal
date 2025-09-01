from gpiozero import Button
import sys, os

sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

pin = 0x1A

button = Button(pin)

while True:
  if sensor.is_pressed:
    print("    pressed")
  else:
    print("unpressed")
