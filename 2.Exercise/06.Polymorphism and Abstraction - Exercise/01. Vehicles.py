from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner_consumption = 0.9

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f"The car drove {distance} km.")
        else:
            print("The car does not have enough fuel to drive that distance.")

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        print(f"The car was refueled with {fuel} liters of fuel.")


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.air_conditioner_consumption = 1.6
        self.hole_percentage = 0.05

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f"The truck drove {distance} km.")
        else:
            print("The truck does not have enough fuel to drive that distance.")

    def refuel(self, fuel):
        fuel_to_add = fuel * (1 - self.hole_percentage)
        self.fuel_quantity += fuel_to_add
        print(f"The truck was refueled with {fuel} liters of fuel. {fuel * self.hole_percentage:.2f} liters leaked from the hole.")
