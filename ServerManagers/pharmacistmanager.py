from Pharmacist.pharmacist import *
from .settings import config

if __name__ == "__main__":
    api.run(debug=config["debug"], port=config["pharmacist_port"], host=config["host"])