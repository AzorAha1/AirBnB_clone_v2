#!/usr/bin/python3
"""this is my comment"""


from flask import Flask
from flask import escape
app = Flask(__name__)


@app.route('/python/<text>')
def show_python_is_cool(text="is cool"):
    """display python followed by text but is cool is constant"""
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route('/')
def hello_hbnb():
    """function to return hello hbnb """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """function to return hbnb with /hbnb url"""
    return "HBNB"


@app.route('/c/<text>')
def show_c(text):
    """display c followed by text"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run()
