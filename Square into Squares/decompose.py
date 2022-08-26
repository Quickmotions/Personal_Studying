# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python
# Fergus Haak - 24/08/2022 - Square into Square Challenge

from itertools import combinations

def decompose(n):
    results = []
    sample = []
    for _ in range(n-1):
        sample.append(len(sample) + 1)
    list_combinations = list()
    for i in range(len(sample) + 1):
        list_combinations += list(combinations(sample, i))
    for option in list_combinations:
        total = n**2
        for number in option:
            total -= number**2
        if total == 0:
            results.append(option)
    if len(results) == 0:
        return None
    result = results[0]
    for option in results:
        if len(option) < len(result):
            result = option
    return list(result)


# tests
print(decompose(30))  # [3,4]
print(decompose(8))  # none

