"""
Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status
    Returns:
        - the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route("/unauthorized", methods=["GET"])
def unauthorized():
    """GET /api/v1/unauthorized
    Raises:
        - 401 error to test unauthorized error handler
    """
    abort(401)

@app_views.route('/stats', strict_slashes=False)
def stats() -> str:
    """GET /api/v1/stats
    Returns:
        - the number of each object
    """
    from models.user import User
    stats = {"users": User.count()}
    return jsonify(stats)

