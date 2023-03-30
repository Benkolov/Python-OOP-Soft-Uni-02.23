from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):

    def test_constructor(self):
        movie = Movie('Inception', 2010, 8.8)
        self.assertEqual(movie.name, 'Inception')
        self.assertEqual(movie.year, 2010)
        self.assertEqual(movie.rating, 8.8)

    def test_name_setter(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.name = 'Interstellar'
        self.assertEqual(movie.name, 'Interstellar')
        with self.assertRaises(ValueError):
            movie.name = ''

    def test_year_setter(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.year = 2014
        self.assertEqual(movie.year, 2014)
        with self.assertRaises(ValueError):
            movie.year = 1886

    def test_add_actor(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.add_actor('Leonardo DiCaprio')
        self.assertIn('Leonardo DiCaprio', movie.actors)
        result = movie.add_actor('Leonardo DiCaprio')
        self.assertEqual(result, 'Leonardo DiCaprio is already added in the list of actors!')

    def test_gt_comparison(self):
        movie1 = Movie('Inception', 2010, 8.8)
        movie2 = Movie('Interstellar', 2014, 8.6)
        result1 = movie1 > movie2
        self.assertEqual(result1, '"Inception" is better than "Interstellar"')
        result2 = movie2 > movie1
        self.assertEqual(result2, '"Inception" is better than "Interstellar"')

    def test_repr(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.add_actor('Leonardo DiCaprio')
        movie_repr = 'Name: Inception\nYear of Release: 2010\nRating: 8.80\nCast: Leonardo DiCaprio'
        self.assertEqual(repr(movie), movie_repr)

    def test_add_multiple_actors(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.add_actor('Leonardo DiCaprio')
        movie.add_actor('Ellen Page')
        movie.add_actor('Tom Hardy')
        self.assertIn('Leonardo DiCaprio', movie.actors)
        self.assertIn('Ellen Page', movie.actors)
        self.assertIn('Tom Hardy', movie.actors)

    def test_rating_setter(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.rating = 9.0
        self.assertEqual(movie.rating, 9.0)

    def test_empty_actor_list(self):
        movie = Movie('Inception', 2010, 8.8)
        self.assertEqual(len(movie.actors), 0)

    def test_same_rating_comparison(self):
        movie1 = Movie('Inception', 2010, 8.8)
        movie2 = Movie('Interstellar', 2014, 8.8)
        result = movie1 > movie2
        self.assertEqual(result, f'"{movie2.name}" is better than "{movie1.name}"')

    def test_actors_order(self):
        movie = Movie('Inception', 2010, 8.8)
        movie.add_actor('Leonardo DiCaprio')
        movie.add_actor('Ellen Page')
        movie.add_actor('Tom Hardy')
        self.assertEqual(movie.actors, ['Leonardo DiCaprio', 'Ellen Page', 'Tom Hardy'])


if __name__ == '__main__':
    unittest.main()
