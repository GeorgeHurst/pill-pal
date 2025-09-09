from gpiozero import Button
import time
import os, sys

sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

sensor = Button(19)

while True:
    if sensor.is_pressed:
        print(1)
    else:
        print(0)
    time.sleep(0.1)
