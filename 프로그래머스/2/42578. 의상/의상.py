from collections import defaultdict


def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    
    for v, k in clothes:
        clothes_dict[k].append(v)
        
    for v in clothes_dict.values():
        answer *= len(v) + 1
        
    return answer - 1