def find_num_set(num, other):
    result = set()
    if num != "":
        result.add(num)

    for i in range(len(other)):
        result.update(find_num_set(num + other[i], other[:i] + other[i + 1:]))

    return result


def is_prime(num):
    if num == 0 or num == 1:
        return 0
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    
    return 1
    
    
def solution(numbers):
    answer = 0
    num_set = set(map(int, find_num_set("", numbers)))
    
    for num in num_set:
        answer += is_prime(num)
        
    return answer
