from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def go_to_standalone():
    return render_template('standalone.html')

@app.route('/edit_pill/slot_<slot_id>')
def edit_pill(slot_id):
    return render_template('edit_pill.html', slot_id=(int(slot_id)-1))