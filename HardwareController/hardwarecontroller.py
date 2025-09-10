import requests

from gpiozero import LED, Button
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import board
from logger import log

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
RELEASE_DOSE = Button(26) # Physical user input to release dose
# button2 = Button(16)
# button3 = Button(12)
# button4 = Button(25)

# Sensors
SENSORS = [ Button(19), Button(13), Button(6), Button(5) ]

# LEDs
DOSE_INDICATOR_LED = LED(4) # GREEN
LATEDOSE_LED = LED(17)      # RED
# led3 = LED(27)
# led4 = LED(22)

# Servos
SERVOS = [    
    servo.Servo(PCA.channels[0], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[1], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[2], min_pulse=500, max_pulse=2500),
    servo.Servo(PCA.channels[3], min_pulse=500, max_pulse=2500)
]



class Airlock:
    def __init__(self, slot):
        self.slot = slot
        
        # degrees of servo angles
        self.OPEN_ANGLE = 0 
        self.CLOSED_ANGLE = 180
    
    def open(self):
        SERVOS[self.slot].angle = self.OPEN_ANGLE
        log("AIRLOCK OPEN")
    
    def close(self):
        SERVOS[self.slot].angle = self.CLOSED_ANGLE
        log("AIRLOCK CLOSED")



# dispense logic
def dispense(slot, amount):
    airlock = Airlock(slot)
    
    for i in range(amount):
        log(f"Dispensing dose {i+1}/{amount} from slot {slot}")
        
        # vibration motor in slot vibrates
        airlock.open()
        while not SENSORS[slot].is_pressed:
            pass
        airlock.close()
    
    pass
    
    