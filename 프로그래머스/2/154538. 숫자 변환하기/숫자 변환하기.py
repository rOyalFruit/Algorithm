from collections import deque


def solution(x, y, n):
    q = deque([(x, 0)])
    visited = {x}
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == y:
            return cnt
        
        for next_num in [cur + n, cur * 2, cur * 3]:
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt+1))
                
    return -1