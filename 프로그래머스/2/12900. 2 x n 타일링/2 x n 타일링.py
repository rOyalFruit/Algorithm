def solution(n):
    answer = 0
    a, b = 1, 2
    
    if n <= 2:
        return n
    
    for i in range(3, n+1):
        answer = (a + b) % 1_000_000_007
        a = b
        b = answer
        
    return answer