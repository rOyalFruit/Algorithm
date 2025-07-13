def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i, j in puddles:  # 물웅덩이 좌표 반대로 돼 있음
        dp[j][i] = -1     # 물웅덩이 표시 (-1로 표시)
    
    # 시작점 설정
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 물웅덩이인 경우
                dp[i][j] = 0
                continue
            
            if i == 1 and j == 1: 
                continue

            up = dp[i-1][j] if dp[i-1][j] != -1 else 0
            left = dp[i][j-1] if dp[i][j-1] != -1 else 0
            dp[i][j] = (up + left) % 1000000007
    
    return dp[n][m]
