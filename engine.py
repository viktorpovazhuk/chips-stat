from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def read_root():
    """
    Return content of root html file
    """
    if request.method == "GET":
        return render_template("index.html")