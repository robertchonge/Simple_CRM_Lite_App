from flask import Flask, request, jsonify, send_from_directory
import json, os

app = Flask(__name__)
DB_FILE = 'contacts.json'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    if not os.path.exists(DB_FILE):
        return jsonify([])
    with open(DB_FILE) as f:
        return jsonify(json.load(f))

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    contacts = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE) as f:
            contacts = json.load(f)
    contacts.append(data)
    with open(DB_FILE, 'w') as f:
        json.dump(contacts, f)
    return jsonify({'success': True}), 201

if __name__ == '__main__':
    app.run()
