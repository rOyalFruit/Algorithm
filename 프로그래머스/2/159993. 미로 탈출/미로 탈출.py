from collections import deque


def bfs(li, lj, maps):
    visited = [[0 for _ in range(len(maps[i]))] for i in range(len(maps))]
    q = deque([(li, lj)])
    visited[li][lj] = 0
    s_dist = e_dist = 0
    
    while q:
        ci, cj = q.popleft()
        
        if maps[ci][cj] == 'S':
            s_dist = visited[ci][cj]
        
        if maps[ci][cj] == 'E':
            e_dist = visited[ci][cj]
            
        if s_dist > 0 and e_dist > 0:
            return s_dist + e_dist
        
        for di, dj in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            ni = ci + di
            nj = cj + dj
            
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[ci]) and maps[ni][nj] != 'X' and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    
    return -1


def solution(maps):
    li, lj = -1, -1  # 레버 좌표
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'L':
                li, lj = i, j

    return bfs(li, lj, maps)