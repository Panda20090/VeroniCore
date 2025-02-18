# authentication.py
# This script provides middleware for handling user authentication in the VeroniCore project.
# It includes functions to protect routes by verifying JWT tokens and ensuring that users are authenticated.

from functools import wraps
from flask import request, jsonify
import jwt

# Assuming the secret key is stored in an environment variable for security
SECRET_KEY = 'your_secret_key_here'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Check if token is passed in request headers
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            # Decode the token to get the user information
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['username']  # Extract the username from the token
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401

        # Add the current user to the request context
        return f(current_user, *args, **kwargs)

    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['username']
            user_role = data.get('role')

            if user_role != 'admin':
                return jsonify({'error': 'Admin access required!'}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
