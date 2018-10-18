from flask import Flask

from config import configer
from model import db
from route import bp
from handle import intercept


def create_app():
    app = Flask(__name__)

    configer.init_app(app)
    intercept.init_app(app)
    db.init_app(app)
    bp.init_app(app)
    return app
