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

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create data file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/save', methods=['POST'])
def save_data():
    # Get form fields
    sir_name = request.form.get('sir_name')
    othernames = request.form.get('othernames')
    date_of_birth = request.form.get('date_of_birth')
    email = request.form.get('email')
    gender = request.form.get('gender')

    # Handle file upload
    file = request.files.get('profile_image')
    filename = None
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

    # Prepare new entry
    new_entry = {
        "sir_name": sir_name,
        "othernames": othernames,
        "date_of_birth": date_of_birth,
        "email": email,
        "gender": gender,
        "profile_image": filename
    }

    # Load existing data
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    # Append new entry
    data.append(new_entry)

    # Save updated data
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
