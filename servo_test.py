import os, sys
sys.path.append(os.path.abspath('venv/lib/python3.11/site-packages'))

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

print("#### START ####")

# for i in range(10):
#     for servo in servos:
#         servo.angle = 0
#         time.sleep(1)
#         servo.angle = 90
#         time.sleep(1)
#         servo.angle = 180
#         time.sleep(1)
#         servo.angle = 0
#         time.sleep(1)

#for i in range(3):
#    for i in range(180):
#        for servo in servos:
#            servo.angle = i
#        time.sleep(0.5)

sleep = 0.2
#for i in range(10):
#	servos[3].angle = 0 
#	time.sleep(sleep)
#	servos[3].angle = 180
#	time.sleep(sleep)

#0 = closed, 180 = open
while True:
	servos[3].angle = 0
	for i in range(90):
		servos[3].angle = i*2
		time.sleep(0.025)
	time.sleep(0.5)
	servos[3].angle = 0

print("#### FINISHED ####")
