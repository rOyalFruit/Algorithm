from collections import deque


def bfs(i, j, land, visited):
    n, m = len(land), len(land[0])
    q = deque([(i, j)])
    visited[i][j] = True
    columns_set = set() 
    quantity = 0
    
    while q:
        ci, cj = q.popleft()
        columns_set.add(cj)   # 석유가 있는 열 추가
        quantity += 1
        
        for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < n and 0 <= nj < m and land[ni][nj] and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    
    return columns_set, quantity


def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    col_totals = [0] * m  # 열별 총합 저장
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                columns, oil_amount = bfs(i, j, land, visited)
                for col in columns:
                    col_totals[col] += oil_amount
                    
    return max(col_totals)
