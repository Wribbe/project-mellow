import os

from flask import render_template, g

from mellow import db
from mellow.config import app


@app.route('/')
def index():
    return render_template('index.html', tasks=db.tasks())


def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
