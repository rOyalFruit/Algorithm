def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    a_idx = 0
    for i in range(len(B)):
        if B[i] <= A[a_idx]:
            continue
        answer += 1
        a_idx += 1
            
    return answer