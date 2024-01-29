#!/usr/bin/python3
"""Script that starts a Flask web application
    Must be listening to 0.0.0.0:5000
    You must use storage for fetching data "from models import storage"
    and storage.all(...)
    After each request you must remove the current SQLAchemy Session:
        .Declare a method to handle @app.teardown_appcontext
        .Call in this method storage.close()
    Routes:
    .(/cities_by_state): display a HTML page
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """After each request removes the current SQLAlchemy session"""
    storage.close()


# Route from /cities_by_state
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Fetching data from storage engine sorted from A-Z by "name" attr"""
    states_dict = storage.all(State).values()
    # Return a template with the variable set to the required argument
    return render_template("8-cities_by_states.html", states=states_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
