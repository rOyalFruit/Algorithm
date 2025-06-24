def solution(diffs, times, limit):
    n = len(diffs)
    left, right = 1, max(diffs)
    
    while left <= right:
        level = (left + right) // 2
        total = 0
        
        for i in range(n):
            diff = diffs[i]
            time = times[i]
            
            if level >= diff:
                total += time
            else:
                total += (time + times[i-1]) * (diff - level) + time
        
        if total <= limit:
            right = level-1
        else:
            left = level+1
            
    return left
