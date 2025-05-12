def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection
    
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    return n - len(lost_set)