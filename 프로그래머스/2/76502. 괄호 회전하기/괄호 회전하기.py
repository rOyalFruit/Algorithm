def solution(s):
    answer = 0
    
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        stack = []
        
        for j in range(len(s)):
            c = new_s[j]
            if c in "({[":
                stack.append(new_s[j])
            else:
                if not stack:
                    stack.append(c)
                    break
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    break
        
        if not stack:
            answer += 1
            
    return answer