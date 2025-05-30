from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def send_email(to_email, sir_name):
    from_email = 'adidabarackpilly@gmail.com'
    app_password = 'adida2601'

    subject = "Registration Successful"
    body = f"Dear {sir_name},\n\nYou have been successfully registered to Enrollix. Thank you!"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, msg.as_string())
            print(f"✅ Email sent to {to_email}")
            return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

@app.route('/save', methods=['POST'])
def save_data():
    new_entry = request.get_json()

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    data.append(new_entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    email_sent = send_email(new_entry['email'], new_entry['sir_name'])

    if email_sent:
        return jsonify({"message": "Data saved and email sent successfully"}), 200
    else:
        return jsonify({"message": "Data saved, but email failed"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
