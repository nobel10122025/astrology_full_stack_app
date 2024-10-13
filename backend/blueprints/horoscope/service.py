from others.astrology import AstrologyService
from .utils import planets, find_star, house_name


def format_stars_planet(planet_position):
    updated_list = []
    for i in planets:
        star_name = find_star(planet_position[i].get("current_sign"), planet_position[i].get("normDegree"))
        updated_object = planet_position[i]
        updated_object["star"] = star_name
        updated_object["rasi"] = house_name[planet_position[i].get("current_sign")]
        updated_list.append(updated_object)
    return updated_list

def generate_horoscope_from_api(birth_details):
    astrology_data = AstrologyService()
    response_generated = astrology_data.generate_horoscope(birth_details)
    if response_generated:
        required_list = response_generated.get("output")
        updated_json = format_stars_planet(required_list[1])
    return updated_json
    