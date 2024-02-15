#!/usr/bin/python3
''' RESTF API blueprint for Solution class '''

from flask import Flask, jsonify, abort, request, make_response
from api.v1.views import app_views
from models.solution import Solution, db


@app_views.route('/solutions', methods=['GET'], strict_slashes=False)
def get_all_solutions():
    solutions = [sol.to_dict() for sol in Solution.query.all()]
    return jsonify(solutions)


@app_views.route('/solutions/<sol_id>', methods=['GET'], strict_slashes=False)
def get_solution_by_id(sol_id):
    ''' returns solution with maching given id '''
    solution = Solution.query.filter_by(id=sol_id).first()
    if solution is None:
        abort(404)
    return jsonify(solution.to_dict())


@app_views.route('/solutions/<sol_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_solution(sol_id):
    ''' deletes solution object with given sol_id '''
    solution = Solution.query.filter_by(id=sol_id).first()
    if solution is None:
        abort(404)
    db.session.delete(solution)
    db.session.commit()
    return (jsonify({}), 200)


@app_views.route('/solutions', methods=['POST'], strict_slashes=False)
def create_new_solution():
    ''' creates new solution object using given data '''
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    elif "title" not in data:
        return make_response(jsonify({"error": "Missing title"}), 400)
    elif "description" not in data:
        return make_response(jsonify({"error": "Missing description"}), 400)
    else:
        obj = Solution(**data)
        db.session.add(obj)
        db.session.commit()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/solutions/<sol_id>', methods=['PUT'], strict_slashes=False)
def update_solution(sol_id):
    """update existing solution object"""
    data = request.get_json()
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = Solution.query.filter_by(id=sol_id).first()
    if obj is None:
        abort(404)
    keys = ["id", "created_at", "updated_at"]
    for key in data.keys():
        if key not in keys:
            setattr(obj, key, data[keys])
    db.session.add(obj)
    db.session.commit()
    return (jsonify(obj.to_dict()), 201)
