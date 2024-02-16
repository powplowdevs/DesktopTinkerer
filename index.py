from flask import Flask, render_template, request, abort, jsonify
from flask_cors import CORS
app = Flask(__name__)
app.config['DEBUG'] = True

PREDEFINED_KEY = None
link = "nothing"

def verify_request(signature):
    return PREDEFINED_KEY == signature

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_png', methods=['POST'])
def upload_png():
    if 'file' not in request.files or 'signature' not in request.form:
        abort(400, 'Missing sum')

    file = request.files['file']
    signature = request.form['signature']

    if not verify_request(signature):
        return "401"

    file.save('.\\static\\desktop.png')

    return "[Horray!] huzzah! or sum idk bro i have an APUSH test in like 2 days"

@app.route('/save_link', methods=['POST'])
def save_link():
    global link
    data = request.get_json()
    if 'string' in data:
        link = data['string']
        return jsonify({"message": "Link saved successfully"})
    else:
        return jsonify({"error": "Link not provided in JSON data"}), 400

@app.route('/link', methods=['GET'])
def get_link():
    global link
    return jsonify({"Saved link": link})


if __name__ == '__main__':
    app.run(debug=True)
