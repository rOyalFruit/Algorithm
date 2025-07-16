def solution(n, s):
    if n > s:
        return [-1]
    
    quotient, remainder = divmod(s, n)
    answer = [quotient] * (n - remainder) + [quotient + 1] * remainder # ex) [4] + [5]
    
    return answer
