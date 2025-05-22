import pytest
import json
from app import app  # assuming app.py is inside src/
from models import db
from ..factories.example_factory import ExampleFactory

# app = create_app()


@pytest.fixture
def client():
    app.testing = True
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


@pytest.fixture
def example_record(client):
    # breakpoint()
    example_record = ExampleFactory.create_batch(2)
    # example_record = "test"
    return example_record


def test_get_example_response(client, example_record):
    # Example MagicMock usage — not needed in this case, but here for reference.
    # mock_service = MagicMock(return_value="Hello, World!")
    # You could patch an external dependency like:
    # with patch('app.greeting_service.get_message', mock_service):
    response = client.get("/example/")
    example_record_response = json.loads(response.data.decode())[0]
    print(
        "\n response: ",
        example_record_response,
        # .array_example,
        # " \n exampleRecord: ",
        # example_record.array_example,
    )
    assert response.status_code == 200
    assert example_record_response["array_example"] == example_record[0].array_example
    assert example_record_response["name"] == example_record[0].name
