def solution(n):
    a, b = 1, 1
    
    for i in range(1, n):
        a, b = b, (a+b) % 1_000_000_007
        
    return b


        
