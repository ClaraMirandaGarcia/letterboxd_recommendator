# utils/storage.py

from backend.scraper.scraper import get_all_watchlist_movies
from backend.utils.storage import save_movies_to_json

if __name__ == "__main__":

    user = "mgaralc"
    movies = get_all_watchlist_movies(user)
    save_movies_to_json(movies, f"{user}_watchlist.json")
    
    for movie in movies:        
        print(movie)