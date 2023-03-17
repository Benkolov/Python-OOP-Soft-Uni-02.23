class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

    import unittest

    class TestIntegerList(unittest.TestCase):

        def test_constructor(self):
            int_list = IntegerList(1, 2, 3)
            self.assertEqual(int_list.get_data(), [1, 2, 3])

        def test_add_element(self):
            int_list = IntegerList(1, 2, 3)
            int_list.add(4)
            self.assertEqual(int_list.get_data(), [1, 2, 3, 4])

        def test_add_non_integer(self):
            int_list = IntegerList(1, 2, 3)
            with self.assertRaises(ValueError) as context:
                int_list.add("test")
            self.assertEqual(str(context.exception), "Element is not Integer")

        def test_remove_index(self):
            int_list = IntegerList(1, 2, 3)
            removed_element = int_list.remove_index(1)
            self.assertEqual(removed_element, 2)
            self.assertEqual(int_list.get_data(), [1, 3])

        def test_remove_index_out_of_range(self):
            int_list = IntegerList(1, 2, 3)
            with self.assertRaises(IndexError) as context:
                int_list.remove_index(3)
            self.assertEqual(str(context.exception), "Index is out of range")

        def test_get(self):
            int_list = IntegerList(1, 2, 3)
            self.assertEqual(int_list.get(1), 2)

        def test_get_out_of_range(self):
            int_list = IntegerList(1, 2, 3)
            with self.assertRaises(IndexError) as context:
                int_list.get(3)
            self.assertEqual(str(context.exception), "Index is out of range")

        def test_insert(self):
            int_list = IntegerList(1, 2, 3)
            int_list.insert(1, 4)
            self.assertEqual(int_list.get_data(), [1, 4, 2, 3])

        def test_insert_out_of_range(self):
            int_list = IntegerList(1, 2, 3)
            with self.assertRaises(IndexError) as context:
                int_list.insert(3, 4)
            self.assertEqual(str(context.exception), "Index is out of range")

        def test_insert_non_integer(self):
            int_list = IntegerList(1, 2, 3)
            with self.assertRaises(ValueError) as context:
                int_list.insert(1, "test")
            self.assertEqual(str(context.exception), "Element is not Integer")

        def test_get_biggest(self):
            int_list = IntegerList(1, 2, 3)
            self.assertEqual(int_list.get_biggest(), 3)

        def test_get_index(self):
            int_list = IntegerList(1, 2, 3)
            self.assertEqual(int_list.get_index(2), 1)

    if __name__ == '__main__':
        unittest.main()
