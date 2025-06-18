from itertools import permutations


def solution(babbling):
    word_list = []
    for i in range(1, 4+1):
        for word in permutations(["aya", "ye", "woo", "ma"], i):
            word_list.append("".join(word))
            
    return sum([1 if i in word_list else 0 for i in babbling])