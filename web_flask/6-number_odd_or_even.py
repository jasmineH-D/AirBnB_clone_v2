#!/usr/bin/python3
"""starts a flask web app"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def index():
    """
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    /hbnb: display “HBNB”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Cvalue(text):
    """
    /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols  with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pyvalue(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Numbervalue(n):
    """
    display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def htmlvalue(n):
    """
    display a HTML page only if n is an integer
    """
    if n % 2 == 0:
        even = 'even'
    else:
        even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           even=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
