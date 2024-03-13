#!/usr/bin/python3
""" Script that starts Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State

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
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<hiss>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def 

@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)