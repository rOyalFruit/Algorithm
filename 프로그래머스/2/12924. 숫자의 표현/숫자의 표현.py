def solution(n):
    answer = 0
    start = 1
    sum_val = 0
    
    for i in range(1, n+1):
        sum_val += i
        
        while sum_val > n:
            sum_val -= start
            start += 1
            
        if sum_val == n:
            answer += 1
            
    return answer