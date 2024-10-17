from others.astrology import AstrologyService
from .utils import planets, find_star, house_name, get_first_house, get_house_lord_star_karma, house_name_lords


def format_stars_planet(planet_position):
    updated_list = []
    for i in planets:
        star_name = find_star(planet_position[i].get("current_sign"), planet_position[i].get("normDegree"))
        updated_object = planet_position[i]
        updated_object["star"] = star_name
        updated_object["rasi"] = house_name[planet_position[i].get("current_sign")]
        updated_object["name"] = i
        updated_list.append(updated_object)
    return updated_list

def get_house_karma(planet_list, house_count):
    karma_list = []
    user_first_house = get_first_house(planet_list)
    if user_first_house + house_count >= 14: required_house_name = house_name[(user_first_house + house_count) - 13]
    else: required_house_name = house_name[(user_first_house + house_count)-1]
    house_lord = house_name_lords[required_house_name]
    karma_list.append(get_house_lord_star_karma(house_lord, planet_list))
    return karma_list

def generate_horoscope_from_api(birth_details, house_number):
    astrology_data = AstrologyService()
    response_generated = astrology_data.generate_horoscope(birth_details)
    if response_generated:
        required_list = response_generated.get("output")
        updated_json = format_stars_planet(required_list[1])
        karma_list = get_house_karma(updated_json, house_number)
        print("karma list", karma_list)
    return updated_json
    