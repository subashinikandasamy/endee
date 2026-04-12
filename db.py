# db.py

import json
import os

DB_FILE = "data.json"


# Ensure file exists
def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)


# Insert data
def insert(data):
    init_db()
    with open(DB_FILE, "r") as f:
        records = json.load(f)

    records.append(data)

    with open(DB_FILE, "w") as f:
        json.dump(records, f, indent=4)


# Search data
def search(query):
    init_db()
    with open(DB_FILE, "r") as f:
        records = json.load(f)

    results = []
    for item in records:
        if query.lower() in str(item).lower():
            results.append(item)

    return results