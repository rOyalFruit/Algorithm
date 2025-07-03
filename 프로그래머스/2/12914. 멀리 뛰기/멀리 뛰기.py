def solution(n):
    if n == 1 or n == 2:
        return n
    
    prev, curr = 1, 2
    for i in range(3, n+1):
        prev, curr = curr, prev + curr
        
    return curr % 1234567
