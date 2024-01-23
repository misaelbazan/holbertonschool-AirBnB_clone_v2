#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


# Create an instance of the Flask application
app = Flask(__name__)


# Route for the main page
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Route for "/hbnb"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


# Route for "/c/<text>"
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces in the text variable
    text = escape(text).replace('_', ' ')
    return "C {}".format(text)


# Route for "/python/<text>"
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    text = escape(text).replace('_', ' ')
    return "Python {}".format(text)


# Check if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
