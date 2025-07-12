def convert_to_base(n, k):
    if n == 0:
        return '0'
    
    digits = '0123456789'
    result = ''
    
    while n > 0:
        result = digits[n % k] + result
        n //= k
    
    return result


def is_prime(num):
    if num == 2:
        return True
    
    if num % 2 == 0 or num < 2:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True


def solution(n, k):
    answer = 0
    numbers = [int(num) for num in convert_to_base(n, k).split('0') if len(num) > 0]
    
    for num in numbers:
        if is_prime(num):
            answer += 1
            
    return answer
