def solution(n):
    answer = [[0] * (i+1) for i in range(n)]
    num = 1
    ci, cj = -1, 0
    di = [1, 0, -1]
    dj = [0, 1, -1]
    
    for i in range(n):
        d = i % 3
        
        for j in range(n - i):
            ci += di[d]
            cj += dj[d]
            answer[ci][cj] = num
            num += 1
    
    return [answer[i][j] for i in range(n) for j in range(i+1)]
