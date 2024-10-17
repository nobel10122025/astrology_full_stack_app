planets = ["Ascendant",
           "Saturn", 
           "Jupiter", 
           "Moon", 
           "Sun", 
           "Venus", 
           "Ketu", 
           "Rahu",
           "Mars", 
           "Mercury"]
karmas = ["Sun", "Moon", "Mars", "Saturn", "Venus", "Mercury", "Rahu", "Jupiter"]

house_star_mapping= {
    1: ["Ashwini", "Bharani", "Krittika"],
    2: ["Krittika", "Rohini", "Mrigashirsa"],
    3: ["Mrigashirsa", "Thiruvathirai", "PunarPoosam"],
    4: ["PunarPoosam", "Poosam", "Ayilyam"],
    5: ["Maham", "Pooram", "Uthiram"],
    6: ["Uthiram", "Astham", "Chitirai"],
    7: ["Chitirai", "Suvathi", "Visakam"],
    8: ["Visakam", "Anusam", "Kettai"],
    9: ["Moolam", "Pooradam", "Uthiradam"],
    10: ["Uthiradam", "Thiruvonam", "Avittam"],
    11: ["Avittam", "Sathayam", "Poorattaathi"],
    12: ["Poorattaathi", "Uthirattaathi", "Revathi"]
}

house_name = {
    1: 'Mesham',
    2: 'Rishabam',
    3: 'Midunam',
    4: 'Kadagam',
    5: 'Simmum',
    6: 'Kanni',
    7: 'Thulam',
    8: 'Viruchigam',
    9: 'Dhanusu',
    10: 'Magaram',
    11: 'Kumbam',
    12: 'Meenam'
}
first_type = [1, 5, 9]
second_type = [2, 6, 10]
third_type= [3, 7, 11]
fourth_type = [4, 8, 12]

house_name_lords = {
    "Mesham": "Mars",
    "Rishabam": "Venus",
    "Midunam": "Mercury",
    "Kadagam": "Moon",
    "Simmum": "Sun",
    "Kanni": "Mercury",
    "Thulam": "Venus",
    "Viruchigam": "Mars",
    "Dhanusu": "Jupiter",
    "Magaram": "Saturn",
    "Kumbam": "Saturn",
    "Meenam": "Jupiter"
}

karma_star_mapping = {
    "Sun": ["Ashwini", "Ayilyam", "Anusam", "Poorattaathi"],
    "Moon": ["Bharani", "Maham", "Kettai", "Uthirattaathi"],
    "Mars": ["Krittika", "Pooram", "Moolam", "Revathi"],
    "Jupiter": ["Mrigashirsa", "Astham", "Uthiradam"],
    "Saturn":["PunarPoosam", "Suvathi", "Avittam"],
    "Mercury": ["Rohini", "Uthiram", "Pooradam"],
    "Venus": ["Thiruvonam", "Thiruvathirai", "Chitirai"],
    "Rahu": ["Sathayam", "Poosam", "Visakam"],
}

star_owner_mapping = {
    "Ashwini": "Ketu",
    "Bharani": "Venus",
    "Krittika": "Sun",
    "Mrigashirsa": "Mars",
    "PunarPoosam": "Jupiter",
    "Rohini": "Moon",
    "Thiruvonam": "Moon",
    "Sathayam": "Rahu",
    "Ayilyam": "Mercury",
    "Anusam": "Saturn",
    "Poorattaathi": "Jupiter",
    "Maham": "Ketu",
    "Kettai": "Mercury",
    "Uthirattaathi": "Saturn",
    "Pooram": "Venus",
    "Moolam": "Ketu",
    "Revathi": "Mercury",
    "Astham": "Moon",
    "Uthiradam": "Sun",
    "Suvathi": "Rahu",
    "Avittam": "Mars",
    "Uthiram": "Sun",
    "Pooradam": "Venus",
    "Thiruvathirai": "Rahu",
    "Chitirai": "Mars",
    "Poosam": "Saturn",
    "Visakam": "Jupiter"
}

planet_owning_house = {
    "Sun": [5],
    "Moon": [4],
    "Venus": [2, 7],
    "Mercury": [3, 6],
    "Jupiter": [9, 12],
    "Saturn": [10, 11],
    "Mars": [1, 8],
    "Rahu": [],
    "Ketu": []
}

bavam_karma_mapping = {
    12: "Sun",
    11: "Mars",
    10: None,
    9: "Rahu",
    8: None,
    7: "Moon",
    6: "Saturn",
    5: "Jupiter",
    4: "Mercury",
    3: "Venus",
    2: "Jupiter",
    1: "Jupiter"
}

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

def get_house_lord_star_karma(house_lord, planet_list):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord: 
            current_star = current_planet["star"]
            for karma in karmas:
                if current_star in karma_star_mapping[karma]: return {"name": karma, "reason": f'House lord ({house_lord}) is in {current_star}'}

def get_house_lord_saram_karma(house_lord, planet_list, users_first_house):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord: 
            star_owner = star_owner_mapping[current_planet["star"]]
            owning_houses = planet_owning_house[star_owner]
            bavan_house_list = []
            karma_list = []
            for houses_no in owning_houses:
                user_house_count = get_planets_current_house(houses_no, users_first_house)
                bavan_house_list.append(user_house_count)
            for house_no in bavan_house_list: 
                if house_no == 6: karma_list.append({"name": "Moon", "reason": f'{house_lord} is on the saram of {house_no} lord'})
                if bavam_karma_mapping[house_no]: karma_list.append({"name": bavam_karma_mapping[house_no], "reason": f'{house_lord} is on the saram of {house_no} lord'})
            return karma_list

def get_house_lord_bavam_karma(house_lord, planet_list, users_first_house):
    for current_planet in planet_list:
        if current_planet["name"] == house_lord:
            planets_current_sign = current_planet["current_sign"]
            print("current_planet", current_planet)
            planets_position = get_planets_current_house(planets_current_sign, users_first_house)
            print("planets_position", planets_position)
            karma_list =[]
            if planets_position == 6: karma_list.append({"name": "Moon", "reason": f'{house_lord} is currently in {planets_position}'})
            if bavam_karma_mapping[planets_position]: karma_list.append({"name": bavam_karma_mapping[planets_position], "reason": f'{house_lord} is currently in {planets_position} house'})
            return karma_list


