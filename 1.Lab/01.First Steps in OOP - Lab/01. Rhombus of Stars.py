class Rhombus:
    def __init__(self, size):
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1):
            print(" " * (self.size - i) + "* " * i)

        for i in range(self.size - 1, 0, -1):
            print(" " * (self.size - i) + "* " * i)


if __name__ == "__main__":
    n = int(input())
    rhombus = Rhombus(n)
    rhombus.draw()
