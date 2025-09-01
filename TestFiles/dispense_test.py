import os, sys
sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import board
from gpiozero import Button

import time

I2C = board.I2C()

# PWM Controller
PCA = PCA9685(I2C)
PCA.frequency = 50

# Servos
servos = servo.Servo(PCA.channels[0], min_pulse=500, max_pulse=2500)

# Sensor
sensor = Button(19)


while True:
	servo.angle = 0
	for i in range(90):
		servo.angle = i*2
		time.sleep(0.025)
	time.sleep(0.5)
	while not sensor.is_pressed:
		#wait
		time.sleep(0.01)
	servo.angle = 0
