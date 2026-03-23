from fastapi import FastAPI,HTTPException
import os
import json

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/images")
def get_images():
    path = "data/metadata.json"

    if not os.path.exists(path):
        raise HTTPException(status_code=500, detail="metadata.json not found")

    with open(path, encoding="utf-8") as f:
        return json.load(f)