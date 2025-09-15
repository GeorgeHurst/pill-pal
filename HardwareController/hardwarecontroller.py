import requests

from gpiozero import LED, Button, Buzzer
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import board
# from logger import log, error, info
from time import sleep
import sys


sys.path.insert(0, "/home/pi/pill-pal/venv/lib/python3.11/site-packages")

"""
4x servo motors
1x pwm board controller thing
4x leds
4x buttons
4x sensors
1x RTC
"""

I2C = board.I2C()

# PWM Controller
PCA = PCA9685(I2C)

# Buttons
BTN = Button(26) # Physical user input to release dose

# Sensors
SENSORS = [ 
           [ Button(19), Button(23) ],  # Compartment 0
           [ Button(13), Button(24) ],  # Compartment 1
           [ Button(6),  Button(25) ],  # Compartment 2
           [ Button(5),  Button(16) ]   # Compartment 3
        ]

BUZZER = Buzzer(12)

# LEDs
BTN_LED = LED(22)
DOSE_INDICATOR_LED = LED(4) # GREEN
# LATEDOSE_LED = LED(17)      # RED
# led3 = LED(27)
# led4 = LED(22)

# Servos
SERVOS = [    
    servo.Servo(PCA.channels[0], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[1], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[2], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[3], min_pulse=500, max_pulse=2500)
]

servo_test = servo.Servo(PCA.channels[8], min_pulse=500, max_pulse=2500)

# degrees of servo angles
OPEN_ANGLE = 180 
CLOSED_ANGLE = 0

class airlock:   
    
    @staticmethod
    def open(slot):
        SERVOS[slot].angle = OPEN_ANGLE
        #log("AIRLOCK OPEN")
    
    @staticmethod
    def close(slot):
        SERVOS[slot].angle = CLOSED_ANGLE
        #log("AIRLOCK CLOSED")


def go(data):
    # BUZZER.off()
    BTN_LED.off() 

    for slot in data:
        slot_id = int(slot[0])
        amount = int(slot[1:])
        
        for i in range(amount):
            print(f"Dispensing {i+1}/{amount}")

            # airlock.open(slot_id)
            servo_test.angle = OPEN_ANGLE
            SENSORS[slot_id][0].wait_for_press()
            SENSORS[slot_id][0].wait_for_release()
            # airlock.close(slot_id)
            servo_test.angle = CLOSED_ANGLE



# dispense logic
def dispense(data):
    
    # BUZZER.on()
    BTN_LED.on()
    
    BTN.wait_for_press()
    go(data)


print("dispense test")
dispense(["02"])
print("done")
    






