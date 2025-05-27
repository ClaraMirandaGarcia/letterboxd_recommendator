# scraper/parser.py

from scraper.movie import Movie

def parse_watchlist(soup) -> list[Movie]:
    movies_block = soup.find_all("li", class_="poster-container")
    movies = []

    for movie in movies_block:
        div = movie.find("div", class_="film-poster")
        if div:
            #alt of img contains the movie title seen as User
            title = div.find("img")["alt"] if div.find("img") else None
            #data-details-endpoint contains JSON with info
            endpoint = div.get("data-details-endpoint")
            # slug
            slug = div.get("data-film-slug")
            if title and endpoint:
                movies.append(Movie(title, endpoint, slug))

    return movies
