def solution(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()  # 연속된 같은 문자 제거
        else:
            stack.append(c)
    
    return 1 if len(stack) == 0 else 0