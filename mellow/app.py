import os

from flask import render_template, g, request, redirect, url_for

from mellow import db
from mellow.config import app


@app.route('/')
def index():
    return render_template('index.html', tasks=db.tasks())


@app.route('/task_add', methods=['POST', 'GET'])
def task_add():

    if request.method == "POST":
        form = request.form
        db.create_task(form.get('title'), form.get('description'))
        return redirect(url_for('index'))

    return render_template('task_add.html')


def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
