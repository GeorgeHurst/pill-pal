import json, os
from ServerManagers.settings import config

class DataManager:
    def __init__(self):
        self.FILE_PATH = "Data/Tables"
    
    # Retrieve data from the desired table from data store
    def load(self, type):
        
        _file = f'{self.FILE_PATH}/{type}.json'
        
        if not os.path.exists(_file):
            return {"error": "Invalid type!"}
        
        with open(_file, 'r') as f:
            return json.load(f)
     
     
    def load_backup(self, type):
    
        _file = f'{self.FILE_PATH}/Backups/{type}_backup.json'
        
        if not os.path.exists(_file):
            return {"error": "Invalid type!"}
        
        with open(_file, 'r') as f:
            return json.load(f)
     
     
    # Save data to the desired table in data store   
    def save(self, type, data):
        
        current_data = self.load(type)
        
        _backup_file = f'{self.FILE_PATH}/Backups/{type}_backup.json'
        _file = f'{self.FILE_PATH}/{type}.json'
        
        if not _backup_file or not _file:
            return {"error": "File does not exist!"}
        
        with open(_backup_file, 'w') as file:
            json.dump(current_data, file, indent=4)
        
        with open(_file, 'w') as file:
            return json.dump(data, file, indent=4)
        
        
    # Retrieve passcode hash
    def get_passcodehash(self):
        _file = "Data/passcode.txt"
        
        with open(_file, 'r') as f:
            return f.read()
        
    # set new passcode
    def set_passcodehash(self, hashed_code):
        _file = "Data/passcode.txt"
        
        with open(_file, 'w') as f:
            return f.write(hashed_code)
        
        
    def get_config(self):
        _file = "Data/config.json"
        
        with open(_file, 'r') as f:
            return f.read()