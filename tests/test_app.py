import app

def test_index():
    client = app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from DevSecOps Pipeline" in resp.data

def test_health():
    client = app.app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"
