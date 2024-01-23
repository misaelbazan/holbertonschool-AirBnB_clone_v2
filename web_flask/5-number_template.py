#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape


# Create an instance of the Flask application
app = Flask(__name__)


# Route for the main page
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this script will return 'hello HBNB'"""
    return "Hello HBNB!"


# Route for "/hbnb"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    It will return the content only 
    if it is in the hbnb url.
    """
    return "HBNB"


# Route for "/c/<text>"
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """this script accepts only text."""
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)


# Route for "/python/<text>"
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    This script accepts only text if it does
    not display the default value.
    """
    text = escape(text).replace('_', ' ')
    return "Python {}".format(text)


# Route for "/number/<int:n>"
@app.route("/number/<int:n>", strict_slashes=False)
def num_int(n):
    """This script accepts only integers."""
    return "{} is a number".format(n)

# Route for "/number_template/<int:n>"
@app.route("/number_template/<int:n>")
def html_int(n):
    """This script links to an html page."""
    return render_template("5-number.html", number=n)


# Check if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
