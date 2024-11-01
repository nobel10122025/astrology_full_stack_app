from .model.cities_model import Cities
import logging

def get_cities_list(query):
    cities = []
    try:
        cities_list = Cities.objects(city__regex=f'(?i)^{query}').limit(10)
        for current_city in cities_list:
            cities.append({
                "name": current_city.city,
                "lat": current_city.lat,
                "long": current_city.lng,
                "_id": current_city._id
            })
    except Exception as e:
        logging.error(f"Connection failed: {e}")
    return cities
        