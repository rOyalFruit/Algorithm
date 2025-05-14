def solution(priorities, location):
    answer = 0
    lst = ([[i, v]for i, v in enumerate(priorities)])
    
    while True:
        cur = lst.pop(0)
        if any(cur[1] < e[1] for e in lst):
            lst.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
                