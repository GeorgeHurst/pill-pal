from .DataManager.datamanager import DataManager
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_cors import CORS

dm = DataManager()
api = Flask(__name__)
CORS(api)

DEFAULT_ROUTE = "/api"


############### GETTERS ##################################

# Get all of a type
@api.route(DEFAULT_ROUTE+"/get/<type>", methods=['GET'])
def getdata(type):
    return dm.load(type)

@api.route(DEFAULT_ROUTE+"/get/pill/<slot>", methods=['GET'])
def getpill(slot):
    data = dm.load("pills")
    return data[int(slot)] # <- -1 maybe

@api.route(DEFAULT_ROUTE+"/get/backup/<type>", methods=['GET'])
def getbackup(type):
    return dm.load_backup(type)

@api.route(DEFAULT_ROUTE+"/get/config", methods=['GET'])
def getconfig():
    config = dm.get_config()
    if not config:
        return jsonify({'error': 'Configuration not found'}), 404
    return jsonify(config)

##########################################################




############### SETTERS ##################################

@api.route(DEFAULT_ROUTE+"/set/<type>", methods=['POST'])
def setdata(type):
    data = request.get_json()
    return dm.save(type, data)

@api.route(DEFAULT_ROUTE+"/set/pill/<slot>", methods=['POST', 'OPTIONS'])
def setpill(slot):
    if request.method == 'OPTIONS':
        return '', 204
    new_data = request.get_json()
    pill_data = dm.load("pills")
    pill_data[int(slot)] = new_data
    dm.save("pills", pill_data)
    return jsonify({"success": True}), 200



##########################################################




############### MISC #####################################
@api.route(DEFAULT_ROUTE+"/authenticate", methods=['POST'])
def check_passcode():
    data = request.get_json()
    user_passcode = data.get('passcode', '')

    stored_hash = dm.get_passcodehash()

    if check_password_hash(stored_hash, user_passcode):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})
    
##########################################################
