def solution(n, s):
    if n > s:
        return [-1]
    
    remain = s - (s // n) * n
    answer = [s // n for _ in range(n)]
    for i in range(1, remain+1):
        answer[-i] += 1
        
    return answer