import requests


def test_post_route():
    code_title = "test"
    code = """
    class Codes(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        unique_id = db.Column(db.String(1000), nullable=False)
        code_title = db.Column(db.String(1000), nullable=False)
        code = db.Column(db.String(10000), nullable=False)
        languange = db.Column(db.String(1000), nullable=False)
        date_added = db.Column(db.DateTime(), default=datetime.today(), nullable=False)
    """
    languange = "python"
    req = requests.post(
        f"http://127.0.0.1:5000/add_code?code_title={code_title}&code={code}&languange={languange}"
    )

    print(req.status_code)
    print(req.json())
    print(req.url)
    assert req.status_code == 200
    assert req.json()["message"] != "error"


def test_get_route():
    import json

    req = requests.get("http://127.0.0.1:5000/get_code/fr5m")
    print(json.dumps(req.json(), indent=4))
    assert req.status_code == 200


test_get_route()
