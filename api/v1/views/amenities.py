#!/usr/bin/python3
    """_summary_
    amenity views
    """
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """
        return all amenity objects in json form
    """
    amenity_list = [a.to_dict() for a in storage.all('Amenity').values()]
    return jsonify(amenity_list)

@app_views.route('/api/v1/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def amenity_by_id():
    """
    return a given amenity
    """
    a = stroage.get("Amenity", amenity_id)
    if a is None:
        abort(404)
    return jsonify(a.to_dict()), 200

@app_views.route('/api/v1', methods=['POST'], strict_slashes=False)
def create_amenity():
    """
    create amenity from url params
    """
    req = request.get_json()
    if not req or not req.is_json:
        return jsonify({"error": "Not a JSON"}), 400    
    elif "name" not in req:
        return jsonify({"error": "Missing name"}), 400
    else:
        name = req["name"]
        data = request.get_json()
        obj = Amenity(**data)
        storage.save()
        return jsonify(obj.to_dict()), 201
    
@app_views.route('/amenities/<amenities_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenities_id):
    """
    update existing amenity object
    """
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    obj = storage.get("Amenity", amenities_id)
    if obj is None:
        abort(404)
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
