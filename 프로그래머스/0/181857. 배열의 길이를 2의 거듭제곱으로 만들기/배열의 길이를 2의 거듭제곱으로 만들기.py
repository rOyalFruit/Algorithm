def solution(arr):
    i = 0
    
    while len(arr) > 2 ** i:
        i += 1
    
    arr.extend([0 for _ in range(2 ** i - len(arr))])
    return arr