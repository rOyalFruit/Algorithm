def solution(d, budget):
    d.sort()
    total = 0
    
    for idx, cost in enumerate(d):
        total += cost
        if total > budget:
            return idx
        
    return len(d)
