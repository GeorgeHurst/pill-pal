from UserInterface.app import *
from .settings import ui_port, debug, host

if __name__ == "__main__":
    app.run(debug=debug, port=ui_port, host=host)