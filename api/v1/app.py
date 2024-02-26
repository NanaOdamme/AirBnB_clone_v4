#!/usr/bin/python3
"""
This module contains the principal application
"""
from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors with a JSON response"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown method to close the storage"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = (getenv('HBNB_API_PORT', default=5000))

    app.run(host=host, port=port, threaded=True)
