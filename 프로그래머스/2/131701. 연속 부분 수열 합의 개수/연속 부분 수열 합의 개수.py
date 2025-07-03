def solution(elements):
    answer = set()
    n = len(elements)
    
    for length in range(1, n + 1):
        current_sum = sum(elements[:length])  # 첫 번째 윈도우
        answer.add(current_sum)
        
        for start in range(n):
            # mod 연산으로 원형 배열 처리
            remove_idx = start
            add_idx = (start + length) % n
            current_sum = current_sum - elements[remove_idx] + elements[add_idx]
            answer.add(current_sum)
    
    return len(answer)