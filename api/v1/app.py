#!/usr/bin/python3
'''app module for registering blueprint and creating flask application for
the student platform project api'''

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import db, classes
from api.v1.views import app_views
from os import getenv

User = classes['User']
Challenge = classes['Challenge']
app = Flask(__name__)
app.register_blueprint(app_views)
user = getenv('USER')
passwd = getenv('PASSWD')
dbs = getenv('DB')
uri = f'mysql://{user}:{passwd}@localhost/{dbs}'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})
db.init_app(app)
with app.app_context():
    db.create_all()


@app.errorhandler(404)
def resource_not_found(error):
    ''' returns not found response in JSON format '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("PLATFORM_API_HOST", "0.0.0.0")
    port = int(getenv("PLATFORM_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
