from flask import request
from colorama import Fore, Style, init, Back
import inspect
from datetime import datetime

init(autoreset=True)


COLOR_MAP = {
    'hardwareapi': Back.RED,
    'standaloneapp': Back.GREEN,
    'pharmacist': Back.BLUE,
    'app': Back.YELLOW
}

NAME_MAP = {
    'hardwareapi': "HardwareControllerAPI",
    'standaloneapp': "StandaloneAPP",
    'pharmacist': "PharmacistAPI",
    'app': "OnboardApp"
}

def log(msg):
    # Get the calling module name
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__.split('.')[-1] if module else 'unknown'
    timestamp = datetime.now().strftime("%H:%M:%S.%f")

    color = COLOR_MAP.get(module_name, Fore.WHITE)
    id = NAME_MAP.get(module_name)
    print(f"{color}[{timestamp}] <{id}> {msg}{Style.RESET_ALL}")