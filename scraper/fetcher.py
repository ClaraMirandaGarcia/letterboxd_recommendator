# scraper/fetcher.py

import requests
from bs4 import BeautifulSoup

def fetch_watchlist_html(username: str) -> BeautifulSoup:
    url = f"https://letterboxd.com/{username}/watchlist/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch watchlist page: {url}")
    return BeautifulSoup(response.text, "html.parser")
