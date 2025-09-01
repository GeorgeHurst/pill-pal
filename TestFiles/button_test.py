from gpiozero import Button, LED
import sys, os

sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))



button = Button(26)
led = LED(22)

while True:
  if button.is_pressed:
    print("    pressed")
    led.on()
  else:
    print("unpressed")
    led.off()
