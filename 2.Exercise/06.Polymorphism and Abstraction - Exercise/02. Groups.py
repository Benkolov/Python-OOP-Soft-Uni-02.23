class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __repr__(self):
        members = ", ".join([str(person) for person in self.people])
        return f"Group {self.name} with members {members}"

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f"{self.people[0].name} {other.people[0].surname}"
        people = self.people + other.people
        return Group(name, people)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.people):
            raise StopIteration
        else:
            person = self.people[self.index]
            self.index += 1
            return f"Person {self.index}: {person}"

    def __getitem__(self, index):
        return self.people[index]


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
