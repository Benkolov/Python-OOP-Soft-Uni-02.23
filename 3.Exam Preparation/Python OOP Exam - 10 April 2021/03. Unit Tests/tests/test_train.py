import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):

    def test_init(self):
        train = Train("TestTrain", 5)
        self.assertEqual(train.name, "TestTrain")
        self.assertEqual(train.capacity, 5)
        self.assertEqual(train.passengers, [])

    def test_add_passenger(self):
        train = Train("TestTrain", 2)
        response = train.add("Alice")
        self.assertEqual(response, "Added passenger Alice")
        self.assertEqual(train.passengers, ["Alice"])

        response = train.add("Bob")
        self.assertEqual(response, "Added passenger Bob")
        self.assertEqual(train.passengers, ["Alice", "Bob"])

    def test_add_passenger_full_train(self):
        train = Train("TestTrain", 1)
        train.add("Alice")

        with self.assertRaises(ValueError) as context:
            train.add("Bob")
        self.assertEqual(str(context.exception), "Train is full")

    def test_add_passenger_exists(self):
        train = Train("TestTrain", 2)
        train.add("Alice")

        with self.assertRaises(ValueError) as context:
            train.add("Alice")
        self.assertEqual(str(context.exception), "Passenger Alice Exists")

    def test_remove_passenger(self):
        train = Train("TestTrain", 2)
        train.add("Alice")
        train.add("Bob")

        response = train.remove("Alice")
        self.assertEqual(response, "Removed Alice")
        self.assertEqual(train.passengers, ["Bob"])

    def test_remove_passenger_not_found(self):
        train = Train("TestTrain", 2)
        train.add("Alice")

        with self.assertRaises(ValueError) as context:
            train.remove("Bob")
        self.assertEqual(str(context.exception), "Passenger Not Found")


if __name__ == '__main__':
    unittest.main()
