#!/usr/bin/python3
"""_summary_  user views """


from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
        return all user objects in json form
    """
    user_list = [a.to_dict() for a in storage.all('User').values()]
    return jsonify(user_list)


@app_views.route('/api/v1/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def user_by_id(user_id):
    """
    return a given user
    """
    a = stroage.get("User", user_id)
    if a is None:
        abort(404)
    return jsonify(a.to_dict()), 200


@app_views.route('/api/v1', methods=['POST'], strict_slashes=False)
def create_user():
    """
    create user from url params
    """
    req = request.get_json()
    if not req or not req.is_json:
        return jsonify(({"error": "Not a JSON"}), 400)
    elif "name" not in req:
        return jsonify(({"error": "Missing name"}), 400)
    elif "email" not in req:
        return jsonify(({"error": "Missing email"}), 400)
    elif "password" not in req:
        return jsonify(({"error": "Missing password"}), 400)
    else:
        name = req["name"]
        data = request.get_json()
        obj = User(**data)
        storage.save()
        return jsonify((obj.to_dict()), 201)


@app_views.route('/users/<users_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user(users_id):
    """
    update existing user object
    """
    if not request.get_json():
        return jsonify(({"error": "Not a JSON"}), 400)
    obj = storage.get("User", users_id)
    if obj is None:
        abort(404)
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()
    return jsonify((obj.to_dict()), 200)
