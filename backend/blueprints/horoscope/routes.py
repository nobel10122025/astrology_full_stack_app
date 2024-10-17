from flask import jsonify, request, Blueprint
from .service import generate_horoscope_from_api

horoscope_bp = Blueprint('horoscope', __name__)

@horoscope_bp.route('/get_house_details', methods=['POST'])
def generate_horoscope_astro():
    birth_details = request.get_json()
    house_number = birth_details["house_number"]
    generated_results = generate_horoscope_from_api(birth_details, house_number)
    return jsonify(generated_results), 200