"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import pyoxford
from tokens import *

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    text = "a b c d e f"
    api = pyoxford.speech("kage-test-speech", oxford_computer_speech)

    # text to speech (.wav file)
    binary = api.text_to_speech(text)
    # with open("sound1.wav", "wb") as f:
    #     f.write(binary)
    #
    # # speech to text
    recognized = api.speech_to_text("sound1.wav")
    # print(recognized)
    #
    # if text == recognized:
    #     print(recognized)
    #     print("success!!")
    #

    return render_template(
        'index.html',
        title='Parrot me',
        year=datetime.now().year,
    )

