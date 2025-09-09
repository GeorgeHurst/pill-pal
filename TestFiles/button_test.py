from gpiozero import Button, LED, Buzzer
import sys, os
sys.path.insert(0, "/home/pi/pill-pal/venv/lib/python3.11/site-packages")


# sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))


buzzer = Buzzer(12)
button = Button(26)
led = LED(22)

while True:
  if button.is_pressed:
    buzzer.on()
    print("    pressed")
    led.on()
  else:
    buzzer.off()
    print("unpressed")
    led.off()
