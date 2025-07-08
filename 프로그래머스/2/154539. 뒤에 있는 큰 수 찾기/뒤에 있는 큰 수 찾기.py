def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and num > numbers[stack[-1]]:
            answer[stack[-1]] = num
            stack.pop()
            
        stack.append(i)
    
    return answer