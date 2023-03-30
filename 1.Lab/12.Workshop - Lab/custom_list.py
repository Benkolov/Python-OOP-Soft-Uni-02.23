class CustomList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)
        return self.data

    def remove(self, index):
        value = self.data[index]
        del self.data[index]
        return value

    def get(self, index):
        return self.data[index]

    def extend(self, iterable):
        self.data.extend(iterable)
        return self.data

    def insert(self, index, value):
        self.data.insert(index, value)
        return self.data

    def pop(self):
        return self.data.pop()

    def clear(self):
        self.data.clear()

    def index(self, value):
        return self.data.index(value)

    def count(self, value):
        return self.data.count(value)

    def reverse(self):
        return self.data[::-1]

    def copy(self):
        return self.data.copy()

    def size(self):
        return len(self.data)

    def add_first(self, value):
        self.data.insert(0, value)

    def dictionize(self):
        result = {}
        for i in range(0, len(self.data), 2):
            key = self.data[i]
            value = self.data[i + 1] if i + 1 < len(self.data) else " "
            result[key] = value
        return result

    def move(self, amount):
        self.data = self.data[amount:] + self.data[:amount]
        return self.data

    def sum(self):
        total = 0
        for value in self.data:
            if isinstance(value, (int, float)):
                total += value
            elif isinstance(value, str):
                total += len(value)
        return total

    def overbound(self):
        return max(range(len(self.data)), key=lambda i: self.data[i] if isinstance(self.data[i], (int, float)) else len(self.data[i]))

    def underbound(self):
        return min(range(len(self.data)), key=lambda i: self.data[i] if isinstance(self.data[i], (int, float)) else len(self.data[i]))

    def is_empty(self):
        return len(self.data) == 0

    def remove_value(self, value):
        if value in self.data:
            self.data.remove(value)
            return True
        return False

    def replace(self, index, value):
        self.data[index] = value

    def concat(self, other):
        return self.data + list(other)

    def slice(self, start, end):
        return self.data[start:end]

    def filter(self, function):
        return list(filter(function, self.data))

    def map(self, function):
        return list(map(function, self.data))

    def reduce(self, function):
        if self.is_empty():
            return None
        result = self.data[0]
        for value in self.data[1:]:
            result = function(result, value)
        return result

    def find(self, function):
        for index, value in enumerate(self.data):
            if function(value):
                return index
        return -1

    def sort(self, key=None, reverse=False):
        return sorted(self.data, key=key, reverse=reverse)

    def __str__(self):
        return str(self.data)


lst = CustomList()
lst.append(1)
lst.append(1)
lst.append(1)
lst.append(1)
lst.append(1)
result = lst.concat([1,2,3,4,5,6,7,8,9,10,11])
print(lst)
print(result)
print(lst.is_empty())
