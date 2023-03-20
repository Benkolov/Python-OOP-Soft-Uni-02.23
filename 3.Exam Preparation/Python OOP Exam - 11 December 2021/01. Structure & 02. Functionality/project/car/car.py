from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):

        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False



    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not (self.get_min_speed_limit() <= value <= self.get_max_speed_limit()):
            raise ValueError(f"Invalid speed limit! Must be between {self.get_min_speed_limit()} and {self.get_max_speed_limit()}!")
        self.__speed_limit = value

    @abstractmethod
    def get_min_speed_limit(self) -> int:
        pass

    @abstractmethod
    def get_max_speed_limit(self) -> int:
        pass

    def take(self):
        if self.is_taken:
            raise ValueError("This car is already taken!")
        self.is_taken = True

    def release(self):
        if not self.is_taken:
            raise ValueError("This car is not taken!")
        self.is_taken = False
