"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import pyoxford
# from tokens import *
oxford_computer_speech = "d6814acbebb940cd8553e0b125cc63a1"
api = pyoxford.speech("kage-test-speech", oxford_computer_speech)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Parrot me',
        year=datetime.now().year,
    )

@app.route('/game')
def gameon():
    bing_token = "bHBDnK+h8L79Mrmp8M0PHfyogYuTrpd6PM25bBh4S9A"
    oxford_computer_speech = "d6814acbebb940cd8553e0b125cc63a1"

    text = "a b c d e f"
    api = pyoxford.speech("kage-test-speech", oxford_computer_speech)

    # text to speech (.wav file)
    binary = api.text_to_speech(text)
    with open("sound1.wav", "wb") as f:
        f.write(binary)

    # speech to text
    recognized = api.speech_to_text("sound1.wav")
    # print(recognized)

    # if text == recognized:
    #     print(recognized)
    #     print("success!!")

    return render_template(
        'game.html',
        title = 'Parrot Me',
        word = recognized
    )

