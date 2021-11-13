# Create a RomanNumerals class that can convert a roman numeral to and from
# an integer value. It should follow the API demonstrated in the examples
# below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately
# starting with the left most digit and skipping any digit with a value
# of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC;
# resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000
# 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

class RomanNumerals:
    def __init__(self):
        self.num = [1, 4, 5, 9, 10, 40, 50, 90,
                    100, 400, 500, 900, 1000]
        self.sym = ["I", "IV", "V", "IX", "X", "XL",
                    "L", "XC", "C", "CD", "D", "CM", "M"]

    def to_roman(self, number):
        i = 12
        roman_str = ""
        while number:
            div = number // self.num[i]
            number %= self.num[i]

            while div:
                roman_str += self.sym[i]
                div -= 1
            i -= 1
        return roman_str

    def from_roman(self, roman_num):
        num_out = 0
        while roman_num:
            i = 12
            for s in reversed(self.sym):
                if roman_num.startswith(s):
                    roman_num = roman_num[(len(s)):]
                    num_out += self.num[i]
                i -= 1
        return num_out


roman = RomanNumerals()

print(roman.from_roman("IV"))
