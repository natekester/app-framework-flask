import pytest

from app import app  # assuming app.py is inside src/


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_hello_world_response(client):
    # Example MagicMock usage — not needed in this case, but here for reference.
    # mock_service = MagicMock(return_value="Hello, World!")
    # You could patch an external dependency like:
    # with patch('app.greeting_service.get_message', mock_service):
    response = client.get("/api/hello-world")
    hello: str = response.data.decode()
    print("hello:", hello)
    assert response.status_code == 200
    assert response.data.decode() == '"Hello, World!"\n'
