#!/usr/bin/puython3
#!/usr/bin/python3
'''
    RESTful API for class City
'''


from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models import Review, storage


@app_views.route('/api/v1/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def all_reviews(place_id):
    """get all reviews of a place"""
    p = storage.get('Place', place_id)
    if p is None:
        abort(404)
    r = [r for r in p.reviews] 
    return jsonify(r.to_dict()), 200

@app_views.route(' /api/v1/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def review_by_id(review_id):
    """_summary_
        get review by id 
    Args:
        review_id (_type_): _description_
    """
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict()), 200

@app_view.route('/api/v1/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def del_review(review_id):
    """_summary_
        delete review by id
    Args:
        review_id (_type_): _description_
    """
    review = storage.get('Reveiw', review_id)
    if review is None:
        abort(404)
    review.delete(review) #storage.delete
    storage.save()
    return jsonify({}), 200

@app_views.route(' /api/v1/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """_summary_
        create new place reveiw
    Args:
        place_id (_type_): _description_
    """
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    elif not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "user_id" not in request.get_json():
        return jsonify({"error": "Missing user_id"}), 400
    elif storage.get("User", request.get_json()["user_id"]) is None:
        abort(404)
    elif "text" not in request.get_json():
        return jsonify({"error": "Missing text"}), 400
    else:
        obj_data = request.get_json()
        obj = Review(**obj_data)
        obj.place_id = place_id
        obj.save()
        return jsonify(obj.to_dict()), 201
    
    
@app_views.route('/api/v1/reviews/<review_id>'):
def update_review(review_id):
    """_summary_
    update a review
    Args:
        review_id (_type_): _description_
    """
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    req_data = request.get_json()
    req_data.pop("id", None)
    req_data.pop("created_at", None)
    req_data.pop("updated_at", None)
    [setattr(review, k, v) for k, v in req_data.items()]
    review.save()
    return make_response(jsonify(review.to_dict()), 200)
