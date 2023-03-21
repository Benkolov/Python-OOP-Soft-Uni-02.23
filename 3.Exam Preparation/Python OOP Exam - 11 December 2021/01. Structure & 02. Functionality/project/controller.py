from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:
        if any(car.model == model for car in self.cars):
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
            self.cars.append(car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        if any(driver.name == driver_name for driver in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        if any(race.name == race_name for race in self.races):
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        driver = next((driver for driver in self.drivers if driver.name == driver_name), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_cars = [car for car in self.cars if isinstance(car, eval(car_type)) and not car.is_taken]
        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")

        new_car = available_cars[-1]
        if driver.car:
            old_model = driver.car.model
            driver.release_car()
            driver.take_car(new_car)
            return f"Driver {driver_name} changed his car from {old_model} to {new_car.model}."
        else:
            driver.take_car(new_car)
            return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        race = next((race for race in self.races if race.name == race_name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = next((driver for driver in self.drivers if driver.name == driver_name), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race.add_driver(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str) -> str:
        race = next((race for race in self.races if race.name == race_name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda driver: driver.car.speed_limit, reverse=True)[:3]

        results = []
        for driver in sorted_drivers:
            driver.win_race()
            results.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(results)

