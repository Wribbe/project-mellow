import sqlite3

from flask import current_app
from mellow.config import PATH_TASKS, CATEGORIES


def db():

    init_db = not PATH_TASKS.is_file()
    conn = sqlite3.connect(PATH_TASKS)

    if init_db:

        with current_app.open_resource('schema.sql') as f:
            conn.executescript(f.read().decode('utf8'))

        cursor = conn.cursor()
        for category in CATEGORIES:
            cursor.execute(
                "INSERT INTO category (name) VALUES (?)", (category,)
            )
        conn.commit()
        cursor.close()

    conn.row_factory = sqlite3.Row

    return conn


def tasks():
    conn = db()

    tasks = {category: [] for category in CATEGORIES}

    cursor = conn.cursor()
    queried_tasks = cursor.execute("""
        SELECT title ,description ,category.name AS category
        FROM task JOIN category WHERE task.id_category = category.id
    """).fetchall()
    cursor.close()

    for task in queried_tasks:
        tasks[task['category']].append(task)

    return tasks
