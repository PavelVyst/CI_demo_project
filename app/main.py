from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/images")
def get_images():
    with open("data/metadata.json") as f:
        return json.load(f)