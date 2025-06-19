from collections import deque


def solution(stones, k):
    dq = deque()
    answer = float('inf')
    
    for i, stone in enumerate(stones):
        # Step 1: 윈도우 범위 벗어난 인덱스 제거
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        # Step 2: 현재 값보다 작은 값들 제거.
        # dq[-1]로 뒤에서부터 제거해야 함
        while dq and stones[dq[-1]] <= stone:
            dq.pop()
        
        # Step 3: 현재 인덱스 추가
        dq.append(i)

        # Step 4: 윈도우 완성 시 정답 갱신
        if i >= k - 1:
            answer = min(answer, stones[dq[0]])
            
    return answer
