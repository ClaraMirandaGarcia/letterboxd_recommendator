# scraper/fetcher.py

import requests
from bs4 import BeautifulSoup
import os
import hashlib

CACHE_DIR = "cache"

def _make_cache_filename(username: str, page: int) -> str:
    '''
    Generates a cache filename based on the username and page number.

    Args:
        username (str): Letterboxd username.
        page (int): Page number.

    Returns:
        str: Path to the corresponding cache file.
    '''
    os.makedirs(CACHE_DIR, exist_ok=True)
    key = f"{username}_page_{page}"
    return os.path.join(CACHE_DIR, hashlib.md5(key.encode()).hexdigest() + ".html")

def fetch_watchlist_page(username: str, page=1, use_cache=True) -> BeautifulSoup:
    '''
    Download or retrieve from cache a page from the watchlist of a Letterboxd user.

    Args:
        username (str): Letterboxd username.
        page (int, optional): Page number to retrieve. Default 1.
        use_cache (bool, optional): Whether to use local cache. Default True.

    Returns:
        BeautifulSoup: HTML content of the page as BeautifulSoup object
    '''


    url = f"https://letterboxd.com/{username}/watchlist/page/{page}/"
    print(f"Fetching {url} (page {page})")

    cache_path = _make_cache_filename(username, page)
    if use_cache and os.path.exists(cache_path):
        
        print(f"→ Using cached page {page}")
        with open(cache_path, "r", encoding="utf-8") as f:
            html = f.read()


    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch watchlist page {page} for user {username}")

        html = response.text
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(html)

    return BeautifulSoup(html, "html.parser")
