# from flask import Flask, jsonify

# # breakpoint()

# import os

from controllers.example_controller import example_bp

# app = Flask(__name__)


# from flask import Flask


# @app.route("/api/hello-world")
# def hello_world():
#     return jsonify("Hello, World!")


# def register_routes():
#     # app.register_blueprint(example_bp, url_prefix="/weapons")
#     return app


if __name__ == "__main__":
    print(example_bp)
    # port = os.environ["API_PORT"]
    # app = register_routes()
    # app.run(host="0.0.0.0", port=port, debug=True)
