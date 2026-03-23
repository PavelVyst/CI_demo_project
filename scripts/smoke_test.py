import requests

def test():
    r = requests.get("http://localhost:8000/health", timeout=10)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

    r = requests.get("http://localhost:8000/images", timeout=10)
    assert r.status_code == 200

    payload = r.json()
    assert "images" in payload
    assert "image_count" in payload

    print("Smoke test passed")


if __name__ == "__main__":
    test()