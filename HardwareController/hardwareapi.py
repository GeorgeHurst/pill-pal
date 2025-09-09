from flask import Flask, request
from HardwareController.hardwarecontroller import dispense

api = Flask(__name__)

DEFAULT_ROUTE = "/hardwarecontroller/api"

@api.route(DEFAULT_ROUTE+"/dispense/<data>", methods=['GET'])
def run(data):
    
    # DATA WILL BE IN URL WITH COMPARTMENT_NUM CONCAT WITH QUANTITY
    
    # string[0] = compartment number
    # string[1:] = quantity
    
    print(f"<HardwareControllerAPI> dispensing {data[1:]} pills in compartment {data[0]}")
    
    # data = request.get_json()
    # dispense()
    
    return { "compartment" : data[0],
             "quantity" : data[1:]
           }