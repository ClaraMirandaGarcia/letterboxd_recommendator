# utils/storage.py

import json
from scraper.movie import Movie

def save_movies_to_json(movies: list[Movie], filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([m.to_dict() for m in movies], f, ensure_ascii=False, indent=2)

def load_movies_from_json(filename: str) -> list[Movie]:
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Movie.from_dict(d) for d in data]
