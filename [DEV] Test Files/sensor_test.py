from gpiozero import Button
import time

sensor = Button(19)

while True:
    if sensor.is_pressed:
        print(1)
    else:
        print(0)
    time.sleep(0.1)
