from gpiozero import Button

sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

pin = 0x00011010

button = Button(pin)

while True:
  if sensor.is_pressed:
    print("    pressed")
  else:
    print("unpressed")
