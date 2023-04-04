from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ("Guitarist", "Drummer", "Singer"):
            raise ValueError("Invalid musician type!")

        musician_name = [m.name for m in self.musicians]
        if name in musician_name:
            raise Exception(f"{name} is already a musician!")

        m = None
        if musician_type == "Guitarist":
            m = Guitarist(name, age)
        elif musician_type == "Drummer":
            m = Drummer(name, age)
        else:
            m = Singer(name, age)
        self.musicians.append(m)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        pass

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        pass

    def add_musician_to_band(self, musician_name: str, band_name: str):
        pass

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass
