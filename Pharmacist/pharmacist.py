from .DataManager.datamanager import DataManager
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_cors import CORS

dm = DataManager()
api = Flask(__name__)
CORS(api)

DEFAULT_ROUTE = "/api"

@api.route(DEFAULT_ROUTE+"/get/<type>", methods=['GET'])
def getdata(type):
    return dm.load(type)

@api.route(DEFAULT_ROUTE+"/set/<type>", methods=['POST'])
def setdata(type, data):
    return dm.save(type, data)

@api.route(DEFAULT_ROUTE+"/get/backup/<type>", methods=['GET'])
def getbackup(type):
    return dm.load_backup(type)

@api.route(DEFAULT_ROUTE+"/authenticate", methods=['POST'])
def check_passcode():
    data = request.get_json()
    user_passcode = data.get('passcode', '')

    stored_hash = dm.get_passcodehash()

    if check_password_hash(stored_hash, user_passcode):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})