from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# This file lives in the VOLUME not inside the container
NOTES_FILE = '/data/notes.txt'

# Make sure the /data folder exists
os.makedirs('/data', exist_ok=True)

@app.route('/')
def home():
    return jsonify({'message': 'Volumes project running!'})

@app.route('/write', methods=['POST'])
def write_note():
    note = request.json.get('note')
    # Write note to the file in the volume
    with open(NOTES_FILE, 'a') as f:
        f.write(note + '\n')
    return jsonify({'message': f'Note saved: {note}'})

@app.route('/read', methods=['GET'])
def read_notes():
    # Read all notes from the file in the volume
    if not os.path.exists(NOTES_FILE):
        return jsonify({'notes': [], 'message': 'No notes yet!'})
    with open(NOTES_FILE, 'r') as f:
        notes = f.read().splitlines()
    return jsonify({'notes': notes, 'total': len(notes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
