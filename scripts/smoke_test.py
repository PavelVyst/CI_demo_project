import requests

def test():
    r = requests.get("http://localhost:8000/health")
    assert r.status_code == 200

    r = requests.get("http://localhost:8000/items")
    assert r.status_code == 200

    print("Smoke test passed")


if __name__ == "__main__":
    test()