from project.driver import Driver


class Race:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Name cannot be an empty string!")
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    def remove_driver(self, driver: Driver):
        if driver not in self.drivers:
            raise ValueError("Driver not found in the race!")
        self.drivers.remove(driver)
