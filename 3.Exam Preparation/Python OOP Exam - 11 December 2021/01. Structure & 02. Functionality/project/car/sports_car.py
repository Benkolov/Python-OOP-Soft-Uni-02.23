from project.car.car import Car


class SportsCar(Car):
    def get_min_speed_limit(self) -> int:
        return 400

    def get_max_speed_limit(self) -> int:
        return 600
