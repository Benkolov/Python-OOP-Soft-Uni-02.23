class vowels:
    def __init__(self, input_string):
        self.input_string = input_string
        self.vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.input_string):
            current_char = self.input_string[self.index]
            self.index += 1
            if current_char in self.vowels:
                return current_char
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
