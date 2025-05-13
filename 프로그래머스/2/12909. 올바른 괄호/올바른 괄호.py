def solution(s):
    lst = []
    
    for char in s:
        if len(lst) <= 0 and char == ')':
            return False
            
        if char == '(':
            lst.append(char)
        else:
            lst.pop(-1)
            
    return len(lst) == 0