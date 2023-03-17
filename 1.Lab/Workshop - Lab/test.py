from custom_list import CustomList
import unittest

# class TestCustomList(unittest.TestCase):
#     def test_append(self):
#         lst = CustomList()
#         self.assertEqual(lst.append(5), [5])
#         self.assertEqual(lst.append(7), [5, 7])
#
#     def test_remove(self):
#         lst = CustomList()
#         lst.extend([1, 2, 3])
#         self.assertEqual(lst.remove(1), 2)
#         self.assertEqual(lst.data, [1, 3])
#
#     def test_get(self):
#         lst = CustomList()
#         lst.extend([1, 2, 3])
#         self.assertEqual(lst.get(0), 1)
#         self.assertEqual(lst.get(2), 3)
#
#     # Add more tests for the other functionalities...
#
# if __name__ == "__main__":
#     unittest.main()


# Create a CustomList instance and add some values
lst = CustomList()
lst.append(1)
lst.append(2)
lst.append(3)
print(lst.data)  # Output: [1, 2, 3]

# Check if the list is empty
print(lst.is_empty())  # Output: False

# Remove a value from the list
lst.remove_value(2)
print(lst.data)  # Output: [1, 3]

# Replace a value at a specific index
lst.replace(1, 4)
print(lst.data)  # Output: [1, 4]

# Concatenate the list with another iterable
result = lst.concat([5, 6, 7])
print(result)  # Output: [1, 4, 5, 6, 7]

# Slice the list
result = lst.slice(1, 3)
print(result)  # Output: [4]

# Filter the list based on a condition
even_values = lst.filter(lambda x: x % 2 == 0)
print(even_values)  # Output: [4]

# Map a function to the list elements
squares = lst.map(lambda x: x ** 2)
print(squares)  # Output: [1, 16]

# Reduce the list using a function
total = lst.reduce(lambda x, y: x + y)
print(total)  # Output: 5

# Find the index of the first element that satisfies a condition
index = lst.find(lambda x: x > 2)
print(index)  # Output: 1

# Sort the list in ascending order
lst.append(2)
sorted_lst = lst.sort()
print(sorted_lst)  # Output: [1, 2, 4]
