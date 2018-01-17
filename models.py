from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_phone = db.Column(db.String(100))
    formatted_phone = db.Column(db.String(20))
