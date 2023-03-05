from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
login_manager = LoginManager()

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/members")
def members():
    return {"members": ["member 1","member 2", "member 3"]}

if __name__ == "__main__":
    app.run(debug=True)




