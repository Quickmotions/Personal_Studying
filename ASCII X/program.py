# https://www.codewars.com/kata/latest/my-languages?beta=false
# Fergus Haak - 07/09/2022 - ASCII Fun #1: X-Shape
from operator import add


def x(n):
    shape = ""
    seqence = [0, 1, n - 2, 1, 0]
    for line in range(n):
        shape += "□" * seqence[0] + "■" * seqence[1] + "□" * seqence[2] + "■" * seqence[3] + "□" * seqence[4] + "\n"
        if line < n-1 / 2:
            seqence = list(map(add, seqence, [1, 0, -2, 0, 1]))
        elif line == n-1 / 2:
            seqence = list(map(add, seqence, [1, 0, -1, 0, 1]))
        else:
            seqence = list(map(add, seqence, [-1, 0, 2, 0, -1]))

    return shape


print(x(5))
