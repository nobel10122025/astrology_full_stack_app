import requests
import json
import os

# Load environment variables from .env file

class AstrologyService:
    def __init__(self):
        self.url = "https://json.freeastrologyapi.com/planets"
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': os.getenv("ASTROLOGY_API_KEY")
        }

    def generate_horoscope(self, payload):
        print("paylaoad", payload)
        response = requests.request("POST", url=self.url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
                return response.json()
        return False