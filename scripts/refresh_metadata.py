import json
import os
from datetime import datetime

ENV = os.getenv("APP_ENV", "staging")
if ENV == "staging":
    METADATA_FILE = "data/metadata_staging.json"
else:
    METADATA_FILE = "data/metadata.json"
IMAGES_DIR = "data/images"
#METADATA_FILE = "data/metadata.json"
ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")


def refresh_metadata():
    if not os.path.exists(IMAGES_DIR):
        raise FileNotFoundError(f"{IMAGES_DIR} does not exist")

    images = []

    for filename in sorted(os.listdir(IMAGES_DIR)):       
        
        if not filename.lower().endswith(ALLOWED_EXTENSIONS):
            continue

        filepath = os.path.join(IMAGES_DIR, filename)

        try:
            size = os.path.getsize(filepath)

            images.append({
                "name": filename,
                "path": f"/images/{filename}",
                "size": size
            })

        except Exception as e:
            print(f"Skipping {filename}: {e}")

    metadata = {
        "last_updated": datetime.utcnow().isoformat(),
        "image_count": len(images),
        "images": images
    }

    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"Metadata refreshed: {len(images)} images")


if __name__ == "__main__":
    refresh_metadata()