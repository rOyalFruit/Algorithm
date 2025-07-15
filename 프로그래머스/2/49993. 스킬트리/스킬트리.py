from collections import defaultdict


def solution(skill, skill_trees):
    answer = 0
    d = defaultdict(int)
    for i, c in enumerate(skill):
        d[c] = i + 1
    
    for s in skill_trees:
        lst = []
        for c in s:
            if d[c] > 0:
                lst.append(d[c])
        
        temp = list(range(1, len(lst)+1))
        if lst == temp:
            answer += 1
            
    return answer