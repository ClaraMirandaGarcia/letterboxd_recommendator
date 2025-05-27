# scraper/movie.py

class Movie:
    def __init__(self, title: str, url: str, slug: str):
        self.title = title
        self.url = url
        self.slug = slug

    def __repr__(self):
        return f"<Movie title='{self.title}' slug='{self.slug}'>"

    def get_json_endpoint(self):
        return f"https://letterboxd.com/film/{self.slug}/json/"