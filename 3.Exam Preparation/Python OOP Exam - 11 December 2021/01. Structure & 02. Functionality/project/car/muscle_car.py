from project.car.car import Car


class MuscleCar(Car):
    def get_min_speed_limit(self) -> int:
        return 250

    def get_max_speed_limit(self) -> int:
        return 450
