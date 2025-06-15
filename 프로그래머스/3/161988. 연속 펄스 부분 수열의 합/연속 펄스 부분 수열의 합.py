def solution(sequence):
    new_sequence = [x if i % 2 == 0 else -1 * x for i, x in enumerate(sequence)]
    
    max_sum = curr_max = new_sequence[0]
    min_sum = curr_min = new_sequence[0]
    
    for num in new_sequence[1:]:
        # 최대 부분합 계산
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)
        
        # 최소 부분합 계산
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)
        
    return max(abs(max_sum), abs(min_sum))