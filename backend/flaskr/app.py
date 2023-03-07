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


# typical create request

# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#         pages_num = int(request.form['pages_num'])
#         review = request.form['review']

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute('INSERT INTO books (title, author, pages_num, review)'
#                     'VALUES (%s, %s, %s, %s)',
#                     (title, author, pages_num, review))
#         conn.commit()
#         cur.close()
#         conn.close()
#         return redirect(url_for('index'))



