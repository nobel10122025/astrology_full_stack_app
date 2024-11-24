from flask import jsonify, request, Blueprint
from .service import generate_horoscope_from_api

horoscope_bp = Blueprint('horoscope', __name__)

@horoscope_bp.route('/generate_horoscope', methods=['POST'])
def generate_horoscope_astro():
    birth_details = request.get_json()
    requested_house = birth_details["updated_house"]
    generated_results = generate_horoscope_from_api(birth_details, requested_house)
    return jsonify(generated_results), 200