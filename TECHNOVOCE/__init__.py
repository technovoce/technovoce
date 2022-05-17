from flask import Flask, render_template, request
from os import makedirs

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "secrets.key"

    makedirs(app.instance_path, exist_ok=True)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/services")
    def services():
        return render_template("services.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    return app