# main.py

from scraper.fetcher import fetch_watchlist_html
from scraper.parser import parse_watchlist

if __name__ == "__main__":
    username = "mgaralc"
    soup = fetch_watchlist_html(username)
    movies = parse_watchlist(soup)

    for movie in movies:
        print(movie)
        print("  JSON:", movie.get_json_endpoint())
