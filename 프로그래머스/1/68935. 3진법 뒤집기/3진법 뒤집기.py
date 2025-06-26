def solution(n):
    digits = ''
    
    while n:
        n, remainder = divmod(n, 3)
        digits += str(remainder)
        
    return int(digits, 3)
