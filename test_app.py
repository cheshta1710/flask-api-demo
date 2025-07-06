import requests

def test_ping():
    res = requests.get("http://localhost:5000/ping")
    assert res.status_code == 200
    assert res.json() == {"message": "Pong!"}
