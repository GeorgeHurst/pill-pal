import sys
import os

sys.path.append(os.path.abspath("venv/lib/python3.11/site-packages"))

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import board

import time

I2C = board.I2C()

# PWM Controller
PCA = PCA9685(I2C)
PCA.frequency = 50

# Servos
servos = [
    servo.Servo(PCA.channels[0], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[1], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[2], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[3], min_pulse=500, max_pulse=2500)
]

print("====STARTING TEST====")
for i in range(10):
    for servo in servos:
        servo.angle = 0
        time.sleep(1)
        servo.angle = 90
        time.sleep(1)
        servo.angle = 180
        time.sleep(1)
        servo.angle = 0
        time.sleep(1)
print("====ENDING TEST====")
