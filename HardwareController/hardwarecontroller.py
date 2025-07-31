import requests

from gpiozero import LED, Button, LineSensor
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
# import board

# from .ServerManagers.settings import config


schedule = requests.get(f'http://127.0.0.1:5000/api/get/schedule')
print(schedule.json())


"""
4x servo motors
1x pwm board controller thing
4x leds
4x buttons
4x sensors
1x RTC
"""

# I2C = board.I2C()

# # PWM Controller
# PCA_CONTROLLER = PCA9685(I2C)

# # Buttons
# RELEASE_DOSE = Button(26) # Physical user input to release dose
# button2 = Button(16)
# button3 = Button(12)
# button4 = Button(25)

# # Sensors
# COMPARTMENT_SENSOR1 = LineSensor(19)
# COMPARTMENT_SENSOR2 = LineSensor(13)
# COMPARTMENT_SENSOR3 = LineSensor(6)
# COMPARTMENT_SENSOR4 = LineSensor(5)

# # LEDs
# DOSE_INDICATOR_LED = LED(4) # GREEN
# LATEDOSE_LED = LED(17) # RED
# led3 = LED(27)
# led4 = LED(22)

# # Servos
# COMPARTMENT_SERVO1 = servo.Servo(PCA_CONTROLLER.channels[0])
# COMPARTMENT_SERVO2 = servo.Servo(PCA_CONTROLLER.channels[1])
# COMPARTMENT_SERVO3 = servo.Servo(PCA_CONTROLLER.channels[2])
# COMPARTMENT_SERVO4 = servo.Servo(PCA_CONTROLLER.channels[3])