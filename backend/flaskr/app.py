from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
login_manager = LoginManager()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/members")
def members():
    return {"members": ["member 1","member 2", "member 3"]}

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == "__main__":
    app.run(port=5555, debug=True)






