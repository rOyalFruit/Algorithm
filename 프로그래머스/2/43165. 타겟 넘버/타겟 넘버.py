from collections import deque


def solution(numbers, target):
    q = deque([(0, 0)])
    count = 0
    
    while q:
        cur_sum, index = q.popleft()
        
        if index == len(numbers):
            if cur_sum == target:
                count += 1
        else:
            q.append((cur_sum + numbers[index], index + 1))  # 현재 숫자를 더하는 경우
            q.append((cur_sum - numbers[index], index + 1))  # 현재 숫자를 빼는 경우
            
    return count