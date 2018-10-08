from flask import Flask

from mosquitto_api.config import configer
from mosquitto_api.model import db
from mosquitto_api.route import bp


def create_app():
    app = Flask(__name__)

    configer.init_app(app)
    db.init_app(app)
    bp.init_app(app)
    return app
