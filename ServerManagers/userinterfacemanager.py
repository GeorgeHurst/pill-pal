from UserInterface.app import *
from .settings import config

if __name__ == "__main__":
    app.run(debug=config["debug"], port=config["ui_port"], host=config["host"])