# scraper/scraper.py

from scraper.fetcher import fetch_watchlist_page
from scraper.parser import parse_watchlist_page
from bs4 import BeautifulSoup
import time
import random


def get_total_pages(soup):
    '''
    Extracts the total number of watchlist pages from the BeautifulSoup HTML.

    Args:
        soup (BeautifulSoup): BeautifulSoup object of a watchlist page.

    Returns:
        int: Total number of pages in the watchlist.
    '''

    pagination = soup.find("div", class_="paginate-pages")
    if not pagination:
        return 1
    page_links = pagination.find_all("a")
    page_numbers = []
    for link in page_links:
        try:
            page_numbers.append(int(link.text.strip()))
        except ValueError:
            continue
    if page_numbers:
        return max(page_numbers)
    return 1

def get_all_watchlist_movies(username):
    '''
    Gets all the movies in the watchlist of a Letterboxd user.

    Args:
        username (str): Letterboxd username.

    Returns:
        list[Movie]: List of Movie objects extracted from the whole watchlist.
    '''
    first_page_soup = fetch_watchlist_page(username, 1)
    total_pages = get_total_pages(first_page_soup)

    all_movies = []
    # Parse the first page
    all_movies.extend(parse_watchlist_page(first_page_soup))

    # Iterating from 2nd to last page
    for page in range(2, total_pages + 1):
        time.sleep(random.uniform(1.5, 3.0))
        html = fetch_watchlist_page(username, page)
        all_movies.extend(parse_watchlist_page(html))

    return all_movies
