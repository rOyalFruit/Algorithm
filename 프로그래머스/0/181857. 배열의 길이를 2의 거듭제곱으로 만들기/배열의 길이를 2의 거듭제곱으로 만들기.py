def solution(arr):
    i = 1
    
    while len(arr) > i:
        i *= 2
    
    return arr + [0] * (i-len(arr))
