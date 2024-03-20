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
def hiss(hiss="is cool"):
    """ function that reutrns a python message """
    return 'Python {}'.format(hiss.replace('_', ' '))


@app.route('/number/<input>', strict_slashes=False)
def digis(input):
    """ function that displays a number if it is an integer """
    if input.isdigit():
        return '{} is a number'.format(input)


@app.route('/number_template/<int:input>', strict_slashes=False)
def html_template(input):
    """ function that displays a HTML page only if input is an integer """
    return render_template('5-number.html', number=input)


@app.route('/number_odd_or_even/<int:input>', strict_slashes=False)
def odd(input):
    """ function that displays an HTML page that checks odd or even """
    if input % 2 == 0:
        input = '{} is even'.format(input)
    else:
        input = '{} is odd'.format(input)
    return render_template('6-number_odd_or_even,html', can_you_even=input)


@app.route('/states_list', strict_slashes=False)
@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)