#!/usr/bin/python3
"""this is my comment"""


from flask import Flask
from flask import escape
from flask import render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """remove the current sqlalchemy sesssion"""
    storage.close()


@app.route('/states_list')
def states():
    states = storage.all(State)
    sortedstates = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sortedstates)