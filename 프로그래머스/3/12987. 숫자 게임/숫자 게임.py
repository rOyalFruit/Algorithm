def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_idx = 0
    
    for i in range(len(B)):
        if A[a_idx] < B[i]:
            answer += 1
            a_idx += 1
            
    return answer
