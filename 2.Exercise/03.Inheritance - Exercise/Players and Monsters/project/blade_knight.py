from project.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)
        self.username = username
        self.level = level

    def __str__(self):

        return f"{self.username} of type {BladeKnight.__name__} has level {self.level}"


