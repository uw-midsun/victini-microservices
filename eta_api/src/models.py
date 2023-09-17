from . import db

class ETA(db.Model):
    __tablename__ = "eta"

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    eta = db.Column(db.Integer, nullable=False)
