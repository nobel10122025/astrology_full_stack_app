from .constants import first_type, second_type, third_type, fourth_type, house_star_mapping, karmas, karma_star_mapping, star_owner_mapping, planet_owning_house, planet_karma_mapping, bavam_karma_mapping, house_karma_lords, aspecting_houses

def get_star_position(degree):
    if degree > 0 and degree < 03.2: return 1
    if degree > 3.2 and degree < 6.4: return 2
    if degree > 6.4 and degree < 10: return 3
    if degree > 10 and degree < 13.2: return 4    
    if degree > 13.2 and degree < 16.4: return 5
    if degree > 16.4 and degree < 20.0: return 6
    if degree > 20 and degree < 23.2: return 7
    if degree > 23.2 and degree < 26.4: return 8
    if degree > 26.4 and degree < 30: return 9

def find_star(house_count, degree):
    star_count = get_star_position(degree)
    if house_count in first_type:
        if star_count <= 4: return house_star_mapping.get(house_count)[0]
        if star_count >= 5 and star_count <= 8: return house_star_mapping.get(house_count)[1]
        else: return house_star_mapping.get(house_count)[2]
    if house_count in second_type:
        if star_count <= 3: return house_star_mapping.get(house_count)[0]
        if star_count >= 3 and star_count <= 7: return house_star_mapping.get(house_count)[1]
        else: return house_star_mapping.get(house_count)[2]
    if house_count in third_type:
        if star_count <= 2: return house_star_mapping.get(house_count)[0]
        if star_count >= 2 and star_count <= 6: return house_star_mapping.get(house_count)[1]
        else: return house_star_mapping.get(house_count)[2]
    if fourth_type.count(house_count) > 0:
        if star_count <= 1: return house_star_mapping.get(house_count)[0]
        if star_count > 1 and star_count <= 5: return house_star_mapping[house_count][1]
        else: return house_star_mapping.get(house_count)[2]

def get_first_house(planet_list):  
    for current_planet in planet_list:
        if current_planet["name"] == "Ascendant": return current_planet["current_sign"]

def get_planets_current_house(planets_current_sign, users_first_house):
    if (planets_current_sign - users_first_house) == 0:  return 1
    elif (planets_current_sign - users_first_house) > 0: return (planets_current_sign - users_first_house + 1)
    else: return (13 - abs(planets_current_sign - users_first_house))

def get_aspecting_houses(planets_current_sign):
    house_list = []
    for house_no in  aspecting_houses:
        if planets_current_sign - house_no == 0: house_list.append(12)
        elif planets_current_sign - house_no > 0: house_list.append(planets_current_sign - house_no)
        else: house_list.append(12-abs(planets_current_sign - house_no)) 
    return house_list

def get_house_lord_star_karma(house_lord, planet_list):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord: 
            current_star = current_planet["star"]
            for karma in karmas:
                if current_star in karma_star_mapping[karma]: return {
                    "name": karma, 
                    "reason": f'House lord ({house_lord}) is in {current_star}',
                    "level": "very_strong"
                }

def get_house_lord_saram_karma(house_lord, planet_list, users_first_house):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord: 
            star_owner = star_owner_mapping[current_planet["star"]]
            owning_houses = planet_owning_house[star_owner]
            bavan_house_list = []
            karma_list = []
            if star_owner == "Ketu" or star_owner == "Rahu":
                if star_owner == "Ketu":
                    karma_list.append({
                        "name": "Sun", 
                        "reason": f'{house_lord} is on the saram of Ketu',
                        "level": "strong"
                        })
                else:
                    karma_list.append({
                        "name": "Moon", 
                        "reason": f'{house_lord} is on the saram of Rahu',
                        "level": "strong"
                        })
            for houses_no in owning_houses:
                user_house_count = get_planets_current_house(houses_no, users_first_house)
                bavan_house_list.append(user_house_count)
            for house_no in bavan_house_list: 
                if house_no == 6: karma_list.append({
                    "name": "Moon", 
                    "reason": f'{house_lord} is on the saram of {house_no} lord',
                    "level": "strong"
                    })
                if bavam_karma_mapping[house_no]: karma_list.append({
                    "name": bavam_karma_mapping[house_no], 
                    "reason": f'{house_lord} is on the saram of {house_no} lord',
                    "level": "strong"
                    })
            return karma_list

def get_house_lord_bavam_karma(house_lord, planet_list, users_first_house):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord:
            planets_current_sign = current_planet["current_sign"]
            planets_position = get_planets_current_house(planets_current_sign, users_first_house)
            karma_list =[]
            if planets_position == 6: karma_list.append({
                    "name": "Moon", 
                    "reason": f'{house_lord} (house lord) is currently in {planets_position}',
                    "level": "strong"
                })
            if bavam_karma_mapping[planets_position]: karma_list.append({
                "name": bavam_karma_mapping[planets_position], 
                "reason": f'{house_lord} (house lord) is currently in {planets_position} house',
                "level": "strong"
                })
            return karma_list

def get_planets_karma(_, planet_list, users_first_house, user_requested_house):
    karma_list = []
    for planet in planet_list:
        planets_position = get_planets_current_house(planet["current_sign"], users_first_house)
        if user_requested_house == planets_position:
            planet_name = planet["name"]
            if planet_name != "Ascendant": karma_list.append({
                "name": planet_karma_mapping[planet_name], 
                "reason": f'{planet_name} is in this {user_requested_house} house',
                "level": "negligible"
            })
    return karma_list

def get_planets_houses_karma(_, planet_list, users_first_house, user_requested_house):
    karma_list = []
    for planet in planet_list:
        planets_position = get_planets_current_house(planet["current_sign"], users_first_house)
        if user_requested_house == planets_position:
            planet_name = planet["name"]
            if planet_name != "Ascendant":
                owning_houses = planet_owning_house[planet_name]
                bavan_house_list = []
                for houses_no in owning_houses:
                    user_house_count = get_planets_current_house(houses_no, users_first_house)
                    bavan_house_list.append(user_house_count)
                for house_no in bavan_house_list: 
                    if house_no == 6: karma_list.append(
                        {
                            "name": "Moon", 
                            "reason": f'{user_requested_house} house has the {planet_name} whose is the owner of {house_no}', 
                            "level": "medium"
                        })
                    if bavam_karma_mapping[house_no]: karma_list.append(
                        {
                            "name": bavam_karma_mapping[house_no], 
                            "reason": f'{user_requested_house} house has the {planet_name} whose is the owner of {house_no}',
                            "level": "medium"
                        })
    return karma_list

def get_house_lord_conjuction_karma(house_lord ,planet_list, users_first_house):
    house_lord_no = None
    house_lord_degree = None
    for current_planet in planet_list:
        if current_planet["name"] == house_lord: 
            house_lord_no = get_planets_current_house(current_planet["current_sign"], users_first_house)
            house_lord_degree = current_planet["normDegree"]
    karma_list = []
    for planet in planet_list:
        planets_position = get_planets_current_house(planet["current_sign"], users_first_house)
        if house_lord_no == planets_position:
            planet_name = planet["name"]
            if planet_name != "Ascendant" and planet_name != house_lord:
                owning_houses = planet_owning_house[planet_name]
                bavan_house_list = []
                for houses_no in owning_houses:
                    user_house_count = get_planets_current_house(houses_no, users_first_house)
                    bavan_house_list.append(user_house_count)
                for house_no in bavan_house_list: 
                    if house_no == 6: karma_list.append(
                        {
                            "name": "Moon", 
                            "reason": f'house lord is with {planet_name} whose is the owner of {house_no}',
                            "level": "medium",
                            "conjunction": get_degree_difference(house_lord_degree, planet["normDegree"])
                        })
                    if bavam_karma_mapping[house_no]: karma_list.append(
                        {
                            "name": bavam_karma_mapping[house_no], 
                            "reason": f'house lord is with {planet_name} whose is the owner of {house_no}',
                            "level": "medium",
                            "conjunction": get_degree_difference(house_lord_degree, planet["normDegree"])
                        })
            if(planet_name != "Ascendant" and planet_karma_mapping[planet_name] and planet_name != house_lord): karma_list.append(
                {
                    "name": planet_karma_mapping[planet_name], 
                    "reason": f'house lord is with {planet_name}',
                    "level": "low",
                    "conjunction": get_degree_difference(house_lord_degree, planet["normDegree"])
                })
    return karma_list
    
def get_user_house_karma(user_first_house, house_count):
    if user_first_house + house_count >= 14: required_house_count =(user_first_house + house_count) - 13
    else: required_house_count = (user_first_house + house_count)-1
    karma_list = []
    if (house_karma_lords[required_house_count]):
        karma_list.append({
            "name": house_karma_lords[required_house_count],
            "reason": f"your current house is {required_house_count} from Aries",
            "level": "medium"
        })
    if (required_house_count == 6):
        karma_list.append({
            "name": "Moon",
            "reason": f"your current house is {required_house_count} from Aries",
            "level": "medium"
        })
    return karma_list

def get_aspecting_planet_karma(_, planet_list, users_first_house, user_requested_house):
    karma_list = []
    aspecting_houses = get_aspecting_houses(user_requested_house)
    for planet in planet_list:
        if planet["name"] != "Ascendant" and planet["name"] != "Ketu" and planet["name"] != "Rahu":
            planets_position = get_planets_current_house(planet["current_sign"], users_first_house)
            if ((aspecting_houses[0] == planets_position or aspecting_houses[6] == planets_position) and planet["name"] == "Saturn"):
                get_planets_owning_house(planet["name"], users_first_house, karma_list, planets_position, user_requested_house)
            elif ((aspecting_houses[1] == planets_position or aspecting_houses[4] == planets_position) and planet["name"] == "Mars"):
                get_planets_owning_house(planet["name"], users_first_house, karma_list, planets_position, user_requested_house)
            elif ((aspecting_houses[2] == planets_position or aspecting_houses[5] == planets_position) and planet["name"] == "Jupiter"):
                get_planets_owning_house(planet["name"], users_first_house, karma_list, planets_position, user_requested_house)
            if aspecting_houses[3] == planets_position:
                get_planets_owning_house(planet["name"], users_first_house, karma_list, planets_position, user_requested_house)
    return karma_list

def get_planets_owning_house(planet_name, users_first_house, karma_list, planets_position, user_requested_house):
    if(planet_name == "Rahu" or planet_name == "Ketu"): karma_list.append(
        {
            "name": "Moon" if planet_name == "Rahu" else "Sun", 
            "reason": f'{planet_name} is aspecting from {planets_position} house',
            "level": "very_low"
        })
    else :
        owning_houses = planet_owning_house[planet_name]
        bavan_house_list = []
        for houses_no in owning_houses:
            user_house_count = get_planets_current_house(houses_no, users_first_house)
            bavan_house_list.append(user_house_count)
        for current_house in bavan_house_list:
            if (current_house == 6): karma_list.append(
                {
                    "name": "Moon", 
                    "reason": f'{planet_name} which is in the {planets_position} is the lord of {current_house} is aspecting {user_requested_house}',
                    "level": "very_low"
                })
            if bavam_karma_mapping[current_house]: karma_list.append(
            {
                "name": bavam_karma_mapping[current_house], 
                "reason": f'{planet_name} which is in the {planets_position} is the lord of {current_house} is aspecting {user_requested_house}',
                "level": "very_low"
            })
    return karma_list

def get_degree_difference(house_lord_degree, planet_degree):
    diff_btw_planets = abs(house_lord_degree - planet_degree)
    if diff_btw_planets <= 5: return "high"
    if diff_btw_planets <= 10: return "low"
    return "negligible"
