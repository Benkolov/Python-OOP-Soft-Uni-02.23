class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def test_cat_size_increase(self):
        cat = Cat("Whiskers")
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_cat_fed_after_eating(self):
        cat = Cat("Whiskers")
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_if_fed(self):
        cat = Cat("Whiskers")
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertEqual(str(context.exception), "Already fed.")

    def test_cat_cannot_sleep_if_not_fed(self):
        cat = Cat("Whiskers")
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual(str(context.exception), "Cannot sleep while hungry")

    def test_cat_not_sleepy_after_sleeping(self):
        cat = Cat("Whiskers")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
