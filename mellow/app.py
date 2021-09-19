import os

from flask import Flask, render_template
from mellow.config import app


@app.route('/')
def index():
    return render_template('index.html')

def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
