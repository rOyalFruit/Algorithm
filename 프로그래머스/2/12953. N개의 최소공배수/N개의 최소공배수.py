def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        
    return a


def solution(arr):
    answer = 1
    for num in arr:
        answer = answer * num // gcd(answer, num)
        
    return answer