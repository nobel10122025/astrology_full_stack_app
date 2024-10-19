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

planet_karma_mapping = {
    "Sun": "Jupiter",
    "Moon": "Jupiter",
    "Mars": "Jupiter",
    "Ketu": "Sun",
    "Mercury": "Saturn",
    "Jupiter": "Rahu",
    "Venus": "Moon",
    "Rahu": "Moon",
    "Saturn": "Mars",
}

house_karma_lords = {
    1: "Jupiter",
    2: "Jupiter",
    3: None,
    4: None,
    5: "Jupiter",
    6: "Saturn",
    7: "Moon",
    8: None,
    9: "Rahu",
    10: None,
    11: "Mars",
    12: "Sun"
}