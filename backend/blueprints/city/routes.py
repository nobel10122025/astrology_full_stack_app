from flask import jsonify, request, Blueprint
from .service import get_cities_list

cities_bp = Blueprint('city', __name__)

@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    query = request.get_json()
    city_list = get_cities_list(query)
    return jsonify(city_list), 200