import requests
from bs4 import BeautifulSoup

BASE_URL = "https://letterboxd.com"
USER_NAME = "mgaralc"
WATCHLIST_URL = f"{BASE_URL}/{USER_NAME}/watchlist/"


def get_watchlist_movies():
    
    print(WATCHLIST_URL)
    response = requests.get(WATCHLIST_URL)
    # Having a quick check about the structure
    soup = BeautifulSoup(response.content, "html.parser")
    full_page = soup.prettify()
    # print(full_page)    

    # Lets iterate over poster-container -> blocks of the movie
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
                movies.append({
                    "title": title,
                    "endpoint": f"{BASE_URL}{endpoint}"
                })
        
    return movies

if __name__ == "__main__":
    watchlist = get_watchlist_movies()
    for movie in watchlist:
        print(movie)
