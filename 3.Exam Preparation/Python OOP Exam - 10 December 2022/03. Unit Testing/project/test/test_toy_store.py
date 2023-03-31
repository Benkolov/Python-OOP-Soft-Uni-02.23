from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct__init(self):
        for key in range(ord("A"), ord("G") + 1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

        self.assertEqual(7, len(self.store.toy_shelf))

    def test_add_toy_on_non_existing_shelf_raises_exception(self):
        pass

    def test_add_toy_that_is_already_on_shelf_raises_exception(self):
        pass

    def test_add_toy_to_a_full_shelf_raises_exception(self):
        pass

    def test_add_toy_successfully_returns_string(self):
        pass


if __name__ == "__main__":
    main()

