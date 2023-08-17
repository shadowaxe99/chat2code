from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/data')
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)