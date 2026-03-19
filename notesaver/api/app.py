from flask import Flask, jsonify, request
import psycopg2, os

app = Flask(__name__)

# Connect to PostgreSQL
def get_db():
    return psycopg2.connect(os.getenv('DATABASE_URL'))

# Create table on startup
def setup():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            note TEXT NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

setup()

# Homepage
@app.route('/')
def home():
    return jsonify({'message': 'Note Saver API is running!'})

# Save a note
@app.route('/notes', methods=['POST'])
def save_note():
    text = request.json.get('note')
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO notes (note) VALUES (%s) RETURNING *', (text,))
    note = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': note[0], 'note': note[1]})

# Get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notes ORDER BY created_at DESC')
    notes = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{'id': n[0], 'note': n[1], 'created_at': str(n[2])} for n in notes])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
