class Book:
    def __init__(self, formatter: 'IFormatter', content: str):
        self.formatter = formatter
        self.content = content

    @property
    def content(self) -> str:
        return self.formatter.format(self)

    @content.setter
    def content(self, value: str):
        self._content = value


class IFormatter:
    def format(self, book: Book) -> str:
        pass


class Formatter(IFormatter):
    def format(self, book: Book) -> str:
        return book._content


class Printer:
    def __init__(self, formatter: 'IFormatter'):
        self.formatter = formatter

    def get_book(self, book: Book) -> str:
        formatted_book = self.formatter.format(book)
        return formatted_book
