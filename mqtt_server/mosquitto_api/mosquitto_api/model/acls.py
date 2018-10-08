from model.base import db


class Acls(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Unicode(255))
    topic = db.Column(db.Unicode(255))
    rw = db.Column(db.Integer, default=0)
