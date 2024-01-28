#!/usr/bin/python3
"""this is my comment"""


from flask import Flask
from flask import escape
from flask import render_template
app = Flask(__name__)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def show_python_is_cool(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to return hello hbnb """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to return hbnb with /hbnb url"""
    return "HBNB"


@app.route('/c/<text>')
def show_c(text, strict_slashes=False):
    """display c followed by text"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/number/<int:n>')
def show_n(n, strict_slashes=False):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n, strict_slashes=False):
    """number template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
