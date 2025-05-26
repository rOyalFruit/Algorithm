from itertools import product


def solution(word):
    words = []
    for i in range(1, 5+1):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append("".join(p))

    return sorted(words).index(word) + 1