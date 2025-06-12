from collections import defaultdict


def solution(strArr):
    len_dict = defaultdict(int)
    
    for s in strArr:
        len_dict[len(s)] += 1
    
    return max(len_dict.values())