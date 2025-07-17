import math


def solution(n, stations, w):
    answer = 0
    start = 1
    lst = []
    coverage = 1 + w * 2
    
    for station in stations:
        uncovered_length = station - w - start
        start = station + w + 1
        lst.append(uncovered_length)
    
    if start <= n:
        remaining_length = n - start + 1
        lst.append(remaining_length)
    
    for num in lst:
        answer += math.ceil(num / coverage)
        
    return answer
