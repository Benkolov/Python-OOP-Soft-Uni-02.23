from project.room import Room
from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> str or None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        result = room.take_room(people)

        if result:
            return result
        self.guests += people

    def free_room(self, room_number: int) -> str or None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))
        guests = room.guests
        result = room.free_room()

        if result:
            return result

        self.guests -= guests

    def status(self):
        free_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {free_rooms}\nTaken rooms: {taken_rooms}"
