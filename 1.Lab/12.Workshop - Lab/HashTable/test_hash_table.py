from unittest import TestCase, main
from hash_table import HashTable


class TestCustomHashTable(TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_correct_initializing(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None] * 4, self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)

    def test__getitem__correct(self):
        self.table["name"] = "Peter"

        self.assertEqual("Peter", self.table["name"])

    def test__getitem_invalid_key_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table["b"]

        self.assertEqual("'b is not a valid key!'", str(ke.exception))

    def test_correct_overwrite_on_key(self):
        self.table["name"] = "Peter"
        self.table["name"] = "Diyan"

        self.assertEqual(self.table["name"], "Diyan")

    def test_resizing_table_when_full(self):
        self.table["1"] = "1"
        self.table["2"] = "2"
        self.table["3"] = "3"
        self.table["4"] = "4"
        self.table["5"] = "5"

        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_index_generate_correct(self):
        result = self.table._HashTable__calc_index("name")
        self.assertEqual(1, result)

    def test_collision_and_no_free_space_to_the_end_of_the_array_starts_from_the_beginning(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        self.table["is_pet_owner"] = True
        self.table["is_driver"] = False

        key_index = self.table._HashTable__keys.index("is_driver")

        self.assertEqual(0, key_index)

    def test_get_on_non_existing_key_without_default_value_returns_none(self):
        self.assertIsNone(self.table.get("b"))

    def test_get_on_non_existing_key_with_default_value_returns_default_value(self):
        self.assertEqual("not valid", self.table.get("b", "not valid"))


if __name__ == "__main__":
    main()
