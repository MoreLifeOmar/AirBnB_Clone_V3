 #!/usr/bin/python3
    """_summary_
        flask view for state class
    """

from AirBnB_clone_v3.api.v1.app import not_found_error
from flask import jsonify, abort, request
from models import storage
from models.state import state
from api.v1.view import from .views import app_views

prefix = 'api/v1/states'
@app_views.route('/states', methods=["GET"], strict_slashes=False)
def get_state():
    """retrieve state """
    state_list = [s.to_dict() for s in storage.all('State').values()]
    return jsonify(state_list)

@app_views.route('states/<state_id>',  methods=["GET"], strict_slashes=False)
def get_state_id(state_id):
    """get state by id"""
    try:
        idstate = storage.get("State", state_id)
    except  not idstate:
        abort(404)
    return jsonify(idstate.to_dict())

@app_views.route('state/<state_id>', methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """ delete state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    state.save()

@app_views.route('states', methods=['POST'], strict_slashes=False)
def create_state():
    """create a state object"""
    
    if not  request.get_json()
        return jsonify({:}), 400
    if 'name' not in request.get_json():
        abort(400)
    params = request.get_json()#.to_dict()
    state = State(**params)
    state.save()
    return jsonify(state.to_dict()), 201

@app_views.route('states/<state_id>', methods=['PUT'], strict_slahes=False)
def update_state(state_id):
    """update state instance"""
    req = request.get_json()
    if not request.is_json:
        return print("not a json"), 400
    if "id" not in req or "name" not in req:
        abort(400)
    stt = storage.get("State", state_id)
    if stt is None:
        abort(404)
    stt.name = req['name']
    stt.save()
    return jsonify(stt.to_dict()), 200
    
