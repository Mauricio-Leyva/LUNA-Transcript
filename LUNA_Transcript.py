# LUNA Transcript
# Author: Mauricio Leyva
# Description: This code is a Flask web application that transcribes audio files using Whisper.

import os
from typing import Dict
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import whisper

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'm4a', 'wav', 'flac'}

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Function to check if the file is allowed to be uploaded
def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Transcribe MP3 file
def transcribe_mp3(file_path: str) -> Dict[str, str]:
    try:
        model = whisper.load_model("small", download_root="./model")
    except Exception as e:
        return {'error': str(e)}

    result = model.transcribe(file_path, verbose=True)
    translation = model.transcribe(file_path, task="translate", verbose=True)
    del model
    return {'original_text': result, 'translation': translation}


# Route for uploading MP3 file and transcribing it
@app.route('/transcribe', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the file is present in the request
        if 'file' not in request.files:
            return {'error': 'No file was selected.'}
        file = request.files['file']
        # Check if the file is an allowed type
        if file and allowed_file(file.filename):
            # Secure the filename before saving it
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Transcribe the MP3 file
            transcription = transcribe_mp3(file_path)
            if 'error' in transcription:
                return {'error': transcription['error']}
            # Delete the uploaded file
            os.remove(file_path)
            return render_template('transcription.html', transcription=transcription)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')

