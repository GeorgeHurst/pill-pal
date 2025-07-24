from Pharmacist.pharmacist import *
from .settings import pharmacist_port, debug

if __name__ == "__main__":
    api.run(debug=debug, port=pharmacist_port)