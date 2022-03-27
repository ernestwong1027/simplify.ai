import os
from os import path
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




#recieve file and send redirect link
@app.route('/submit', methods=['POST'])
def submit_file():
    if 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = generate_file_name(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            response = {
                'filename': filename
            }
            return response, 200
    return "Invalid File", 400


#Get processed file
@app.route('/file/<filename>', methods=['GET'])
def download_file(filename):
    filename = filename+'.txt'
    if path.exists('uploads/' + filename):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    return "Invalid File", 400

#Check if file type is allowed
ALLOWED_EXTENSIONS = {'txt', 'wav'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_file_name(filename):
    return uuid.uuid4().hex + '.' + filename.rsplit('.', 1)[1].lower()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)