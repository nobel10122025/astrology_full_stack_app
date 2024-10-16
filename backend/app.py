from flask import Flask
from blueprints.horoscope import routes
from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Registering blueprints
app.register_blueprint(routes.horoscope_bp)
load_dotenv()

if __name__ == '__main__':
    app.run(debug=True)
