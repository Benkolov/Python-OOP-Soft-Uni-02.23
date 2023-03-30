from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._get_user(username)
        if user:
            if movie.owner != user:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")
            if movie in self.movies_collection:
                raise Exception("Movie already added to the collection!")
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
            return f"{username} successfully added {movie.title} movie."
        else:
            raise Exception("This user does not exist!")

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self._get_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self._get_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self._get_user(username)
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self._get_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return "\n".join([movie.details() for movie in sorted_movies])

    def __str__(self):
        users_str = ", ".join(
            [user.username for user in self.users_collection]) if self.users_collection else "No users"
        movies_str = ", ".join(
            [movie.title for movie in self.movies_collection]) if self.movies_collection else "No movies"
        return f"All users: {users_str}\nAll movies: {movies_str}"

    def _get_user(self, username: str):
        for user in self.users_collection:
            if user.username == username:
                return user
        return None
