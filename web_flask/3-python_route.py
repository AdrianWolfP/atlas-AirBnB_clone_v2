#!/usr/bin/python3

""" Write a script that states flask web app"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def greeting():
    """ Returns a greeting """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ function that returns hbnb """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ function that returns message with a C """
    new_text = text.replace("_", " ")
    return ('C ' + new_text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def textPython(text='is cool'):        
    return ('Python ' + text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)