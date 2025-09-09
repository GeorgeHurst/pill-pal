from HardwareController.hardwarecontroller import *
from .settings import config

if __name__ == "__main__":
    api.run(debug=config["debug"], port=config["hardware_port"], host=config["host"])