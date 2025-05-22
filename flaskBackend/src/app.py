from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db

# breakpoint()

import os

from controllers.example_controller import example_bp

# app = Flask(__name__)


from flask import Flask


# app/__init__.py
# from flask import Flask

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")  # or however you load config

    print("initializing app !!!!\n!!!!!\n!!!!")
    db.init_app(app)

    with app.app_context():
        # Import models so they get registered properly
        import models

        db.create_all()

    return app


app = create_app()


app.register_blueprint(example_bp)


@app.route("/api/hello-world")
def hello_world():
    return jsonify("Hello, World!")


# def register_routes():
#     print("example_bp", example_bp)
#     app.register_blueprint(example_bp, url_prefix="/api")
#     return app


if __name__ == "__main__":
    print(os.environ)
    port = os.environ.get("API_PORT")
    if not port:
        port = 8080
        # app = register_routes()

    app.run(host="0.0.0.0", port=port, debug=True)
