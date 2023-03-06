from . import db

# user model
class Users():
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
