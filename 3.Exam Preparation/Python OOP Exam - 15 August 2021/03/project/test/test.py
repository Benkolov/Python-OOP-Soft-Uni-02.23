import unittest

from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):

    def setUp(self):
        self.shop = PetShop("Pet Haven")

    def test_init(self):
        self.assertEqual(self.shop.name, "Pet Haven")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_food_positive_quantity(self):
        result = self.shop.add_food("Dog Food", 500)
        self.assertEqual(self.shop.food["Dog Food"], 500)
        self.assertEqual(result, "Successfully added 500.00 grams of Dog Food.")

    def test_add_food_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.shop.add_food("Dog Food", -500)

    def test_add_food_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.shop.add_food("Dog Food", 0)

    def test_add_pet_unique(self):
        result = self.shop.add_pet("Buddy")
        self.assertIn("Buddy", self.shop.pets)
        self.assertEqual(result, "Successfully added Buddy.")

    def test_add_pet_duplicate(self):
        self.shop.add_pet("Buddy")
        with self.assertRaises(Exception):
            self.shop.add_pet("Buddy")

    def test_feed_pet_nonexistent_pet(self):
        with self.assertRaises(Exception):
            self.shop.feed_pet("Dog Food", "Buddy")

    def test_feed_pet_nonexistent_food(self):
        self.shop.add_pet("Buddy")
        result = self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(result, "You do not have Dog Food")

    def test_feed_pet_adding_food(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 1000)
        result = self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(result, "Buddy was successfully fed")

    def test_feed_pet_success(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 2000)
        result = self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(result, "Buddy was successfully fed")

    def test_repr(self):
        self.shop.add_pet("Buddy")
        self.shop.add_pet("Max")
        result = self.shop.__repr__()
        self.assertEqual(result, "Shop Pet Haven:\nPets: Buddy, Max")

    def test_add_food_multiple_times(self):
        self.shop.add_food("Dog Food", 200)
        self.shop.add_food("Dog Food", 300)
        self.assertEqual(self.shop.food["Dog Food"], 500)

    def test_add_multiple_pets(self):
        self.shop.add_pet("Buddy")
        self.shop.add_pet("Max")
        self.assertIn("Buddy", self.shop.pets)
        self.assertIn("Max", self.shop.pets)

    def test_feed_pet_food_quantity_decreases(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 2000)
        self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(self.shop.food["Dog Food"], 1900)

    def test_add_food_float_quantity(self):
        self.shop.add_food("Dog Food", 200.5)
        self.assertEqual(self.shop.food["Dog Food"], 200.5)

    def test_feed_pet_float_food_quantity(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 1000.5)
        self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(self.shop.food["Dog Food"], 900.5)

    def test_feed_pet_multiple_times(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 2000)
        self.shop.feed_pet("Dog Food", "Buddy")
        self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(self.shop.food["Dog Food"], 1800)

    def test_add_multiple_foods(self):
        self.shop.add_food("Dog Food", 500)
        self.shop.add_food("Cat Food", 300)
        self.assertEqual(self.shop.food["Dog Food"], 500)
        self.assertEqual(self.shop.food["Cat Food"], 300)

    def test_feed_pet_multiple_foods(self):
        self.shop.add_pet("Buddy")
        self.shop.add_pet("Whiskers")
        self.shop.add_food("Dog Food", 2000)
        self.shop.add_food("Cat Food", 1500)
        self.shop.feed_pet("Dog Food", "Buddy")
        self.shop.feed_pet("Cat Food", "Whiskers")
        self.assertEqual(self.shop.food["Dog Food"], 1900)
        self.assertEqual(self.shop.food["Cat Food"], 1400)

    def test_feed_pet_insufficient_food(self):
        self.shop.add_pet("Buddy")
        self.shop.add_food("Dog Food", 50)
        result = self.shop.feed_pet("Dog Food", "Buddy")
        self.assertEqual(result, "Adding food...")


if __name__ == '__main__':
    unittest.main()