import unittest

from project.plantation import Plantation


class TestPlantation(unittest.TestCase):

    def test_initialization(self):
        plantation = Plantation(5)
        self.assertEqual(plantation.size, 5)
        self.assertEqual(plantation.plants, {})
        self.assertEqual(plantation.workers, [])

    def test_size_setter(self):
        plantation = Plantation(5)
        with self.assertRaises(ValueError):
            plantation.size = -1
        plantation.size = 10
        self.assertEqual(plantation.size, 10)

    def test_hire_worker(self):
        plantation = Plantation(5)
        result = plantation.hire_worker("John")
        self.assertEqual(result, "John successfully hired.")
        self.assertEqual(plantation.workers, ["John"])

        with self.assertRaises(ValueError):
            plantation.hire_worker("John")

    def test_len(self):
        plantation = Plantation(5)
        self.assertEqual(len(plantation), 0)

        plantation.planting("John", "apple")
        self.assertEqual(len(plantation), 1)

    def test_planting(self):
        plantation = Plantation(2)
        with self.assertRaises(ValueError):
            plantation.planting("John", "apple")

        plantation.hire_worker("John")
        result = plantation.planting("John", "apple")
        self.assertEqual(result, "John planted it's first apple.")
        self.assertEqual(plantation.plants, {"John": ["apple"]})

        result = plantation.planting("John", "banana")
        self.assertEqual(result, "John planted banana.")
        self.assertEqual(plantation.plants, {"John": ["apple", "banana"]})

        plantation.hire_worker("Mike")
        with self.assertRaises(ValueError):
            plantation.planting("Bob", "cherry")

        with self.assertRaises(ValueError):
            plantation.planting("Mike", "orange")

    def test_str(self):
        plantation = Plantation(2)
        plantation.hire_worker("John")
        plantation.planting("John", "apple")
        plantation.hire_worker("Mike")
        plantation.planting("Mike", "banana")

        expected_output = "Plantation size: 2\nJohn, Mike\nJohn planted: apple\nMike planted: banana"
        self.assertEqual(str(plantation), expected_output)

    def test_repr(self):
        plantation = Plantation(2)
        plantation.hire_worker("John")
        plantation.hire_worker("Mike")

        expected_output = "Size: 2\nWorkers: John, Mike"
        self.assertEqual(repr(plantation), expected_output)

