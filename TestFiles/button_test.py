from gpiozero import Button, LED
import sys, os
sys.path.insert(0, "/home/pi/pill-pal/venv/lib/python3.11/site-packages")
from adafruit_pca9685 import PCA9685


# sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

buzzer = pca.channels[15]

button = Button(26)
led = LED(22)

while True:
  if button.is_pressed:
    buzzer.frequency = 400
    print("    pressed")
    led.on()
  else:
    buzzer.frequency = 0
    print("unpressed")
    led.off()
