# backend/scraper/parser.py

from backend.scraper.movie import Movie

def parse_watchlist_page(soup) -> list[Movie]:
    '''
    Parse a watchlist page to extract Movie objects.

    Args:
        soup (BeautifulSoup): HTML of the watchlist page as a BeautifulSoup object.

    Returns:
        list[Movie]: List of movies represented as Movie objects.
    '''
    movies_block = soup.find_all("li", class_="poster-container")
    movies = []

    for movie in movies_block:
        div = movie.find("div", class_="film-poster")
        if div:
            #alt of img contains the movie title seen as User
            title = div.find("img")["alt"] if div.find("img") else None
            #data-details-endpoint contains JSON with info
            endpoint = div.get("data-details-endpoint")
            if title and endpoint:
                movies.append(Movie(title, endpoint))

    return movies
