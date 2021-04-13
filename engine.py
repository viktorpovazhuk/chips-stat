from flask import Flask
import database

app = Flask(__name__)


@app.route("/")
def home_view():
    users = database.fetch()
    return list(users)
