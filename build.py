from flask_frozen import Freezer
from TECHNOVOCE import create_app

if __name__ == "__main__":
    app = create_app()
    app.config['FREEZER_DESTINATION'] = "../build/"

    freezer = Freezer(app)

    freezer.freeze()
