def solution(sequence, k):
    n = len(sequence)   
    answer = [0, n-1]
    right = n-1
    window = 0
    
    for i in range(n-1, -1, -1):
        window += sequence[i]
        
        if window > k:
            window -= sequence[right]
            right -= 1

        if window == k and right - i <= answer[1] - answer[0]:
            answer = [i, right]    
        
    return answer