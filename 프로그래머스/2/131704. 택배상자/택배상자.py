from collections import deque


def solution(order):
    order = deque(order)
    answer = 0
    stack = []
    
    for i in range(1, len(order)+1):
        if i == order[0]:
            order.popleft()
            answer += 1
            
            while stack and stack[-1] == order[0]:
                stack.pop()
                order.popleft()
                answer += 1
                
        else:
            stack.append(i)
        
    return answer