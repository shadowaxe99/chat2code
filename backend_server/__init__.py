from flask import Flask
from .config import Config
from .database import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from .routes import api_bp
app.register_blueprint(api_bp)
