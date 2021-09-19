import os

from flask import Flask
from pathlib import Path

app = Flask(__name__)

PATH_ROOT = Path(__file__).parent.parent
PATH_DATA = Path(os.environ.get("MELLOW_PATH_DATA", PATH_ROOT / 'data'))
PATH_TASKS = PATH_DATA / 'mello.sqlite3'

for path in [v for v in globals().values() if isinstance(v, Path)]:
    print(path)
    if path.exists() or path.suffix:
        continue
    path.mkdir(exist_ok=True, parents=True)


CATEGORIES = ['TODO', 'DOING', 'DONE']
