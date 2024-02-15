#!/usr/bin/python3
''' RESTF API blueprint for User class '''

from flask import Flask, jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User, db


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    users = [usr.to_dict() for usr in User.query.all()]
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_by_id(user_id):
    ''' returns user with maching given id '''
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    ''' deletes user object with given user_id '''
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return (jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_new_user():
    ''' creates new user object using given data '''
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    elif "email" not in data:
        return make_response(jsonify({"error": "Missing email"}), 400)
    elif "password" not in data:
        return make_response(jsonify({"error": "Missing password"}), 400)
    else:
        obj = User(**data)
        db.session.add(obj)
        db.session.commit()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """update existing user object"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = User.query.filter_by(id=user_id).first()
    if obj is None:
        abort(404)
    keys = ["id", "email", "created_at", "updated_at"]
    for key in data.keys():
        if key not in keys:
            setattr(obj, key, data[keys])
    db.session.add(obj)
    db.session.commit()
    return (jsonify(obj.to_dict()), 201)
