from others.astrology import AstrologyService
from .utils import find_star, get_first_house, get_house_lord_star_karma, get_house_lord_saram_karma, get_house_lord_bavam_karma, get_planets_karma, get_planets_houses_karma, get_house_lord_conjuction_karma, get_user_house_karma, get_aspecting_planet_karma
from .constants import planets, house_name, house_name_lords, star_owner_mapping


def format_stars_planet(planet_position):
    updated_list = []
    for i in planets:
        star_name = find_star(planet_position[i].get("current_sign"), planet_position[i].get("normDegree"))
        updated_object = planet_position[i]
        updated_object["star"] = star_name
        updated_object["rasi"] = house_name[planet_position[i].get("current_sign")]
        updated_object["name"] = i
        updated_object["star_lord"] = star_owner_mapping[star_name]
        updated_list.append(updated_object)
    return updated_list

def get_house_karma(planet_list, house_count):
    karma_list = []
    user_first_house = get_first_house(planet_list)
    if user_first_house + house_count >= 14: required_house_name = house_name[(user_first_house + house_count) - 13]
    else: required_house_name = house_name[(user_first_house + house_count)-1]
    house_lord = house_name_lords[required_house_name]
    karma_list.append(get_house_lord_star_karma(house_lord, planet_list))
    karma_list = karma_list + get_house_lord_saram_karma(house_lord, planet_list, user_first_house)
    karma_list = karma_list + get_house_lord_bavam_karma(house_lord, planet_list, user_first_house)
    karma_list = karma_list + get_planets_houses_karma(house_lord, planet_list, user_first_house, house_count)
    karma_list = karma_list + get_user_house_karma(user_first_house, house_count)
    karma_list = karma_list + get_house_lord_conjuction_karma(house_lord, planet_list, user_first_house)
    karma_list = karma_list + get_aspecting_planet_karma(house_lord, planet_list, user_first_house, house_count)
    karma_list = karma_list + get_planets_karma(house_lord, planet_list, user_first_house, house_count)
    return karma_list

def generate_horoscope_from_api(birth_details):
    chart_generated = None
    astrology_data = AstrologyService()
    response_generated = astrology_data.generate_horoscope(birth_details)
    if (birth_details["generate_chart"]): chart_generated = astrology_data.generate_horoscope_chart(birth_details)
    if response_generated:
        required_list = response_generated.get("output")
        updated_planet_list = format_stars_planet(required_list[1])
        karma_list = []
        for i in range(1,13): 
            house_karma_list = get_house_karma(updated_planet_list, i)
            if (i == 1): house_karma_list.insert(1,get_house_lord_star_karma("Ascendant", updated_planet_list))
            karma_list.append({ i: house_karma_list })
    if (chart_generated): return {"planet_position" : updated_planet_list, "karma_list": karma_list, "chart": chart_generated["output"]}
    return {"planet_position" : updated_planet_list, "karma_list": karma_list, "chart": ""}
    