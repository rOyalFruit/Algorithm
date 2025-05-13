def solution(s):
    lst = []
    for char in s:
        if char == '(':
            lst.append(char)
        else:
            if len(lst) <= 0:
                return False
            lst.pop(-1)
    return len(lst) == 0