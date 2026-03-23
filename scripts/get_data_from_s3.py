import os
import requests

IMAGE_URLS = [
    f"https://aft-vbi-pds.s3.amazonaws.com/bin-images/0000{i}.jpg"
    for i in range(1, 10)
]

OUTPUT_DIR = "data/images"


def download_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for url in IMAGE_URLS:
        filename = url.split("/")[-1]
        path = os.path.join(OUTPUT_DIR, filename)

        print(f"Downloading {url}...")

        r = requests.get(url, timeout=15)
        r.raise_for_status()

        content_type = r.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            raise ValueError(f"URL did not return an image: {url}")

        with open(path, "wb") as f:
            f.write(r.content)

        print(f"Saved to {path}")


if __name__ == "__main__":
    download_images()