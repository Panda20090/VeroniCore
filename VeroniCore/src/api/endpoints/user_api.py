# user_api.py
# This script defines the user-related API endpoints for the VeroniCore project.
# It handles user authentication, profile management, and other user-specific functionalities.

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# In-memory user database (for demonstration purposes)
users_db = {}

@app.route('/api/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if username in users_db:
        return jsonify({'error': 'Username already exists.'}), 409

    # Hash the password for security
    hashed_password = generate_password_hash(password, method='sha256')
    users_db[username] = {'password': hashed_password}
    
    return jsonify({'message': f'User {username} registered successfully.'}), 201

@app.route('/api/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password.'}), 401

    return jsonify({'message': f'User {username} logged in successfully.'}), 200

@app.route('/api/users/profile', methods=['GET'])
def get_user_profile():
    username = request.args.get('username')

    if not username or username not in users_db:
        return jsonify({'error': 'User not found.'}), 404

    # For demonstration, returning a simple profile
    profile = {
        'username': username,
        'bio': 'This is a sample user bio.',
        'preferences': {'theme': 'dark', 'notifications': True}
    }

    return jsonify({'profile': profile}), 200

@app.route('/api/users/update_profile', methods=['PUT'])
def update_user_profile():
    data = request.get_json()
    username = data.get('username')
    bio = data.get('bio')
    preferences = data.get('preferences')

    if not username or username not in users_db:
        return jsonify({'error': 'User not found.'}), 404

    # Update the profile information
    profile = {
        'username': username,
        'bio': bio if bio else 'This is a sample user bio.',
        'preferences': preferences if preferences else {'theme': 'dark', 'notifications': True}
    }

    return jsonify({'message': 'Profile updated successfully.', 'profile': profile}), 200

if __name__ == "__main__":
    app.run(debug=True)
