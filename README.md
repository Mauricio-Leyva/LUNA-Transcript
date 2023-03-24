# LUNA-Transcript
LUNA Transcript is a Flask web application that allows users to upload MP3, M4A, WAV, and FLAC files and transcribe them using [Whisper](https://github.com/openai/whisper.git). The application is built using Flask and allows users to upload audio files, transcribe them, and view the transcriptions on a separate page. The transcriptions are performed using the Whisper library, which provides accurate transcription and translation of audio files. The project is designed to be easy to use and accessible to users of all levels, with a simple user interface and clear instructions for uploading and transcribing audio files.


### Prerequisites
***
Before running LUNA Transcript, make sure you have the following installed:

- Python 3.6 or higher
- Flask
- Werkzeug
- Whisper

### Getting Started
***
To get started, clone this repository:
```
$ git clone https://github.com/your_username/LUNA-Transcript.git
```
Once you have cloned the repository, navigate to the project directory:
```
$ cd LUNA-Transcript
```
The uploads directory is where the uploaded audio files will be saved. You can specify the location of this directory by setting the UPLOAD_FOLDER configuration variable in the Flask app. In the provided code, the UPLOAD_FOLDER is set to uploads/, but you can modify this to suit your needs.

The models directory is where the whisper models are stored. The load_model function in the code expects to find the models in this directory. You'll need to download the appropriate whisper model for your use case and save it in this directory.

Once you've created these directories, you should be ready to run the code.

### Available models and languages
***
This application uses the Whisper library to perform speech-to-text transcription. Whisper provides a range of pre-trained models with varying sizes and capabilities, including English-only and multilingual models. The following table lists the available models and their corresponding sizes, parameters, and resource requirements:

| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|--------|------------|--------------------|--------------------|---------------|----------------|
| tiny   | 39 M       | tiny.en            | tiny               | ~1 GB         | ~32x           |
| base   | 74 M       | base.en            | base               | ~1 GB         | ~16x           |
| small  | 244 M      | small.en           | small              | ~2 GB         | ~6x            |
| medium | 769 M      | medium.en          | medium             | ~5 GB         | ~2x            |
| large  | 1550 M     | N/A                | large              | ~10 GB        | 1x             |

By default, this application uses the small model. To use a different model, modify the model = whisper.load_model("small", download_root="your own path here") line in LUNA_Transcript.py to specify the desired model.

### Running the Application
***
Before running the application, make sure to modify the following configuration variables in LUNA_Transcript.py to suit your needs:

- app.config['UPLOAD_FOLDER'] = 'uploads/' be sure to modify the path to include your own path where the uploads/ folder should be located

And make sure to modify the
```
model = whisper.load_model("small", download_root="your own path here")
```
to include your own path to the Whisper model.


To run the application, use the following command:
```
$ python LUNA_Transcript.py
```
Once the server is running, navigate to http://localhost:5000 in your web browser.

### Usage
To transcribe an audio file, click on the "Choose File" button on the home page and select an MP3, M4A, WAV, or FLAC file. Once you have selected a file, click the "Transcribe" button. The transcription and translation will be displayed on a new page.

### License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/openai/whisper/blob/main/LICENSE) file for details.

### Approach
![Image text](https://raw.githubusercontent.com/openai/whisper/main/approach.png)
