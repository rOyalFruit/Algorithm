def solution(land):
    n = len(land)
    for i in range(1, n):
        for j in range(4):
            temp = land[i][j]
            for k in range(4):
                if j == k:
                    continue
                land[i][j] = max(land[i][j], temp + land[i-1][k])
                
    return max(land[n-1])