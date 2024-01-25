#!/usr/bin/python3
"""Script that starts a Flask web application
    Must be listening to 0.0.0.0:5000
    Routes:
        - (/) : display "Hello HBNB!"
        - (/hbnb) : display "HBNB"
        - (/c/<text>) : display "C" followed by the value of the <text>
        variable (Replace "_" with a space " ")
    .You must use the option strict_slashes=False in the route definition
"""

from flask import Flask, abort, render_template


# Create an instance of the Flask application
app = Flask(__name__)


# Route from the main page
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Route from /hbnb page
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


# Route from "/c/<text>"
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    # Use replace method for replace "_" with spaces " "
    result = text.replace("_", " ")
    return f"C {result}"


# Route from "/python/<text>, with 'is cool' as default value"
@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    # Replacing underscores "_" with spaces " "
    result = text.replace("_", " ")
    return f"Python {result}"


# Route from "/number/<n>, to display a text only if <n> is an int.
@app.route("/number/<n>", strict_slashes=False)
def n_is_int(n):
    # Validationg if "n" is int
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)


# Route from "/number_template/<n>", display a HTML page if <n> is int
@app.route("/number_template/<n>", strict_slashes=False)
def n_is_int_html(n):
    # Validating if "n" is digit
    if n.isdigit():
        # Returning the template with the customized value "n"
        return render_template("5-number.html", n=n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
