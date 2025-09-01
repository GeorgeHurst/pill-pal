import sys
import os

import time

sys.path.append(os.path.abspath("Python_PCA9685/src"))

from PCA9685_smbus2 import PCA9685

pwm = PCA9685.PCA9685(interface=1)
pwm.set_pwm_freq(50)
pwm.set_pwm(0,0,102)

time.sleep(1)

pwm.set_pwm(0,0,512)

time.sleep(1)

pwm.set_pwm(0,0,307)

time.sleep(1)
