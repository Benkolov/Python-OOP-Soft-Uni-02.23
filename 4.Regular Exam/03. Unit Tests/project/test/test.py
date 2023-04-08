from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("John Smith", 25, 1200.0)

    def test_init(self):
        self.assertEqual(self.player.name, "John Smith")
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.points, 1200.0)
        self.assertEqual(self.player.wins, [])

    def test_name_validation(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("JS", 25, 1200.0)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_validation(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("John Smith", 17, 1200.0)
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win(self):
        self.player.add_new_win("Australian Open")
        self.assertEqual(self.player.wins, ["Australian Open"])
        self.player.add_new_win("Wimbledon")
        self.assertEqual(self.player.wins, ["Australian Open", "Wimbledon"])

    def test_add_existing_win(self):
        player = TennisPlayer("John Smith", 25, 1200.0)
        player.add_new_win("Australian Open")
        result = player.add_new_win("Australian Open")
        self.assertEqual(result, "Australian Open has been already added to the list of wins!")

    def test_comparison(self):
        player1 = TennisPlayer("John Smith", 25, 1200.0)
        player2 = TennisPlayer("Jane Doe", 28, 1500.0)
        result = player1 < player2
        self.assertEqual(result, 'Jane Doe is a top seeded player and he/she is better than John Smith')

    def test_comparison_other_not_big(self):
        player1 = TennisPlayer("John Smith", 25, 1800.0)
        player2 = TennisPlayer("Jane Doe", 28, 1500.0)
        result = player1 < player2
        self.assertEqual(result, 'John Smith is a better player than Jane Doe')

    def test_str_representation(self):
        player = TennisPlayer("John Smith", 25, 1200.0)
        player.add_new_win("Australian Open")
        player.add_new_win("Wimbledon")
        expected_str = "Tennis Player: John Smith\n" \
                       "Age: 25\n" \
                       "Points: 1200.0\n" \
                       "Tournaments won: Australian Open, Wimbledon"
        self.assertEqual(str(player), expected_str)


if __name__ == "__main__":
    main()
