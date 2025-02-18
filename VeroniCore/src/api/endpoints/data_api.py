# data_api.py
# This script defines the data-related API endpoints for the VeroniCore project.
# It handles operations such as data retrieval, storage, and processing.

from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# Path to data storage (for demonstration purposes)
DATA_STORAGE_PATH = os.path.join(os.getcwd(), "data_storage")

# Ensure the data storage directory exists
os.makedirs(DATA_STORAGE_PATH, exist_ok=True)

@app.route('/api/data/upload', methods=['POST'])
def upload_data():
    data = request.get_json()
    data_id = data.get('id')
    content = data.get('content')

    if not data_id or not content:
        return jsonify({'error': 'Data ID and content are required.'}), 400

    file_path = os.path.join(DATA_STORAGE_PATH, f"{data_id}.json")
    
    with open(file_path, 'w') as data_file:
        json.dump(content, data_file)

    return jsonify({'message': f'Data with ID {data_id} uploaded successfully.'}), 201

@app.route('/api/data/retrieve/<data_id>', methods=['GET'])
def retrieve_data(data_id):
    file_path = os.path.join(DATA_STORAGE_PATH, f"{data_id}.json")

    if not os.path.exists(file_path):
        return jsonify({'error': 'Data not found.'}), 404

    with open(file_path, 'r') as data_file:
        content = json.load(data_file)

    return jsonify({'data_id': data_id, 'content': content}), 200

@app.route('/api/data/update/<data_id>', methods=['PUT'])
def update_data(data_id):
    file_path = os.path.join(DATA_STORAGE_PATH, f"{data_id}.json")

    if not os.path.exists(file_path):
        return jsonify({'error': 'Data not found.'}), 404

    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Content is required for update.'}), 400

    with open(file_path, 'w') as data_file:
        json.dump(content, data_file)

    return jsonify({'message': f'Data with ID {data_id} updated successfully.'}), 200

@app.route('/api/data/delete/<data_id>', methods=['DELETE'])
def delete_data(data_id):
    file_path = os.path.join(DATA_STORAGE_PATH, f"{data_id}.json")

    if not os.path.exists(file_path):
        return jsonify({'error': 'Data not found.'}), 404

    os.remove(file_path)
    return jsonify({'message': f'Data with ID {data_id} deleted successfully.'}), 200

if __name__ == "__main__":
    app.run(debug=True)
