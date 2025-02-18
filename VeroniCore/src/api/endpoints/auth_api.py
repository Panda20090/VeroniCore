# auth_api.py
# This script defines the authentication-related API endpoints for the VeroniCore project.
# It handles user authentication, including login, token generation, and token verification.

from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# In-memory user database (for demonstration purposes)
users_db = {
    'testuser': {'password': 'pbkdf2:sha256:150000$abcdefgh$examplehashedpassword'}
}

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password.'}), 401

    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

@app.route('/api/auth/verify_token', methods=['POST'])
def verify_token():
    token = request.get_json().get('token')

    if not token:
        return jsonify({'error': 'Token is missing.'}), 400

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': 'Token is valid.', 'data': decoded}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token.'}), 401

@app.route('/api/auth/refresh_token', methods=['POST'])
def refresh_token():
    token = request.get_json().get('token')

    if not token:
        return jsonify({'error': 'Token is missing.'}), 400

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'], options={"verify_exp": False})
        new_token = jwt.encode({
            'username': decoded['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')

        return jsonify({'token': new_token}), 200
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token.'}), 401

if __name__ == "__main__":
    app.run(debug=True)
