import unittest

from project.bookstore import Bookstore


class TestBookstore(unittest.TestCase):

    def test_constructor(self):
        bookstore = Bookstore(10)
        self.assertEqual(bookstore.books_limit, 10)
        self.assertEqual(bookstore.total_sold_books, 0)
        self.assertEqual(len(bookstore), 0)

    def test_books_limit_setter(self):
        bookstore = Bookstore(10)
        bookstore.books_limit = 20
        self.assertEqual(bookstore.books_limit, 20)

        with self.assertRaises(ValueError):
            bookstore.books_limit = 0

        with self.assertRaises(ValueError):
            bookstore.books_limit = -5

    def test_receive_book(self):
        bookstore = Bookstore(10)
        result = bookstore.receive_book("Book A", 5)
        self.assertEqual(result, "5 copies of Book A are available in the bookstore.")
        self.assertEqual(len(bookstore), 5)

        result = bookstore.receive_book("Book B", 3)
        self.assertEqual(result, "3 copies of Book B are available in the bookstore.")
        self.assertEqual(len(bookstore), 8)

        with self.assertRaises(Exception):
            bookstore.receive_book("Book C", 3)

    def test_sell_book(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("Book A", 5)

        result = bookstore.sell_book("Book A", 2)
        self.assertEqual(result, "Sold 2 copies of Book A")
        self.assertEqual(bookstore.total_sold_books, 2)

        with self.assertRaises(Exception):
            bookstore.sell_book("Book B", 1)

        with self.assertRaises(Exception):
            bookstore.sell_book("Book A", 4)

    def test_str_representation(self):
        bookstore = Bookstore(10)
        bookstore.receive_book("Book A", 5)
        bookstore.receive_book("Book B", 3)
        bookstore.sell_book("Book A", 2)

        expected = (
            "Total sold books: 2\n"
            "Current availability: 6\n"
            " - Book A: 3 copies\n"
            " - Book B: 3 copies"
        )
        self.assertEqual(str(bookstore), expected)


if __name__ == '__main__':
    unittest.main()
