from flask import Flask
from app.config import Config
from app.routes import ALL_BLUEPRINTS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY
    for bp in ALL_BLUEPRINTS:
        app.register_blueprint(bp)
    return app
