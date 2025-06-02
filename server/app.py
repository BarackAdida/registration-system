from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.json'
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdirs(UPLOAD_FOLDER)

@app.route('/save', methods=['POST'])
def save_data():
    sir_name = request.form.get('sir_name')
    othernames = request.form.get('othernames')
    date_of_birth = request.form.get('date_of_birth')
    email = request.form.get('email')
    gender = request.form.get('gender')

    image_file = request.files.get('profile_image')
    image_filename = secure_filename(image_file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
    image_file.save(image_path)

    new_entry = {
        "sir_name": sir_name,
        "othernames": othernames,
        "date_of_birth": date_of_birth,
        "email": email,
        "gender": gender,
        "profile_image": image_filename
    }

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    data.append(new_entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "Data saved successfully!"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json', r) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
