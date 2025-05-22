from flask import Blueprint, jsonify, request
from services.service_factory import ServiceFactory

example_bp = Blueprint("example_bp", __name__, url_prefix="/example")
example_service = ServiceFactory.get_example_service()

print("registering routes")


@example_bp.route("/", methods=["GET"])
def get_examples():
    examples = example_service.get_all_examples()
    print(examples)
    return jsonify(examples)


@example_bp.route("/", methods=["POST"])
def create_example():
    data = request.json
    example = example_service.create_example(data["name"], data["json"], data["atta"])
    return jsonify(example), 201
