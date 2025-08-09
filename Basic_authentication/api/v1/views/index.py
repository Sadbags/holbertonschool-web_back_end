#!/usr/bin/env python3
"""
Index views module for the API.

This module defines a set of endpoints for:
- Checking API status (`/status`)
- Retrieving statistics (`/stats/`)
- Testing authentication error responses (`/unauthorized` and `/forbidden`)

It uses the Flask `app_views` blueprint, meaning these routes
will be prefixed with `/api/v1` when registered in the main app.
"""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    Status endpoint.

    GET /api/v1/status
    ------------------
    Purpose:
        - Simple health check endpoint to verify that the API is running.

    Returns:
        JSON response:
            {
                "status": "OK"
            }
    HTTP status code:
        200 OK
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    Statistics endpoint.

    GET /api/v1/stats/
    ------------------
    Purpose:
        - Returns basic statistics about the application,
          specifically counts of stored resources.

    Process:
        - Imports the `User` model dynamically (to avoid circular imports).
        - Calls `User.count()` to retrieve the total number of user objects.

    Returns:
        JSON response:
            {
                "users": <number_of_users>
            }
    HTTP status code:
        200 OK
    """
    from models.user import User  # Local import to avoid circular dependency
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """
    Unauthorized endpoint (for testing purposes).

    GET /api/v1/unauthorized
    ------------------------
    Purpose:
        - Forces the API to return an HTTP 401 Unauthorized error.
        - Useful for testing authentication logic and error handling.

    Returns:
        - No body content (the `abort()` function sends a default error response).
    HTTP status code:
        401 Unauthorized
    """
    return abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """
    Forbidden endpoint (for testing purposes).

    GET /api/v1/forbidden
    ---------------------
    Purpose:
        - Forces the API to return an HTTP 403 Forbidden error.
        - Useful for testing permission handling and error responses.

    Returns:
        - No body content (the `abort()` function sends a default error response).
    HTTP status code:
        403 Forbidden
    """
    return abort(403)
