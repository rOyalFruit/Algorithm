from collections import Counter


def solution(k, tangerine):
    answer = 0
    sum_val = 0
    count = Counter(tangerine)
    
    for val in sorted(count.values(), reverse=True):
        if sum_val >= k:
            break
            
        sum_val += val
        answer += 1
        
    return answer