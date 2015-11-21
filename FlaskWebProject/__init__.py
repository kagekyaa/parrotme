"""
The flask application package.
"""
import os
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

from flask import Flask
app = Flask(__name__, template_folder=tmpl_dir)

import FlaskWebProject.views