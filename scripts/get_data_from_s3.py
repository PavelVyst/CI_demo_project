import os
import requests

IMAGE_URLS = []

for index_images in range(1,10):

    IMAGE_URLS.append(f"https://aft-vbi-pds.s3.amazonaws.com/bin-images/0000{index_images}.jpg")

OUTPUT_DIR = "data/images"


def download_images():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for url in IMAGE_URLS:
        filename = url.split("/")[-1]
        path = os.path.join(OUTPUT_DIR, filename)

        print(f"Downloading {url}...")

        r = requests.get(url)
        r.raise_for_status()

        with open(path, "wb") as f:
            f.write(r.content)

        print(f"Saved to {path}")


if __name__ == "__main__":
    download_images()