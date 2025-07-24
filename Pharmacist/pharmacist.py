from .DataManager.datamanager import DataManager
from flask import Flask

dm = DataManager()
api = Flask(__name__)

DEFAULT_ROUTE = "/api"

@api.route(DEFAULT_ROUTE+"/get/<type>", methods=['GET'])
def getdata(type):
    return dm.load(type)

@api.route(DEFAULT_ROUTE+"/set/<type>", methods=['POST'])
def setdata(type, data):
    return dm.save(type, data)

