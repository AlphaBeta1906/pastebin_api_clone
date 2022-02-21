import pytest
from api import run,db
from api.config import ConfigTest

app = run()
@pytest.fixture
def client():
    app.config.from_object(ConfigTest)
    
    with app.app_context():
        from api.model import Paste
        db.create_all()
        db.session.commit()
    
    return app.test_client()

def testing_route(client):
    response = client.get("api/v1/test")
    assert response.status_code == 200

def test_post(client):
    response = client.post("api/v1/paste",json= {"title": "testing", "code": "print('hello wordl')","language": "python"})
    print(response)
    assert response.status_code == 200    