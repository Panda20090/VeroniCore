# error_handler.py
# This script provides custom error handling for the VeroniCore project.
# It defines how the application should respond to different types of errors, such as 404 Not Found and 500 Internal Server Error.

from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested resource could not be found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An internal server error occurred.'}), 500

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad Request', 'message': 'The request could not be understood or was missing required parameters.'}), 400

@app.errorhandler(401)
def unauthorized_error(error):
    return jsonify({'error': 'Unauthorized', 'message': 'Authentication is required and has failed or has not yet been provided.'}), 401

@app.errorhandler(403)
def forbidden_error(error):
    return jsonify({'error': 'Forbidden', 'message': 'You do not have permission to access the requested resource.'}), 403

@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({'error': 'Method Not Allowed', 'message': 'The method is not allowed for the requested URL.'}), 405

@app.errorhandler(Exception)
def handle_unexpected_error(error):
    return jsonify({'error': 'Unexpected Error', 'message': str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)
