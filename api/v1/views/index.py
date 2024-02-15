#!/usr/bin/python3
''' flask blueprint module '''

from flask import jsonify
from api.v1.views import app_views
from models import classes


@app_views.route("/status")
def get_status():
    ''' returns JSON of OK status for status route '''
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def storage_stats():
    stats = {}
    for key, value in classes.items():
        stats[key] = value.query.count()
    return jsonify(stats)
