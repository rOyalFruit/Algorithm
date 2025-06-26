from itertools import combinations


def solution(number):
    return sum(1 if sum(lst) == 0 else 0 for lst in combinations(number, 3))