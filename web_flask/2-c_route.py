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

from flask import Flask


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
    return f"{result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
