from model.base import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Unicode(255))
    password = db.Column(db.Unicode(255))
    super = db.Column(db.Integer, default=0)
