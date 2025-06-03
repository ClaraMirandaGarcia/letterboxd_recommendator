# backend/scraper/movie.py

class Movie:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def __repr__(self):
        return f"<Movie title='{self.title}' url='{self.url}'>"

    def get_json_endpoint(self):
        return f"Movie(title={self.title!r}, url={self.url!r})"
    
    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            url=data["url"]
        )