from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
