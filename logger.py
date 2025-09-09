from flask import request
from colorama import Fore, Style, init
import inspect
from datetime import datetime

init(autoreset=True)


COLOR_MAP = {
    'hardwareapi': Fore.RED,
    'standaloneapi': Fore.GREEN,
    'pharmacist': Fore.BLUE,
    'app': Fore.YELLOW
}

def log(msg):
    # Get the calling module name
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__.split('.')[-1] if module else 'unknown'
    timestamp = datetime.now().strftime("%H:%M:%S.%f")

    color = COLOR_MAP.get(module_name, Fore.WHITE)
    print(f"{color}[{timestamp}]<{module_name}> {msg}{Style.RESET_ALL}")