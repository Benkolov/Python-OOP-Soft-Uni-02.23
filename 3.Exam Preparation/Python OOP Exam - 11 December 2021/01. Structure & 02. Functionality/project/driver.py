from project.car.car import Car


class Driver:
    def __init__(self, name: str, car: Car = None, number_of_wins: int = 0):

        self.name = name

        self.car = car
        self.number_of_wins = number_of_wins

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def take_car(self, car: Car):
        if self.car is not None:
            raise ValueError("This driver already has a car!")
        if car.is_taken:
            raise ValueError("This car is already taken!")
        self.car = car
        car.take()

    def release_car(self):
        if self.car is None:
            raise ValueError("This driver has no car to release!")
        self.car.release()
        self.car = None

    def win_race(self):
        self.number_of_wins += 1
