def solution(elements):
    answer = set()
    elements.extend(elements)
    n = len(elements) // 2
    
    for i in range(1, n+1):
        for j in range(0, n):
            answer.add(sum(elements[j:j+i]))
                        
    return len(answer)