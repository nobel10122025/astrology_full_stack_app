import requests
import json
import os

# Load environment variables from .env file

class AstrologyService:
    def __init__(self):
        self.url = "https://json.freeastrologyapi.com"
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': os.getenv("ASTROLOGY_API_KEY")
        }

    def generate_horoscope(self, payload):
        response = requests.request("POST", url=f"{self.url}/planets", headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
                return response.json()
        return False
    
    def generate_horoscope_chart(self, payload):
        response = requests.request("POST", url="https://json.apiastro.com/horoscope-chart-url", headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
                return response.json()
        return False