#!/usr/bin/python3
"""this is my comment"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """function to return hello hbnb """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
