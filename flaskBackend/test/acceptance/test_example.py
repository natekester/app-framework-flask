import pytest
import json
from app import app  # assuming app.py is inside src/
from models import db
from ..factories.example_factory import ExampleFactory
from ..factories.sub_example_factory import SubExampleFactory


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
    example_record = ExampleFactory.create_batch(2)
    return example_record


@pytest.fixture
def sub_example_record(example_record):
    sub_example_record = SubExampleFactory(example=example_record[0])
    return sub_example_record


def test_get_example_response(client, example_record, sub_example_record):

    response = client.get("/example/")
    example_record_response = json.loads(response.data.decode())[0]

    assert response.status_code == 200
    assert example_record_response["array_example"] == example_record[0].array_example
    assert example_record_response["name"] == example_record[0].name
