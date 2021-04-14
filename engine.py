from flask import Flask
import database

app = Flask(__name__)


@app.route("/")
def home_view():
    database.worker.open_connection()
    users = database.worker.get_users()
    database.worker.delete_user(users[1][0])
    database.worker.update_user(users[2][0], "sanya")
    database.worker.add_user()
    database.worker.close_connection()
    return str(users)
