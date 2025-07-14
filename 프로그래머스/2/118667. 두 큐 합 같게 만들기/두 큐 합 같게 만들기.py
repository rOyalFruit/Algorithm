from collections import deque


def solution(queue1, queue2):
    answer = 0
    max_idx = len(queue1) + len(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    
    while answer <= max_idx+1 and q1_sum != q2_sum:
        if q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
        else:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        
        answer += 1
        
    return answer if q1_sum == q2_sum else -1