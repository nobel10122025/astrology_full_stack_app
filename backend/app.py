from flask import Flask
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

from blueprints.horoscope.routes import horoscope_bp
from blueprints.city.routes import cities_bp
from blueprints.auth.routes import auth_bp

app = Flask(__name__)
load_dotenv()
CORS(app) 
app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv("DB_NAME"),
    'host': os.getenv("DB_CONNECT"),
    'tls': True,
    'tlsInsecure': True
}
db = MongoEngine(app)
app.secret_key = 'dfg5dr56gft56tg'  # Replace with a strong secret key
jwt = JWTManager(app)

# Registering blueprints
app.register_blueprint(horoscope_bp)
app.register_blueprint(cities_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
