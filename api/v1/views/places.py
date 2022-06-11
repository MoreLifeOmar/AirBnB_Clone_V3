#!/usr/bin/python3
"""_summary_  place views """


from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City


@app_views.route('api/v1/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """
        return all place objects in json form
    """
    city = storage.get(City, city_id)
    try:
        places = city.places
    except Exception:
        abort(404)
    places_list = []
    for place in places:
        places_list.append(place.to_dict)
    return jsonify(places_list)


@app_views.route('/api/v1/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def place_by_id(place_id):
    """
    return a given place
    """
    a = stroage.get("Place", place_id)
    if a is None:
        abort(404)
    return jsonify(a.to_dict()), 200

@app_views.route('/api/v1/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def place_by_id(place_id):
    """
    return a given place
    """
    a = stroage.get("Place", place_id)
    if a is None:
        abort(404)
    storage.delete(a)
    storage.save()
    res = {}
    return jsonify(res), 200


@app_views.route('/api/v1/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """
    create place from url params
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    req = request.get_json()
    if not req or not req.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in req:
        return jsonify({"error": "Missing name"}), 400
    elif "user_id" not in req:
        return jsonify({"error": "Missing user_id"}), 400
    else:
        name = req["name"]
        data = request.get_json()
        obj = Place(**data)
        storage.save()
        return jsonify((obj.to_dict()), 201)


@app_views.route('/places/<places_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(places_id):
    """
    update existing place object
    """
    body_req = request.get_json()
    obj = storage.get("Place", places_id)
    if body_req is None:
        return jsonify({"error": "Not a JSON"}), 400
    if obj is None:
        abort(404)
    obj.name = body_req['name']
    obj.save()
    return jsonify((obj.to_dict()), 200)
