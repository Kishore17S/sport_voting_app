from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, template_folder='frontend', static_folder='frontend')
app.secret_key = "supersecretkey"  # for session management

# Initialize the database (Create table and set initial counts)
def init_db():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS votes (option TEXT PRIMARY KEY, count INTEGER)')
    c.execute('INSERT OR IGNORE INTO votes (option, count) VALUES (?, ?)', ('Cricket', 0))
    c.execute('INSERT OR IGNORE INTO votes (option, count) VALUES (?, ?)', ('Football', 0))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    selected = request.form.get('option')
    if selected not in ['Cricket', 'Football']:
        return jsonify({'status': 'error', 'message': 'Invalid option!'})

    # Update the vote count for the selected option
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('UPDATE votes SET count = count + 1 WHERE option = ?', (selected,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})

@app.route('/results')
def results():
    conn = sqlite3.connect('votes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM votes')
    results = c.fetchall()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080)
