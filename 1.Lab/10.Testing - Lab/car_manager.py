class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

import unittest

class TestCar(unittest.TestCase):

    def test_constructor(self):
        car = Car("Make", "Model", 10, 50)
        self.assertEqual(car.make, "Make")
        self.assertEqual(car.model, "Model")
        self.assertEqual(car.fuel_consumption, 10)
        self.assertEqual(car.fuel_capacity, 50)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_setter(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_setter(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_setter(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.fuel_consumption = -5
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_setter(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.fuel_capacity = -5
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_setter(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -5
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        car = Car("Make", "Model", 10, 50)
        car.refuel(20)
        self.assertEqual(car.fuel_amount, 20)

    def test_refuel_negative_amount(self):
        car = Car("Make", "Model", 10, 50)
        with self.assertRaises(Exception) as context:
            car.refuel(-5)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_over_capacity(self):
        car = Car("Make", "Model", 10, 50)
        car.refuel(60)
        self.assertEqual(car.fuel_amount, 50)

    def test_drive(self):
        car = Car("Make", "Model", 10, 50)
        car.refuel(50)
        car.drive(100)
        self.assertEqual(car.fuel_amount, 40)

    def test_drive_not_enough_fuel(self):
        car = Car("Make", "Model", 10, 50)
        car.refuel(10)
        with self.assertRaises(Exception) as context:
            car.drive(200)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
