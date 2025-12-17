from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return jsonify({"message": "API is running"})

@api.route('/health')
def health():
    return jsonify({"status": "healthy"})


@api.route('/status')
def status():
    return jsonify({"status": "CI/CD pipeline working!", "version": "1.0"})
# Add your other routes here
# Example:
# @api.route('/items', methods=['GET'])
# def get_items():
#     return jsonify({"items": []})
