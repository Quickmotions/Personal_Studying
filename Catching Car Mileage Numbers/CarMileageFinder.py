# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
# 16/08/2022 Fergus Haak

def is_interesting(number, awesome_phrases):
    numbers = [number, number + 1, number + 2]
    current = 0
    for n in numbers:
        n_split = [int(a) for a in str(n)]
        current += 1
        if current == 1:
            return_value = 2
        else:
            return_value = 1
        if n < 100:
            continue
        # Any digit followed by all zeros: 100, 90000
        for digit in n_split[1:]:
            if digit != 0:
                break
        else:
            return return_value
        # Every digit is the same number: 1111
        for digit in n_split[1:]:
            if digit != n_split[0]:
                break
        else:
            return return_value
        # The digits are sequential, incrementing: 1234
        current = n_split[0]
        for digit in n_split[1:]:
            if digit == current + 1 or current == 9 and digit == 0:
                current = digit
            else:
                break
        else:
            return return_value
        # The digits are sequential, decrementing: 4321
        current = n_split[0]
        for digit in n_split[1:]:
            if digit == current - 1:
                current = digit
            else:
                break
        else:
            return return_value
        # The digits are a palindrome: 1221 or 73837
        if n_split == n_split[::-1]:
            return return_value
        # The digits match one of the values in the awesome_phrases array
        if n in awesome_phrases:
            return return_value
    return 0


tests = [
    {'n': 100, 'interesting': [1337, 256], 'expected': 0},
    {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
    {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
    {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
    {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
    {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
]
for t in tests:
    print(is_interesting(t["n"], t["interesting"]))
