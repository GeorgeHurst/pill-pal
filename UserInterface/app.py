from flask import Flask, render_template, request, jsonify
import os, json
from werkzeug.security import check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


with open('Data/passcode.txt', 'r') as file:
    stored_hash = file.read().strip()

DATA_FILE = 'Data/Tables/data.json'
PILL_FILE = 'Data/Tables/pills.json'
SCHEDULE_FILE = 'Data/Tables/schedule.json'
PREFERENCES_FILE = 'Data/Tables/user_preferences.json'
FAILED_SCHEDULE_FILE = 'Data/Tables/failed_schedule.json'
BACKUP_PILL_FILE = 'Data/Tables/Backups/pills_backup.json'
BACKUP_SCHEDULE_FILE = 'Data/Tables/Backups/schedule_backup.json'
BACKUP_FAILED_SCHEDULE_FILE = 'Data/Tables/Backups/failed_schedule_backup.json'

@app.route('/')
def login():
    return render_template('login_page.html')




############### STANDALONE ROUTES ###############
@app.route('/standalone')
def go_to_standalone():
    return render_template('standalone.html')

@app.route('/edit_pill/slot_<slot_id>')
def edit_pill(slot_id):
    return render_template('edit_pill.html', slot_id=(int(slot_id)-1))

# @app.route('/load_data/<data_type>', methods=['GET'])
# def load_data(data_type):
    
#     match data_type:
#         case "pills":
#             file = PILL_FILE
#         case "schedule":
#             file = SCHEDULE_FILE
#         case "user_preferences":
#             file = PREFERENCES_FILE
#         case "failed_scheduled":
#             file = FAILED_SCHEDULE_FILE
#         case _:
#             print("Invalid File Type!")
#             return
    
#     if not os.path.exists(file):
#         return jsonify({})
#     with open(file, 'r') as f:
#         data = json.load(f)
#     return jsonify(data)


# @app.route('/load_backup/<data_type>', methods=['GET'])
# def load_backup(data_type):
    
#     match data_type:
#         case "pills":
#             file = BACKUP_PILL_FILE
#         case "schedule":
#             file = BACKUP_SCHEDULE_FILE
#         case _:
#             print("Invalid File Type!")
#             return
    
#     if not os.path.exists(file):
#         return jsonify({})
#     with open(file, 'r') as f:
#         data = json.load(f)
#     return jsonify(data)

# @app.route('/get_pill_data/<int:slot_id>', methods=['GET'])
# def get_pill_data(slot_id):
#     if not os.path.exists(PILL_FILE):
#         return jsonify({})

#     try:
#         with open(PILL_FILE, 'r') as f:
#             pills = json.load(f)
#         if slot_id < 0 or slot_id >= len(pills):
#             return jsonify({})
#         pill_data = pills[slot_id]
#         return jsonify(pill_data)
#     except Exception as e:
#         print("Error fetching pill data:", e)
#         return jsonify({}), 500
    
# @app.route('/save_pill/<int:slot_id>', methods=['POST'])
# def save_pill(slot_id):
#     if not os.path.exists(PILL_FILE):
#         return jsonify({'error': 'Data file not found'}), 404

#     try:
#         with open(PILL_FILE, 'r') as f:
#             data = json.load(f)

#         pills = data.get("pills", [])

#         while len(pills) <= slot_id:
#             pills.append({})

#         updated_pill = {
#             "name": request.form['name'],
#             "dosePerPill": int(request.form['dosePerPill']),
#             "pillsPerDose": int(request.form['pillsPerDose']),
#             "dosesPerDay": int(request.form['dosesPerDay']),
#             "minHoursBetweenDoses": int(request.form['minHoursBetweenDoses'])
#         }

#         pills[slot_id] = updated_pill
#         data["pills"] = pills

#         with open(PILL_FILE, 'w') as f:
#             json.dump(data, f, indent=2)

#         return go_to_standalone()

#     except Exception as e:
#         print("Error saving pill data:", e)
#         return jsonify({'error': 'Failed to save'}), 500

# @app.route('/update_pill_data/<int:slot_id>', methods=['POST'])
# def update_pill_data(slot_id):
#     if not os.path.exists(PILL_FILE):
#         return jsonify({'error': 'Data file missing'}), 404

#     try:
#         with open(PILL_FILE, 'r') as f:
#             data = json.load(f)

#         pills = data.get("pills", [])
#         if slot_id < 0 or slot_id >= len(pills):
#             return jsonify({'error': 'Invalid slot ID'}), 400

#         updated_pill = request.get_json()
#         pills[slot_id] = updated_pill

#         with open(PILL_FILE, 'w') as f:
#             json.dump(data, f, indent=2)

#         return jsonify({'success': True})
#     except Exception as e:
#         print("Error updating pill data:", e)
#         return jsonify({'error': 'Internal error'}), 500

# @app.route('/save_data/<data_type>', methods=['POST'])
# def save_data(data_type):
    
#     match data_type:
#         case "pills":
#             file = PILL_FILE
#             backup_file = BACKUP_PILL_FILE
#         case "schedule":
#             file = SCHEDULE_FILE
#             backup_file = BACKUP_SCHEDULE_FILE
#         case "failed_schedule":
#             file = FAILED_SCHEDULE_FILE
#             backup_file = BACKUP_FAILED_SCHEDULE_FILE
#         case "user_preferences":
#             file = PREFERENCES_FILE
#             backup_file = None
#         case _:
#             print("Invalid File Type!")
#             return
    
#     if backup_file != None:
#         with open(file, 'r') as f:
#             data = json.load(f)
#         with open(backup_file, 'w') as bf:
#             json.dump(data, bf, indent=2)
    
#     new_data = request.get_json()
#     with open(file, 'w') as f:
#         json.dump(new_data, f, indent=2)
#     return jsonify({'status': 'success'})


# @app.route('/save_backup/<data_type>', methods=['POST'])
# def save_backup(data_type):
    
#     match data_type:
#         case "pills":
#             file = BACKUP_PILL_FILE
#             og_file = PILL_FILE
#         case "schedule":
#             file = BACKUP_SCHEDULE_FILE
#             og_file = SCHEDULE_FILE
#         case _:
#             print("Invalid File Type!")
#             return
#     with open(og_file, 'r') as f:
#         new_data = json.load(f)
    
#     with open(file, 'w') as f:
#         json.dump(new_data, f, indent=2)
#     return jsonify({'status': 'success'})


#################################################


@app.route('/main')
def main_page():
    return render_template("main_page.html")

@app.route('/schedule')
def schedule():
    return render_template("schedule.html")

@app.route('/check_passcode', methods=['POST'])
def check_passcode():
    data = request.get_json()
    user_passcode = data.get('passcode', '')

    if check_password_hash(stored_hash, user_passcode):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True)
