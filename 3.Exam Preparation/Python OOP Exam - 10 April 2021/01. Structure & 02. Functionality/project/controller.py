from project.core.decoration_factory import DecorationFactory
from project.decoration.decoration_repository import DecorationRepository
from project.core.aquarium_factory import AquariumFactory


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
            self.aquariums.append(aquarium)
            return f'Successfully added {aquarium_type}.'
        except ValueError as error:
            return str(error)

    def add_decoration(self, decoration_type: str):
        try:
            decoration = self.decoration_factory.create_decoration(decoration_type)
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        except ValueError as error:
            return str(error)

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        self.decorations_repository.remove(decoration)
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
            return None

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass
