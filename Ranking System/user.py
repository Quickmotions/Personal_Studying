# Codewars style ranking system - 24/08/2022 - Fergus Haak
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python

class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_minus_one(self):
        if self.rank - 1 == 0:
            return self.rank - 2
        return self.rank - 1

    def inc_progress(self, act_rank: int):
        if act_rank == self.rank:
            self.progress += 3
        elif act_rank == self.rank_minus_one():
            self.progress += 1
        elif act_rank not in [-1, -2, -3, -4, -5, -6, -7, -8, 1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError("Rank must be in range [-8,-1]U[1,8]")
        elif act_rank > self.rank != 8:
            if act_rank > 0 and self.rank < 0:
                act_rank -= 1
            self.progress += abs(self.rank - act_rank) * abs(self.rank - act_rank) * 10
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0: self.rank = 1
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
