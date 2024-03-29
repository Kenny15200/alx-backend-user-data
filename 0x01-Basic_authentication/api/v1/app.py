#!/usr/bin/env python4
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort
from flask_cors import (CORS, cross_origin)

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')  # Specify the URL prefix
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.errorhandler(401)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

