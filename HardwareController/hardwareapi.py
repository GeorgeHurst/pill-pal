from flask import Flask, request
from HardwareController.hardwarecontroller import dispense

api = Flask(__name__)

DEFAULT_ROUTE = "/hardwarecontroller/api"

@api.route(DEFAULT_ROUTE+"/dispense", methods=['POST'])
def run():
    # data = request.get_json()
    # dispense()
    
    print("<HardwareControllerAPI> DISPENSING NOW.")
    return { "success" : True}