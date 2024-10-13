from flask import Flask
from blueprints.horoscope import routes
from dotenv import load_dotenv

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(routes.horoscope_bp)
load_dotenv()

if __name__ == '__main__':
    app.run(debug=True)
