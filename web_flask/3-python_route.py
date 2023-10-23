#!/usr/bin/python3
"""starts a flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """/: display “Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """/hbnb: display “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Cvalue(text):
    return 'C ' + text.replace('_', ' ')


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')