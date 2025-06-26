def solution(a, b):
    return sum(num1 * num2 for num1, num2 in zip(a, b))