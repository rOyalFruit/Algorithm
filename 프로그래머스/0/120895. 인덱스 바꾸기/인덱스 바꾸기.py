def solution(my_string, num1, num2):
    lst = list(my_string)
    lst[num1], lst[num2] = my_string[num2], my_string[num1]
    return ''.join(lst)