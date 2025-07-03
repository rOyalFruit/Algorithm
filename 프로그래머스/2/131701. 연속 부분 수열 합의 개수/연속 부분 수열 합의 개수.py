def solution(elements):
    answer = set()
    n = len(elements)
    elements = elements * 2
    
    for length in range(1, n + 1):
        current_sum = sum(elements[:length])
        answer.add(current_sum)
        
        for start in range(n):
            current_sum = current_sum - elements[start] + elements[start + length]
            answer.add(current_sum)
    
    return len(answer)