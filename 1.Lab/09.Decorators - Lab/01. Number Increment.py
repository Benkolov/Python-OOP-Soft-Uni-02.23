def number_increment(numbers):
    def increase():
        result = [el+1 for el in numbers]
        return result
    return increase()
