import json
import os

FILE = "posted.json"

def load():
    if not os.path.exists(FILE):
        return set()
    return set(json.load(open(FILE)))

def save(data):
    json.dump(list(data), open(FILE, "w"))

posted = load()

def exists(h):
    return h in posted

def add(h):
    posted.add(h)
    save(posted)