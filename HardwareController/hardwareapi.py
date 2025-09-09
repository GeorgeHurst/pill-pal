from flask import flask, request
from hardwarecontroller import dispense

api = Flask(__name__)

DEFAULT_ROUTE = "/hardwarecontroller/api"

@api.route(DEFAULT_ROUTE+"/dispense", methods=['POST'])
def run():
    data = request.get_json()
    dispense()