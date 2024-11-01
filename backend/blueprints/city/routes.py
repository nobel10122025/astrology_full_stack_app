from flask import jsonify, request, Blueprint
from .service import get_cities_list

cities_bp = Blueprint('city', __name__)

@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    city_name = request.args.get('name')
    city_list = get_cities_list(city_name)
    return jsonify(city_list), 200