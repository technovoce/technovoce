from flask import Flask, render_template, request
from os import makedirs

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "secrets.key"

    makedirs(app.instance_path, exist_ok=True)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app