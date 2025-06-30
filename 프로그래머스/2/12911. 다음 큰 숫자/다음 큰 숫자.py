def solution(n):
    target = bin(n)[2:].count('1')
    next = n + 1
    
    while bin(next)[2:].count('1') != target:
        next += 1
        
    return next