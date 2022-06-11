#!/usr/bin/python3
"""
States Module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State


def checker(id):
    """ checker if a state exists in storage """
    try:
        state = storage.get(State, id)
        state.to_dict()
    except Exception:
        abort(404)
    return state


def getStates(state_id):
    """
    retrieve all states if the id is None otherwise
    retrieve the state with the given id
    """
    if state_id is not None:
        state = checker(state_id)
        dictionnary = state.to_dict()
        return jsonify(dict_state)
    states = storage.all(State)
    statesList = []
    for state in states.values():
        statesList.append(state.to_dict())
    return jsonify(statesList)


def delState(state_id):
    """ Delete the state with the state_id """
    if state_id is not None:
        state = checker(state_id)
        if not obj:
            return make_response(jsonify({"error": "Not Found"}), 404)
        storage.delete(state)
        storage.save()
        return make_response(jsonify({}), 200)
