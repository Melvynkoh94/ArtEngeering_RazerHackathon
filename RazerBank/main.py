# FLASK_APP=main.py in .flaskenv, telling the interpreter that main file is main.py
# But we need to import Flask app declared in application/__init__.py
# Previously it was here
from application import app # FLASK_APP=main.py in .flaskenv, telling the interpreter that main file is main.py
# But we need to import Flask app declared in application/__init__.py
# Previously it was here
from application import app 