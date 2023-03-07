class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        else:
            return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(value)):
            if i > 0 and roman_dict[value[i]] > roman_dict[value[i-1]]:
                result += roman_dict[value[i]] - 2 * roman_dict[value[i-1]]
            else:
                result += roman_dict[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"
