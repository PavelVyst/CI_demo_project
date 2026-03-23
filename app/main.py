from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()


@app.get("/images")
def get_images():
    path = "data/metadata.json"

    if not os.path.exists(path):
        raise HTTPException(status_code=500, detail="metadata.json not found")

    with open(path) as f:
        return json.load(f)

@app.get("/images")
def get_images():
    with open("data/metadata.json") as f:
        return json.load(f)