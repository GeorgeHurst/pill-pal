from colorama import Fore, Style, init, Back
import inspect
from datetime import datetime

init(autoreset=True)


COLOR_MAP = {
    'hardwareapi': Back.MAGENTA,
    'standaloneapp': Back.GREEN,
    'pharmacist': Back.BLUE,
    'app': Back.YELLOW
}

NAME_MAP = {
    'hardwareapi': "HardwareAPI",
    'standaloneapp': "StandaloneAPP",
    'pharmacist': "PharmacistAPI",
    'app': "OnboardApp"
}

def log(msg):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__.split('.')[-1] if module else 'unknown'
    timestamp = datetime.now().strftime("%H:%M:%S.%f")

    color = COLOR_MAP.get(module_name, Fore.WHITE)
    id = NAME_MAP.get(module_name)
    print(f"{color}[{timestamp}] <{id}> {msg}{Style.RESET_ALL}")

def error(msg):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__.split('.')[-1] if module else 'unknown'
    timestamp = datetime.now().strftime("%H:%M:%S.%f")

    id = NAME_MAP.get(module_name)
    print(f"{Back.RED}[{timestamp}][ERROR] <{id}> {msg}{Style.RESET_ALL}")
    
def info(msg):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__.split('.')[-1] if module else 'unknown'
    timestamp = datetime.now().strftime("%H:%M:%S.%f")

    id = NAME_MAP.get(module_name)
    print(f"{Back.LIGHTBLACK_EX}[{timestamp}][INFO]  <{id}> {msg}{Style.RESET_ALL}")