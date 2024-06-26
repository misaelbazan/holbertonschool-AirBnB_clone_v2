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
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """After each request removes the current SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a list of all states"""
    #amenities = storage.all(Amenity)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
