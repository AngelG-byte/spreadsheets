from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
    spreadsheets = db.relationship("Spreadsheet", backref="user", lazy=True)

class Spreadsheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    string_value = db.Column(db.String(225), nullable=True)
    integer_value = db.Column(db.Integer, nullable=True)
    columns= db.relationship("Column", backref="spreadsheet", lazy=True)

class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(225), nullable=True)
    numbers = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)
    

