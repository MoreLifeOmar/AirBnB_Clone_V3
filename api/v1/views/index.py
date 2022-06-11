#!/usr/bin/python3
"""
Index Module
"""
from api.v1.view import app_views
from flask import jsonify


@app_views.route('/status', strit_slashes=False)
def status():
    """ API Status"""
    okStatus = {"status": "OK"}
    return jsonify(okStatus)


@app_views.route('stats')
def stats():
    """
        Return dict of data count
    """
    dictionnary = {"amenities": storage.count(Amenity),
                   "cities": storage.count(City),
                   "places": storage.count(Place),
                   "reviews": storage.count(Review),
                   "states": storage.count(State),
                   "users": storage.count(User)}
    return jsonify(dictionnary)
