from functools import cmp_to_key


def solution(numbers):

    def compare(x, y):
        return int(y+x) - int(x+y)

    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    return '0' if numbers[0] == '0' else ''.join(numbers)