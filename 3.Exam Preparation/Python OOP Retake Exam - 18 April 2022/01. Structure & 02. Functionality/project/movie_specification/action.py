from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
