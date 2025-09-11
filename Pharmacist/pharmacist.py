from .DataManager.datamanager import DataManager
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_cors import CORS
from datetime import datetime
import os, requests, sys
from time import sleep
from logger import log, error, info

sys.path.insert(0, "/home/pi/pill-pal/venv/lib/python3.11/site-packages")

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
    dm.save(type, data)
    log(f"Data of type {type} saved.")
    return {"success" : True}

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
    
@api.route(DEFAULT_ROUTE+"/remove/pill/<slot_id>", methods=['POST'])
def remove_from_slot(slot_id):
    pill_data = dm.load("pills")
    pill_data[int(slot_id)] = {}
    dm.save("pills", pill_data)
    return jsonify({"success": True}), 200
##########################################################


@api.route(DEFAULT_ROUTE+"/request/dispense", methods=['GET'])
def request_dispense():
    data = {}
    sch = dm.load("schedule")

    time = datetime.now().strftime("%H:%M")
    # time = "09:30"
    
    for slot in sch:
        if slot["time"] == time:
            data = slot["pills"]

    if data == {}:
        info("No pills to dispense")
        return { "failed" : "No pills to dispense"}
    
    dose = ""
    for slot in data:
        if slot["id"] == "3":
            addon = ""
        else:
            addon = "-"
        dose += slot["id"] + slot["amount"] + addon
        
        
    log(f"Request sent to HardwareAPI to dispense {time} dose. ({dose})")
    
    requests.get(
        url=f"http://127.0.0.1:5003/hardwarecontroller/api/dispense/{dose}"
    )

    sleep(1)
     
     
    
    

    return { "success" : True }

