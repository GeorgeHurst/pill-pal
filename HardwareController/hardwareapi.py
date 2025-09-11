from flask import Flask, request
from HardwareController.hardwarecontroller import dispense
from logger import log, info

api = Flask(__name__)

DEFAULT_ROUTE = "/hardwarecontroller/api"

@api.route(DEFAULT_ROUTE+"/dispense/<data>", methods=['GET'])
def run(data):
    
    schedule = data.split("-")
    
    dispense(schedule)
    
    log(f" Dose has finished dispensing")
    return { 
            "status" : "finished"
           }