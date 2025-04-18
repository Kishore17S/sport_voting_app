from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='frontend', static_folder='frontend')
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    selected = request.form.get('option')
    if selected in ['Cricket', 'Football']:
        return jsonify({'status': 'success', 'message': 'Voted successfully!'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid option!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
