#!/usr/bin/python3
''' RESTF API blueprint for Challenge class '''

from flask import Flask, jsonify, abort, request, make_response
from api.v1.views import app_views
from models.challenge import Challenge, db


@app_views.route('/challenges', methods=['GET'], strict_slashes=False)
def get_all_challenges():
    """ returns all challenge class objects """
    challenges = [obj.to_dict() for obj in Challenge.query.all()]
    return jsonify(challenges)


@app_views.route('/challenges/<Chall_id>', methods=['GET'],
                 strict_slashes=False)
def get_challenge_by_id(Chall_id):
    ''' returns challenge with maching given id '''
    challenge = Challenge.query.filter_by(id=Chall_id).first()
    if challenge is None:
        abort(404)
    return jsonify(challenge.to_dict())


@app_views.route('/challenges/<Chall_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_challenge(Chall_id):
    ''' deletes challenge object with given Chall_id '''
    challenge = Challenge.query.filter_by(id=Chall_id).first()
    if challenge is None:
        abort(404)
    db.session.delete(challenge)
    db.session.commit()
    return (jsonify({}), 200)


@app_views.route('/challenges', methods=['POST'], strict_slashes=False)
def create_new_challenge():
    ''' creates new challenge object using given data '''
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    elif "title" not in data:
        return make_response(jsonify({"error": "Missing title"}), 400)
    elif "description" not in data:
        return make_response(jsonify({"error": "Missing description"}), 400)
    elif "topic" not in data:
        return make_response(jsonify({"error": "Missing topic"}), 400)
    else:
        obj = Challenge(**data)
        db.session.add(obj)
        db.session.commit()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/challenges/<Chall_id>', methods=['PUT'],
                 strict_slashes=False)
def update_challenge(Chall_id):
    """update existing challenge object"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = Challenge.query.filter_by(id=Chall_id).first()
    if obj is None:
        abort(404)
    keys = ["id", "created_at", "updated_at"]
    for key in data.keys():
        if key not in keys:
            setattr(obj, key, data[keys])
    db.session.add(obj)
    db.session.commit()
    return (jsonify(obj.to_dict()), 201)
