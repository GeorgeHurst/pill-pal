from flask import Flask, request
# from HardwareController.hardwarecontroller import dispense
from logger import log

api = Flask(__name__)

DEFAULT_ROUTE = "/hardwarecontroller/api"

@api.route(DEFAULT_ROUTE+"/dispense/<data>", methods=['GET'])
def run(data):
    
    # DATA WILL BE IN URL WITH COMPARTMENT_NUM CONCAT WITH QUANTITY
    
    # string[0] = compartment number
    # string[1:] = quantity
    slot = data[0]
    amount = data[1:]
    
    log(f"Dispensing {amount} pills in compartment {slot}")
    
    # dispense()
    
    log(f"Slot {slot} has finished dispensing")
    return { 
            "compartment" : slot,
            "quantity" : amount
           }