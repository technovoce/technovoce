from flask import Flask, render_template, request
from os import makedirs

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "secrets.key"

    makedirs(app.instance_path, exist_ok=True)

    @app.route("/")
    def index():
        return render_template("index.html", page="index")

    @app.route("/about.html")
    def about():
        return render_template("about.html", page="about")

    @app.route("/services.html")
    def services():
        return render_template("services.html", page="services")

    @app.route("/contact.html")
    def contact():
        return render_template("contact.html", page="contact")

    return app