from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        if not name.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.name = name
        if portion <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.portion = portion
        self.price = price
        if not brand.strip():
            raise ValueError("Brand cannot be empty string or white space!")
        self.brand = brand

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
