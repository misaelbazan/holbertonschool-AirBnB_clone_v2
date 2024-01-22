#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
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
def python_text(text="is_cool"):
    text = escape(text).replace('_', ' ')
    return "python {}".format(text)

# Route for "/number/<int:n>"
@app.route("/number/<int:n>", strict_slashes=False)
def num_int(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>")
def html_int(n):
    return render_template("5-number.html", number=n)


# Check if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)