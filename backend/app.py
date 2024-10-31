from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from blueprints.horoscope.routes import horoscope_bp
from blueprints.city.routes import cities_bp

app = Flask(__name__)
load_dotenv()
CORS(app) 
app.config['MONGODB_SETTINGS'] = {
    'db': 'horoscope_service',
    'host': 'mongodb+srv://nobel10122025:OLd7VRfphDVH7G7R@cluster0.xbfffcm.mongodb.net/horoscope_service?retryWrites=true&w=majority&ssl=true',
    'tls': True,
    'tlsInsecure': True
}
db = MongoEngine(app)

# Registering blueprints
app.register_blueprint(horoscope_bp)
app.register_blueprint(cities_bp)

if __name__ == '__main__':
    app.run(debug=True)
