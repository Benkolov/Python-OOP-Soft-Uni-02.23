def reverse_text(input_string):
    for i in range(len(input_string) - 1, -1, -1):
        yield input_string[i]


# Example usage:
for char in reverse_text("step"):
    print(char, end='')
