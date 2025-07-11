from collections import deque


def solution(n, t, m, p):
    d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    result = [0]
    i = 1
    
    while True:
        if len(result) >= t * m:
            break
            
        dq = deque()
        num = i
        while num != 0:
            num, remainder = divmod(num, n)
            dq.appendleft(remainder)

        result.extend([i if i < 10 else d[i] for i in dq])
        i += 1
    
    return "".join(map(str, result[p-1:t*m:m]))