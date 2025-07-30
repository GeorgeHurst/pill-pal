from UserInterface.Standalone.standaloneapp import *
from .settings import config

if __name__ == "__main__":
    app.run(debug=config["debug"], port=config["standalone_port"], host=config["host"])