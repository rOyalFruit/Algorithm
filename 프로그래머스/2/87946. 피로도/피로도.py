from itertools import permutations
        

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons):
        count = 0
        fatigue = k
    
        for required_k, cost in perm:
            if required_k <= fatigue:
                count += 1
                fatigue -= cost
            else:
                break
        
        answer = max(answer, count)
        
    return answer