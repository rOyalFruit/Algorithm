def find_permutations(current, remaining):
    result = []
    
    if not remaining:  # 모든 요소가 선택되었을 때 (완전한 순열)
        if current:  # 빈 리스트가 아닌 경우에만 추가
            result.append(current)
        return result
    
    # 길이가 1부터 최대 길이의 순열까지 모든 결과물을 포함하려면 리턴 조건 수정하면 됨.
    # 
    # if current: # 현재 순열을 결과에 추가 (빈 리스트가 아닌 경우)
    #     result.append(current)
    #
    # if not remaining: # 남은 요소가 없으면 현재 결과 반환
    #     return result
    
    for i in range(len(remaining)):
        new_current = current + [remaining[i]]
        new_remaining = remaining[:i] + remaining[i+1:]
        result.extend(find_permutations(new_current, new_remaining))
        
    return result
        

def solution(k, dungeons):
    answer = 0
    
    for perm in find_permutations([], dungeons):
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