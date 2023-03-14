def start_playing(func):
    return func.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))


guitar = Guitar()
print(start_playing(guitar))

