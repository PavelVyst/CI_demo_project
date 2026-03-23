import json
from datetime import datetime

def generate_release():
    data = {
        "version": datetime.utcnow().isoformat(),
        "status": "release_candidate"
    }

    with open("data/release.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Release metadata created")


if __name__ == "__main__":
    generate_release()